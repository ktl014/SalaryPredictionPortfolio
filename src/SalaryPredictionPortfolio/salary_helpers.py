"""Helpers"""
# Standard dist imports
import os
import logging

# Third party imports
import pandas as pd

# Project level imports
from SalaryPredictionPortfolio.utils.config import opt
from SalaryPredictionPortfolio.utils.genericconstants import GenericConstants as GConst
from SalaryPredictionPortfolio.utils.genericconstants import SalaryConstants as SConst

# Module level constants

def read_in_dataset(dset, raw=False, verbose=False):
    """ Read in one of the Salary datasets

    Args:
        dset (str): basename of the dataset (e.g. test_features.csv, train_features.csv)
        raw (bool): Flag for raw or processed data. Default is raw
        verbose (bool): Print out verbosity

    Returns:
        pd.DataFrame: dataset
    """
    data_type = GConst.RAW_DATA if raw else GConst.PROCESSED_DATA
    df = pd.read_csv(os.path.join(opt.data_dir, data_type, dset))
    #Todo change this to logging
    if verbose:
        verbose_print_ds(df, dset)
    return df

def merge_dataset(train, salaries):
    """Merge the train and salaries datasets.

    Both need to have a common key `jobId`

    Args:
        train (pd.DataFrame):
        salaries (pd.DataFrame):

    Returns:
        Merged dataset
    """
    train_data_merged = train.merge(salaries, how='left', on=SConst.job_id)
    return train_data_merged

def verbose_print_ds(df, dset):
    print('\n{0:*^80}'.format(' Reading in the {0} dataset '.format(dset)))
    print("\nit has {0} rows and {1} columns".format(*df.shape))
    print('\n{0:*^80}\n'.format(' It has the following columns '))
    print(df.info())
    print('\n{0:*^80}\n'.format(' The first 5 rows look like this '))
    print(df.head())
