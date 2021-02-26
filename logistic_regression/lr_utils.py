import numpy as np
import h5py
import os

def load_dataset():

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = '../datasets/train_catvnoncat.h5'
    abs_file_path = os.path.join(script_dir, rel_path)
    train_dataset = h5py.File(abs_file_path, "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:]) # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:]) # your train set labels

    rel_path = '../datasets/test_catvnoncat.h5'
    abs_file_path = os.path.join(script_dir, rel_path)
    test_dataset = h5py.File(abs_file_path, "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:]) # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:]) # your test set labels

    classes = np.array(test_dataset["list_classes"][:]) # the list of classes
    
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes

