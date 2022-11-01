# %%
import numpy as np

# %%
def compute_cost(predictions, Y):
    """
    calculate cost based on two column vectors of size n x 1
    """
    m = len(Y)
    cost_per_datapoint = np.subtract(predictions, Y)**2
    total_cost = sum(cost_per_datapoint)
    # total_cost = sum(cost_per_datapoint/(2*m))
    return total_cost


# def compute_cost(predictions, Y):
#     """
#     calculate cost based on two column vectors of size n x 1
#     """
#     m = len(Y)
#     cost_per_datapoint = np.subtract(predictions, Y)**2
#     total_cost = sum(cost_per_datapoint)
#     return total_cost


