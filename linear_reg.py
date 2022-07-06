#PROGRAM ON SIMPLE LINEAR REGRESSION MODEL
def slope_y_on_x(X, Y, n):
    sum_X = 0
    sum_Y = 0
    sum_XY = 0
    squareSum_X = 0
    squareSum_Y = 0
    c = 0
    i = 0
    while i < n:
        # sum of elements of array X.
        sum_X = sum_X + X[i]

        # sum of elements of array Y.
        sum_Y = sum_Y + Y[i]

        # sum of X[i] * Y[i].
        sum_XY = sum_XY + X[i] * Y[i]

        # sum of square of array elements.
        squareSum_X = squareSum_X + X[i] * X[i]
        squareSum_Y = squareSum_Y + Y[i] * Y[i]

        i = i + 1

    # use formula for calculating correlation
    # coefficient.
    byx = ((sum_XY * n) - (sum_X * sum_Y)) / ((squareSum_X * n) - (sum_X * sum_X))
    bar_X = sum_X / n
    bar_Y = sum_Y / n
    c = (bar_Y) - (byx * (bar_X))
    print("BAR X", bar_X)
    print("BAR Y", bar_Y)
    print(f"Line of regression : {byx} * x + {c}")

    return c


# Driver function
X = [15, 18, 21, 24, 27]
Y = [25, 25, 27, 31, 32]

# Find the size of array.
n = len(X)

# Function call to correlationCoefficient.

print('{0:.6f}'.format(slope_y_on_x(X, Y, n)))
