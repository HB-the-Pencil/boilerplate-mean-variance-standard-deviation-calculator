import numpy as np

def func_array(nparray, func):
    """
    Run a function across both axes of an array and the flattened array.
    """
    
    if "float" in str(type(func(nparray))):
        return [
            func(nparray, axis=0).tolist(),
            func(nparray, axis=1).tolist(),
            float(func(nparray))
        ]
    else:
        return [
            func(nparray, axis=0).tolist(),
            func(nparray, axis=1).tolist(),
            int(func(nparray))
        ]

def calculate(list):
    mtrx = np.array(list)
    try:
        mtrx = mtrx.reshape([3, 3])
    except ValueError as e:
        e.args = ["List must contain nine numbers."]
        raise
    
    calculations = {}
    calculations["mean"] = func_array(mtrx, np.mean)
    calculations["variance"] = func_array(mtrx, np.var)
    calculations["standard deviation"] = func_array(mtrx, np.std)
    calculations["max"] = func_array(mtrx, np.max)
    calculations["min"] = func_array(mtrx, np.min)
    calculations["sum"] = func_array(mtrx, np.sum)


    return calculations