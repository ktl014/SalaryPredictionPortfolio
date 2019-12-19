"""Visualization helpers"""

# Standard dist imports

# Third party imports
import matplotlib.pyplot as plt
import seaborn as sns


def plot_target(data, target_col):
    """Visualize target variable

    Args:
        data (pd.DataFrame): dataset
        target_col (str): string of target variable

    Returns:
        None

    """
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(data[target_col])
    plt.subplot(1, 2, 2)
    sns.distplot(data[target_col], bins=20)
    plt.show()

    print('\n{0:*^80}'.format(' Reviewing target variable ' + target_col))
    print(data[target_col].describe())


def plot_feature(data, col, target_col, verbose=False):
    '''
    Make plot for each features
    left, the distribution of samples on the feature
    right, the dependance of salary on the feature
    '''
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    if data[col].dtype == 'int64':
        data[col].value_counts().sort_index().plot()
    else:
        # change the categorical variable to category type and order their level by the mean salary
        # in each category
        mean = data.groupby(col)[target_col].mean()
        data[col] = data[col].astype('category')
        levels = mean.sort_values().index.tolist()
        data[col].cat.reorder_categories(levels, inplace=True)
        data[col].value_counts().plot()
    plt.xticks(rotation=45)
    plt.xlabel(col)
    plt.ylabel('Counts')
    plt.subplot(1, 2, 2)

    if data[col].dtype == 'int64' or col == 'companyId':
        # plot the mean salary for each category and fill between the (mean - std, mean + std)
        mean = data.groupby(col)[target_col].mean()
        std = data.groupby(col)[target_col].std()
        mean.plot()
        plt.fill_between(range(len(std.index)),
                         mean.values - std.values, mean.values + std.values, alpha=0.1)
    else:
        sns.boxplot(x=col, y=target_col, data=data)

    plt.xticks(rotation=45)
    plt.ylabel(target_col.upper())
    plt.show()

    if verbose:
        print('\n{0:*^80}'.format(' Feature Distribution ({}) '.format(col)))
        print(data[col].value_counts())
        print('\nStatistial Descriptors\nn{}'.format('-' * 30))
        print(data[col].describe())
