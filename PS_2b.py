import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

current_palette = sns.color_palette("Set2", 10)
sns.set_palette(current_palette)

bY = pd.read_csv("udacity_students.csv")
bY.head()

total = bY['Frequency'].sum() # total number of students
print("The total number of students is %d." % total)

bY['Percentage'] = round((bY['Frequency']/total)*100, 3) # add the Percentage column
bY.head()

# born before 1975
print("The number of students born before 1975 \
is somewhere between %g percent and %g percent." % (round(bY.iloc[0:6, 2].sum(), 2), bY.iloc[0:7, 2].sum()))

# visualize data
ax = sns.barplot(x = 'Birth year', y = 'Frequency', data = bY)
ax.set_xticklabels(labels = bY['Birth year'], rotation = 50)

# add labels on top of each bar
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width()/2., height, '{}'.format(int(height)), ha = 'center')

plt.show()
