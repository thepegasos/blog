import numpy as np
from cost import compute_cost
from model import compute_model_output, compute_model_output_nn


def gradient_decent(iterations, W, X, Y, alpha):
    """
    returns the learned parameters w, b and list of cost per iteration
    """
    m = len(X)
    all_costs = []
    for i in range(iterations):
        
        # model_prediction = compute_model_output(w, x, b)
        preds = compute_model_output(X=X, W=W).values.reshape(len(X), 1)
        # cost = compute_cost(y_pred=model_prediction, y=y, m=m)
        cost = compute_cost(predictions=preds, Y=Y)
        # dw,db = compute_gradients(model_prediction, y, x, m)
        dW = compute_gradients(predictions=preds, Y=Y, X=X.values, m=len(X))
        # w, b = update_parameters(w, b, dw, db, alpha)
        W = update_parameters(W=W, dW=dW, alpha=alpha)
        all_costs.append(cost)
        print_at = iterations/10
        if i%print_at == 0: # only print 10 progress costs
            print(f"Iteration # {i}, cost: {cost}")
    return W, all_costs


def gradient_decent_nn(iterations, W, X, Y, alpha):
    """
    returns the learned parameters w, b and list of cost per iteration
    """
    m = len(X)
    all_costs = []
    for i in range(iterations):
        
        # model_prediction = compute_model_output(w, x, b)
        # preds = compute_model_output(X=X, W=W).values.reshape(len(X), 1) # For linear
        preds = compute_model_output_nn(X=X, W=W).reshape(len(X), 1) # for DL
        # cost = compute_cost(y_pred=model_prediction, y=y, m=m)
        cost = compute_cost(predictions=preds, Y=Y)
        # dw,db = compute_gradients(model_prediction, y, x, m)
        dW = compute_gradients(predictions=preds, Y=Y, X=X.values, m=len(X))
        # w, b = update_parameters(w, b, dw, db, alpha)
        W = update_parameters(W=W, dW=dW, alpha=alpha)
        all_costs.append(cost)
        print_at = iterations/10
        if i%print_at == 0: # only print 10 progress costs
            print(f"Iteration # {i}, cost: {cost}")
    return W, all_costs

# def compute_gradients(y_pred, y, x, m):
#     diff_per_example = (y_pred - y)/m
#     dj_dw = diff_per_example*x
#     dj_db = diff_per_example
#     return dj_dw, dj_db


# def update_parameters(w, b, dw, db, alpha):
#     w = w - alpha*sum(dw)
#     b = b - alpha*sum(db)
#     return w, b

def compute_gradients(predictions, Y, X, m):
    diff_per_example = (predictions - Y)/m
    dj_dW = np.matmul(X.T, diff_per_example).round(2)
    return dj_dW


def update_parameters(W, dW, alpha):
    W = W - alpha*dW
    return W