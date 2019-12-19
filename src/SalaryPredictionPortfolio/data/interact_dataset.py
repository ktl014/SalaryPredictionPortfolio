"""Interact with the dataset"""
# Standard dist imports

# Third party imports
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from IPython.display import display


# Project level imports

# Module level constants

def detect_duplicates(data, column=None):
    """Detect duplicate values within dataframe"""
    if data.duplicated().sum() == 0:
        print("Duplicates detected!")

        if column:
            duplicated_rows_data = data[data.duplicated(column, keep='last')]
        else:
            # Select duplicate rows except last occurrence based on all columns
            duplicated_rows_data = data[data.duplicated(keep='last')]

        print("Duplicate Rows except last occurrence are :")
        display(duplicated_rows_data)
    else:
        print('No duplicates detected')


def detect_nan_values(data):
    """Detect nan values within dataframe"""
    nan_columns = data.columns[data.isna().any()].tolist()
    if nan_columns:
        print(f'NaN columns: {nan_columns}')
        return data.loc[:, data.isna().any()]
    else:
        print('No NaN values detected')


def clean_nan_values(data):
    """Clean null values in coordinates"""
    print('\t cleaning nan values...')
    print("\t\tOld size: {}".format(data.shape))
    nan_columns = data.columns[data.isna().any()].tolist()
    for i in nan_columns:
        data[i] = data[i].replace(0, np.nan)
        data = data[data[i].notnull()]
    print("\t\tNew size: {}".format(data.shape))
    return data


def detect_outlier(data, col, verbose=False, visualize=False):
    """Detect outliers

    Example:
        outliers = detect_outlier(train_df['salary'], verbose=True, visualize=True)
        train_df = train_df.drop(outliers[:,0]).reset_index(drop=True)
        plot_target(train_df, target_col='salary')

    :param data:
    :return:
    """

    stat = data[col].describe()
    print('Original Data Distribution\n{}'.format('-' * 30))
    print(stat)
    iqr = stat['75%'] - stat['25%']
    upper = stat['75%'] + 1.5 * iqr
    lower = stat['25%'] - 1.5 * iqr
    print(f'\nThe upper and lower bounds for suspected outliers are {upper} and {lower}')

    if visualize:
        plt.figure(figsize=(14, 6))
        plt.subplot(1, 3, 1)
        sns.distplot(data[col])
        plt.xlim(right=lower)
        plt.subplot(1, 3, 2)
        sns.distplot(data[col])
        plt.subplot(1, 3, 3)
        sns.distplot(data[col])
        plt.xlim(left=upper)
        plt.show()

    if verbose:
        print('\nData under lower bound\n{}'.format('-' * 40))
        # check potential outlier below lower bound
        display(data[data[col] < lower])
        print(data[col][data[col] < lower].describe())

        print('\nData above upper bound\n{}'.format('-' * 40))
        # check potential outlier above upper bound
        display(data[data[col] > upper])
        print(data[col][data[col] > upper].describe())
        # Check most suspicious potential outliers above upper bound
        # display(df[(df[col] > 222.5) & (df[col] == 'JUNIOR')])

    return lower, upper
