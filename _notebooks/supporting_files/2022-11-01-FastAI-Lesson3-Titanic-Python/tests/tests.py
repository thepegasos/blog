import pytest
import os
import numpy as np
import sys

THIS_FILE_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.add(THIS_FILE_DIR_PATH/"..")



def test_update_parameters():
    W = np.array([[1,2,3], [4,5,6]])
    dW = np.array([[1, 0, 1], [0, 1, 1]])
    alpha = 0.1
    updated_W = update_parameters(W=W, dW=dW, alpha=0.1)
    true_W = np.array([[0.9, 2, 2.9], [4, 4.9, 5.9]])
    # print(updated_W)
    # print(true_W)
    assert (updated_W == true_W).all()

def test_compute_gradients():
    preds = np.array([10, 20, 30, 35, 40])
    Y = np.array([10, 15, 29, 30, 42])
    X = np.array([[range(1,5)], [range(5, 9)], \
        [range(9, 13)], [range(13, 17)], [range(17, 21)]])
    m = 5
    diff_per_example = (preds - Y)/m
    dj_dW_compute = compute_gradients(predictions=preds, Y=Y, X=X, m=m)
    dj_dW_orig = np.matmul(X.T, diff_per_example).round(2)
    assert (dj_dW_orig == dj_dW_compute).all()
