import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns
import mpl_toolkits


f = pd.read_csv('./all/train.csv')

# f.hist(bins=50, figsize=(20,15))
# plt.savefig("attribute_histogram_plots")
#     #plt.show()
# corr_matrix = f.corr()
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(f.describe())
#     print(corr_matrix)

# attributes = ["crim", "indus", "nox", "rad",'tax']
# scatter_matrix(f[attributes], figsize=(12, 8))
# plt.savefig('matrix.png')

# print(f.head())
f['crim'].value_counts().plot(kind = 'bar')
plt.title('number of rooms')
plt.xlabel('Bedrooms')
plt.ylabel('Count')
sns.despine