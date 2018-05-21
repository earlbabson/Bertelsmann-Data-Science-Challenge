# Example code for Lesson 11 PS3a (BBC Memory Scores and NHL)

import pandas as pd
import numpy as np

def calculate_stats(csv):
    """The function takes in a .csv file and returns either mean scores
    (for the BBC dataset) or a dataframe containing measures of center
    (for the NHL dataset)
    """

    df = pd.read_csv(csv)

    col1 = df[df.columns[0]]
    col2 = df[df.columns[1]].dropna().astype(int) # remove NaNs and convert col2 to int

    # calculate the mean
    mean_col1 = np.round(np.mean(col1), 2)
    mean_col2 = np.round(np.mean(col2), 2)

    if csv == 'memory_scores.csv':
        print("The average recognition score is %g" % mean_col1)
        print("The average temporal memory score is %g" % mean_col2)

    else:
        # construct a pandas df
        stats = pd.DataFrame(np.array([['Detroit Red Wings', mean_col1, np.median(col1),
                                         np.bincount(col1).argmax()],
                                       ['San Jose Sharks', mean_col2, np.median(col2),
                                         np.bincount(col2).argmax()]]),
                                       columns = ['Team', 'Mean', 'Median', 'Mode'])


        return stats


team_data = calculate_stats('NHL.csv')
print(team_data)
