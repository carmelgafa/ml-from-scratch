'''
classification using ID3 algorithm
'''
import numpy as np
from algorithms.utils.simple_tree import SimpleTree

class ID3Classifier:
    '''
    execution of ID3 algorithm to classify data
    '''

    def __init__(self):
        '''
        init function
        '''
        self.result_tree = SimpleTree()
        self.POSITIVE_VAL = 'Yes'
        self.NEGATIVE_VAL = 'No'

        self.ATTRIB_NAME = 'Attrib'
        self.VALUE_NAME = 'Value'

    def id3_compute(self, attrib_names, attribs, targets):
        '''
        interface function to start the execution of ID3 process
        '''

        for attrib_name in attrib_names:
            self.result_tree.add_node(attrib_name)

        self.result_tree.add_leafnode(self.POSITIVE_VAL)
        self.result_tree.add_leafnode(self.NEGATIVE_VAL)

        parent = {self.ATTRIB_NAME: None, self.VALUE_NAME: None}
        self.__id3(attrib_names, attribs, targets, parent)

    def display_tree(self):
        '''
        displays the results tree
        '''
        self.result_tree.display()
        self.result_tree.show()

    def __id3(self, attrib_names, attribs, targets, parent):
        '''
        Actual ID3 algorithm that is executed recursively to classify the data
        '''
        # calculate the entropy of the set
        unique, counts = np.unique(targets, return_counts=True)
        unique_counts = dict(zip(unique, counts))
        total_count = len(targets)

        if len(unique) == 1:
            leaf_value = unique[0]
            self.result_tree.add_edge(parent[self.ATTRIB_NAME], leaf_value, parent[self.VALUE_NAME])
        else:
            # prob of results
            prob_yes = unique_counts[self.POSITIVE_VAL] / total_count
            prob_no = unique_counts[self.NEGATIVE_VAL] / total_count

            # entropy calculation
            entropy_set = -((prob_yes * np.log2(prob_yes)) +
                            (prob_no * np.log2(prob_no)))

            # list to contain info gain of all attributes
            attrib_gains = []

            # loop through all attributes
            for idx, _ in enumerate(attrib_names):
                # get all possible values for the attribute, e.g. for temp (hot,mild,cold)
                node_unique_vals = np.unique(attribs[:, idx])
                # the info gaine will be the set entropy minus the attriutre entropies
                # initialize gain with set entropy
                attrib_info_gain = entropy_set

                # loop through unique values
                for aval in node_unique_vals:
                    # get how many attribues have that value
                    aval_filter = attribs[:, idx] == aval
                    aval_count = np.count_nonzero(aval_filter)
                    # how many of these are true and false
                    aval_res_true = np.count_nonzero(
                        targets[aval_filter] == self.POSITIVE_VAL) / aval_count
                    aval_res_false = np.count_nonzero(
                        targets[aval_filter] == self.NEGATIVE_VAL) / aval_count

                    # the value will be 0 if one of the above values is 0 cause log 0
                    aval_entropy = 0
                    if aval_res_false != 0 and aval_res_true != 0:
                        aval_entropy = -((aval_res_true * np.log2(aval_res_true))
                                         + (aval_res_false * np.log2(aval_res_false)))

                    # factor into the info gain
                    attrib_info_gain = attrib_info_gain - \
                        (aval_entropy * (aval_count / total_count))

                # append the attribute info gain
                attrib_gains.append(attrib_info_gain)

            # select the attribute with the maximum info gain
            selected_attrib_filter = np.where(
                attrib_gains == np.max(attrib_gains))

            # get the index of this attribute
            selected_attribute_idx = selected_attrib_filter[0][0].squeeze()

            # get the attribute name and add it to the tree as a node
            current_attrib = attrib_names[selected_attribute_idx]

            # get the unique values for this attribute
            current_vals = np.unique(
                attribs[:, selected_attrib_filter[0].squeeze()])

            # loop through all values
            for current_val in current_vals:
                # get the items with that value
                attribs_filter = attribs[:, selected_attribute_idx] == current_val
                data_subset = attribs[attribs_filter]
                data_subset = np.delete(data_subset, selected_attribute_idx, 1)
                targets_subset = targets[attribs_filter]
                attribs_names_subset = attrib_names.copy()
                attribs_names_subset.remove(current_attrib)

                if parent[self.ATTRIB_NAME] is None:
                    self.result_tree.rootnode = current_attrib
                else:
                    self.result_tree.add_edge(
                        parent[self.ATTRIB_NAME], current_attrib, parent[self.VALUE_NAME])

                current_parent = {self.ATTRIB_NAME: current_attrib, self.VALUE_NAME: current_val}

                self.__id3(attribs_names_subset, data_subset, targets_subset,
                           current_parent)

    def infer(self, case):
        '''
        goes through the case in hand in the tree and returns the result found

        Arguments:
        ----------

        case: dictionary containing the case in had in the form 'node:branch'
        '''
        result = self.result_tree.traverse(case)
        return result