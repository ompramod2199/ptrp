#PROGRAM ON RANK CORRELATION COEFFICENT
import pandas as pd
import scipy.stats
import math

x = [15, 18, 21, 15, 21]
y = [25, 25, 27, 27, 27]


def correlation_coefficent(x, y, n):
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    squaresum_x = 0
    squaresum_y = 0
    i = 0
    while i < n:
        sum_x = sum_x + x[i]

        sum_y = sum_y + y[i]

        sum_xy = sum_xy + x[i] * y[i]

        squaresum_x = squaresum_x + x[i] * x[i]

        squaresum_y = squaresum_y + y[i] * y[i]

        i = i + 1

    corr = (float)(n * sum_xy - sum_x * sum_y) / (float)(
        math.sqrt((n * squaresum_x - sum_x * sum_x) * (n * squaresum_y - sum_y * sum_y)))
    return corr


def spearmans_rank_correlation(x, y):
    xranks = pd.Series(x).rank()
    print("Rankings of X:")
    print(xranks)

    yranks = pd.Series(y).rank()
    print("Rankings of Y:")
    print(yranks)

    print("Spearman's Rank correlation:", scipy.stats.pearsonr(xranks, yranks)[0])


n = len(x)
spearmans_rank_correlation(x, y)
print("correlation", correlation_coefficent(x, y, n))