import numpy as np
import sys
# from scipy.stats import threshold

def performanceW2(gt, gt_test, array_params=None):

    if isinstance(gt, (list,)):
        gt = np.array(gt)

    if isinstance(gt_test, (list,)):
        gt_test = np.array(gt_test)

    gt = np.where((gt <= 50), 0, gt)
    gt = np.where((gt == 255), 1, gt)
    gt = np.where((gt == 85), -1, gt)
    gt = np.where((gt == 170), -1, gt)

    if not np.array_equal(np.unique(gt_test), [0, 1]):
        gt_test[gt_test!=0] = 1

    TP_list = []
    FP_list = []
    TN_list = []
    FN_list = []

    dim = 1
    if np.array(gt_test).ndim > 3:
        dim = len(gt_test)

    for a in range(dim):
        # True Positive (TP): # pixels correctly segmented as foreground
        TP = np.sum(np.logical_and(gt_test == 1, gt == 1)) if dim == 1 else np.sum(np.logical_and(gt_test[a] == 1, gt == 1))

        # True Negative (TN): pixels correctly detected as background
        TN = np.sum(np.logical_and(gt_test == 0, gt == 0)) if dim == 1 else np.sum(np.logical_and(gt_test[a] == 0, gt == 0))

        # False Positive (FP): pixels falsely segmented as foreground
        FP = np.sum(np.logical_and(gt_test == 1, gt == 0)) if dim == 1 else np.sum(np.logical_and(gt_test[a] == 1, gt == 0))

        # False Negative (FN): pixels falsely detected as background
        FN = np.sum(np.logical_and(gt_test == 0, gt == 1)) if dim == 1 else np.sum(np.logical_and(gt_test[a] == 0, gt == 1))

        TP_list.append(TP)
        FP_list.append(FP)
        TN_list.append(TN)
        FN_list.append(FN)

        sys.stdout.write("\r>  Computing ... {:.2f}%".format(a * dim / 100))
        sys.stdout.flush()

    print("\n\nSummary: TP, FP, TN, FN")
    print("------------------------------------------------------------")
    if array_params is None:
        print("TP: {}\tFP: {}\tTN: {}\tFN: {}".format(TP_list[0], FP_list[0], TN_list[0], FN_list[0]))
    else:
        for id, param in enumerate(array_params):
            print("For param = {} - TP: {}\tFP: {}\tTN: {}\tFN: {}".format(param, TP_list[id], FP_list[id], TN_list[id], FN_list[id]))
    print("------------------------------------------------------------")

    return TP_list, FP_list, TN_list, FN_list