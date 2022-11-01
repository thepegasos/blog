# %%
import numpy as np

# %%
def compute_model_output(X, W):
    # model: W*X 
        # W = n x m, 
        # n= number of examples
        # m= number of features (weights) + constant term
    
    # input: weights and x matrix
    # output: predictions (n x 1)
    
    return np.matmul(X, W)

# %%

def compute_model_output_nn(X, W):
    # model: W*X 
        # W = n x m, 
        # n= number of examples
        # m= number of features (weights) + constant term
    
    # input: weights and x matrix
    # output: predictions (n x 1)
    
    linear_preds = np.matmul(X, W)
    lin_relu_preds = np.where(linear_preds < 0, 0, linear_preds) # make negative values zero
    return np.sum(lin_relu_preds, axis=1)


