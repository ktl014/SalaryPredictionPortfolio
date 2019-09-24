"""Visualization helpers"""

# Standard dist imports
import logging

# Third party imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def plot_target(df, target_col):
    """Visualize target variable

    Args:
        df (pd.DataFrame): dataset
        target_col (str): string of target variable

    Returns:
        None

    """
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(df[target_col])
    plt.subplot(1, 2, 2)
    sns.distplot(df[target_col], bins=20)
    plt.show()

    print('\n{0:*^80}'.format(' Reviewing target variable ' + target_col))
    print(df[target_col].describe())


def plot_feature(df, col, target_col):
    '''
    Make plot for each features
    left, the distribution of samples on the feature
    right, the dependance of salary on the feature
    '''
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    if df[col].dtype == 'int64':
        df[col].value_counts().sort_index().plot()
    else:
        # change the categorical variable to category type and order their level by the mean salary
        # in each category
        mean = df.groupby(col)[target_col].mean()
        df[col] = df[col].astype('category')
        levels = mean.sort_values().index.tolist()
        df[col].cat.reorder_categories(levels, inplace=True)
        df[col].value_counts().plot()
    plt.xticks(rotation=45)
    plt.xlabel(col)
    plt.ylabel('Counts')
    plt.subplot(1, 2, 2)

    if df[col].dtype == 'int64' or col == 'companyId':
        # plot the mean salary for each category and fill between the (mean - std, mean + std)
        mean = df.groupby(col)[target_col].mean()
        std = df.groupby(col)[target_col].std()
        mean.plot()
        plt.fill_between(range(len(std.index)), mean.values - std.values, mean.values + std.values, \
                         alpha=0.1)
    else:
        sns.boxplot(x=col, y=target_col, data=df)

    plt.xticks(rotation=45)
    plt.ylabel(target_col.upper())
    plt.show()
