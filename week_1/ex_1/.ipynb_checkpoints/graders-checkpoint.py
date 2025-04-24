import numpy as np

def task1_grader(x,y,xs,ys,n):
    mae = (1/n)*np.sum(np.sqrt((x-xs)**2 + (y-ys)**2))
    passed = True
    if mae > 0.05:
        passed = False
    return mae, passed

def task1_grader_speeds(v,vs,n):
    mae = (1/n)*np.sum((v-vs))
    passed = True
    if mae > 0.05:
        passed = False
    return mae, passed




