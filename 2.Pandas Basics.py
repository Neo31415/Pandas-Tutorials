#Link: https://pythonprogramming.net/basics-data-analysis-python-pandas-tutorial/

import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import style

# One of the graph style
style.use('fivethirtyeight')

# Data prior to being loaded into a Pandas Dataframe can take multiple forms, but generally it needs to be a dataset that can form to rows and columns. 
# So maybe a dictionary like this:
web_stats = {'Day':[1,2,3,4,5,6,7,8,9], 
             'Visitors':[43,34,65,56,29,76,56,77,26],
             'Bounce Rate':[65,67,78,65,45,52,45,76,83]}

# We can turn this dictionary to a dataframe by doing the following:
stats = pd.DataFrame(web_stats)

# You can call for a quick initial snippit by doing this, by default it gives 1st 5 rows 
print(stats.head())
print(stats.tail()) # Same as above but from below

# We can also put no. to get specific ammount of rows
print(stats.tail(2))

# We can set any column as an index in pandas dataframe (by default, pandas gives rows indexing by it self )
print(stats.set_index('Day'))

# To save it as our primary data frame....
# we can do either
stats = stats.set_index('Day')
# or  
stats.set_index('Day', inplace=True)

# We can reference specific items in a dataframe like this:
print(stats['Visitors'])
# or like this, like an object (but make sure there is no space b/w name)
print(stats.Visitors)

# we can plot a single column like this:
stats['Visitors'].plot()
plt.show()

#We can also plot the entire dataframe. So long as the data is normalized or on the same scale
stats.plot()
plt.show()

# we leave, you can also reference multiple columns at a time
print(stats[['Visitors','Bounce Rate']])

# Converting a column to a list
print(stats.Visitors.tolist())

# To convert entire data frame to multidimenshional list
import numpy as np
print(np.array(stats))