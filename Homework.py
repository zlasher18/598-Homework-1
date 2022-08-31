import scipy
from scipy.optimize import minimize


def function(paramt):
    x1, x2, x3, x4, x5 = paramt
    return (x1-x2)**2+(x2+x3-2)**2+(x4-1)**2+(x5-1)**2
const = ({'type':'eq','fun':lambda paramt: x1+ 3*x2 },
    {'type':'eq','fun':lambda paramt: x3+x4-2*x5},
    {'type':'eq','fun':lambda paramt: x2-x5})

b = scipy.optimize.Bounds(-10,10,keep_feasible=False)
guess1 = [5,5,5,5,5]
result = minimize(function,guess1,bounds=b,constraints=const)
result.x
