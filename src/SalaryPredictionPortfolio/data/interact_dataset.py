"""Interact with the dataset"""
# Standard dist imports
import logging

# Third party imports

# Project level imports
from SalaryPredictionPortfolio.salary_helpers import read_in_dataset
from SalaryPredictionPortfolio.utils.config import opt
from SalaryPredictionPortfolio.utils.genericconstants import SalaryConstants as Const

# Module level constants

def main():
    logger = logging.getLogger(__name__)
    logger.info('\n{0:*^80}'.format(' Interact with dataset '))

    train_df = read_in_dataset(dset='train_features.csv', raw=True, verbose=True)

    logger.info('\n{0:*^80}'.format(' Reviewing jobId '))
    duplicate_flag = train_df[Const.job_id].nunique() == len(train_df)
    logger.info('are there no duplicate jobIds: {}'.format(duplicate_flag))

    logger.info('\n{0:*^80}'.format(' Reviewing companyId '))
    logger.info('{} unique companies'.format(train_df[Const.company_id].nunique()))
    logger.info(train_df[Const.company_id].value_counts())

    jobs_per_company = 0
    logger.info('How many jobs per companies? {}')



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    main()
