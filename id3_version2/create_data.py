import numpy as np
import pandas as pd
import math

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

    e = np.array(part_entrop)

    size = np.sum(e[:,1])

    information = sum([item[0]/size*item[1] for item in part_entrop])

    return information


def calculate_gain(df_set, set_entropy, partition_name, output_classes):
    '''
    Gain(X,T) = H(T) - H(X,T)
    '''

    
    df_partition = df_set[partition_name]

    part_classes = df_partition.unique()


    part_entropy = [calculate_entropy(df_set.loc[df_partition == t_class], output_classes) for t_class in part_classes]


    information = calculate_information(part_entropy)

    gain = set_entropy - information

    return gain



def execute():
    df_set = pd.read_csv('data.csv')
    output_classes = df_set.play.unique()
    set_entropy = calculate_entropy(df_set, output_classes)[0]

    print( f'temperature gain :{calculate_gain(df_set, set_entropy, "temperature", output_classes)}')
    print( f'outlook gain :{calculate_gain(df_set, set_entropy, "outlook", output_classes)}')
    print( f'humidity gain :{calculate_gain(df_set, set_entropy, "humidity", output_classes)}')
    print( f'windy gain :{calculate_gain(df_set, set_entropy, "windy", output_classes)}')



if __name__ == "__main__":
    execute()
