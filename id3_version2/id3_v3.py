import numpy as np
import pandas as pd
import math
import os
from tree import Tree
from tree import TreeBuilderHelper
from tree import TreeNode


class ID3:

    def __init__(self, training_file_name, output_attrib):
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.dataset_path = os.path.join(current_dir, training_file_name)

        self.output_attrib = output_attrib


        self._helper = TreeBuilderHelper(data_filename=training_file_name, output_variable_name=output_attrib)
        self._tree = Tree()


    def calculate_entropy(self, df_set, output_classes):
        '''
        Entropy is calculated by 
        1. obtaining for the probability of every message, probability distribution, p_i
            by dividing the number of elements in each class by the number of elements in the
            set
        2. summing p_i * log_2(p_i)

        This function returns the array [entropy, set_size]. Returning the set size with the 
        entropy makes it easer to calculate the gain
        '''
        set_size = df_set.shape[0]

        # we partition the set of records on the basis if the output attributes
        # the probability distribution of the classes is the number of elements
        # in each class divided by the number of elements in the set
        prob_dist = list((df_set[self.output_attrib] == o_class).sum()/set_size  for o_class in output_classes )

        # the entropy of the set is calculated by
        # summing the product of the probability by the log_2 of the probability
        # for each element of the probability distribution
        # As the log_2 of 0 is not defined, we remove these elements
        prob_dist = list(filter(lambda p: p != 0, prob_dist))
        entropy =  sum(list(- p * math.log2(p)  for p in prob_dist))


        return [entropy, set_size]


    def calculate_information(self, part_entropy):

        # part_entropy is a 2D list where each partition is represented by a list
        # such as [entropy, size of partition]. Adding the sizes of the pertitions
        # will result in the size of the original dataset
        e = np.array(part_entropy)
        size = np.sum(e[:,1])

        # the information needed to identify a class is the weighted average of the entropies
        # that is the weighted average needed to identify the class of an element in each subset
        information = sum([item[0] / size * item[1] for item in part_entropy])

        return information


    def calculate_gain(self, df_set, set_entropy, partition_name, output_classes):
        '''
        Gain(X,T) = H(T) - H(X,T)
        '''
        df_partition = df_set[partition_name]
        part_classes = df_partition.unique()

        part_entropy = [self.calculate_entropy(df_set[df_partition == t_class], output_classes) for t_class in part_classes]

        information = self.calculate_information(part_entropy)

        gain = set_entropy - information


        return gain

    def ID3_exec(self) -> Tree:


        training_data = pd.read_csv(self.dataset_path)


        start_input_attribs = list(training_data.columns)
        start_input_attribs.remove(self.output_attrib)

        root_node = self._ID3_exec_recursive(start_input_attribs, training_data)

        self._tree.set_root_node(root_node)

        return self._tree

    def _ID3_exec_recursive(self, input_attribs, training_data)->TreeNode:
        '''
        '''
        # get the number of output values
        output_classes = training_data[self.output_attrib].unique()

        # if all records have the same output Value
        # return a node with that output Value
        # This will be a leaf node in the tree
        if len(output_classes) == 1:
            
            current_node = self._helper.create_leaf_node(output_classes[0])
            # current_node = RootedDAC()
            # current_node.add_node(output_classes[0])
            return current_node

        # if there is no data, return an error node
        # elif len(training_data) == 0:
        #     current_node = RootedDAC()
        #     current_node.add_node('failure')
        #     return current_node

        # when we cannot return a single node, recursion ensues
        else:
            # compute the information gain for each input attribute relative to training set
            information_gains=[]

            set_entropy = self.calculate_entropy(training_data, output_classes)[0]
            
            for feature in input_attribs:
                gain = self.calculate_gain(training_data, set_entropy, feature, output_classes)
                information_gains.append(gain)

            # get the attribute with the largest gain relative to training set
            # create a node with that attribute
            largest_gain_attrib = input_attribs[information_gains.index(max(information_gains))]
            largest_gain_attrib_values = training_data[largest_gain_attrib].unique()

            # current_node = RootedDAC()
            # current_node.add_node(largest_gain_attrib)

            current_node = self._helper.create_node(largest_gain_attrib)

            # create a copy of input attributes list, removing the selected attribute
            new_input_attributes = input_attribs.copy()
            new_input_attributes.remove(largest_gain_attrib)

            # for all the values of the selected attribute
            # partition the data
            # call ID3 to get a node for that partitioned dataset
            # append the returned node to the selected attribute node, using the value as edge
            for largest_gain_attrib_value in largest_gain_attrib_values:

                new_training_data = training_data[training_data[largest_gain_attrib] == largest_gain_attrib_value]

                new_node = self._ID3_exec_recursive(new_input_attributes, new_training_data)

                current_node.connect_node(largest_gain_attrib_value, new_node)

                # current_node.append_tree(largest_gain_attrib, new_node, largest_gain_attrib_value)

            # return the attribute node
            return current_node

if __name__ == "__main__":

    id3 = ID3("data.csv", 'play')
    tree = id3.ID3_exec()

    tree.display()

    # id3_rules = tree.generate_rules()
    # id3_rules_len = len(id3_rules)

    # print(id3_rules)