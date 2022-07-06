#PROGRAM ON PEARSON CORRELATION distribution
import pandas as pd
from scipy.stats import pearsonr

# Import your data into Python
df = pd.read_csv("Auto.csv")

# Convert dataframe into series
list1 = df['weight']
list2 = df['mpg']

# Apply the pearsonr()
corr, _ = pearsonr(list1, list2)
print('Pearsons correlation: %.3f' % corr)