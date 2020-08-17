import numpy as np
import pandas as pd
import math
import os
from simple_tree import SimpleTree

def calculate_entropy(df_set, output_classes):
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
    prob_dist = list((df_set.play == o_class).sum()/set_size  for o_class in output_classes )

    # the entropy of the set is calculated by
    # summing the product of the probability by the log_2 of the probability
    # for each element of the probability distribution
    # As the log_2 of 0 is not defined, we remove these elements
    prob_dist = list(filter(lambda p: p != 0, prob_dist))
    entropy =  sum(list(- p * math.log2(p)  for p in prob_dist))

    return [entropy, set_size]


def calculate_information(part_entrop):

    # part_entrop is a 2D list where each partition is represented by a list
    # such as [entropy, size of partition]. Adding the sizes of the pertitions
    # will result in the size of the original dataset
    e = np.array(part_entrop)
    size = np.sum(e[:,1])

    # the information needed to identify a class is the weighted average of the entropies
    # that is the weighted average needed to identify the class of an element in each subset
    information = sum([item[0] / size * item[1] for item in part_entrop])

    return information


def calculate_gain(df_set, set_entropy, partition_name, output_classes):
    '''
    Gain(X,T) = H(T) - H(X,T)
    '''
    df_partition = df_set[partition_name]
    part_classes = df_partition.unique()

    part_entropy = [calculate_entropy(df_set[df_partition == t_class], output_classes) for t_class in part_classes]

    information = calculate_information(part_entropy)

    gain = set_entropy - information

    return gain



def ID3(input_attribs, output_attrib, training_data):
    output_classes = training_data[output_attrib].unique()


    if len(output_classes) == 1:
        current_node = SimpleTree()
        print(current_node)

        current_node.add_node(output_classes[0])
        # current_node.add_edge(output_classes[0], output_classes[0], output_classes[0])
        return current_node

    else:
        set_entropy = calculate_entropy(training_data, output_classes)[0]

        # print(set_entropy)

        information_gains=[]

        for feature in input_attribs:
            gain = calculate_gain(training_data, set_entropy, feature, output_classes)
            information_gains.append(gain)

        # print(input_attribs)
        # print(information_gains)

        largest_gain_attrib = input_attribs[information_gains.index(max(information_gains))]
        largest_gain_attrib_values = training_data[largest_gain_attrib].unique()

        print(largest_gain_attrib_values)

        new_input_attributes = input_attribs.copy()
        new_input_attributes.remove(largest_gain_attrib)

        print(new_input_attributes)

        current_node = SimpleTree()
        current_node.add_node(largest_gain_attrib)

        for largest_gain_attrib_value in largest_gain_attrib_values:
            # print(largest_gain_attrib_value)
            new_training_data = training_data[training_data[largest_gain_attrib] == largest_gain_attrib_value]
            
            new_node = ID3(new_input_attributes, output_attrib, new_training_data)

            print(type(new_node))
            print(current_node)
            print(largest_gain_attrib_value)

            current_node.append_tree(largest_gain_attrib, new_node, largest_gain_attrib_value)
            
        return current_node





if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(current_dir, "data.csv")

    training_data = pd.read_csv(dataset_path)

    output_attrib = 'play'
    input_attribs = list(training_data.columns)
    input_attribs.remove(output_attrib)
    
    tree = ID3(input_attribs, output_attrib, training_data)

    print(tree.nodes)
    print(tree.tree)
    print(tree.rootnode)



    print(tree.display())