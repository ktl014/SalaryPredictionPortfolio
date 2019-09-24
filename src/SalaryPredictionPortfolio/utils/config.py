""" """
from __future__ import absolute_import

# Standard dist imports
from pprint import pprint
import os
from pathlib import Path

# Third party imports

# Project level imports
from SalaryPredictionPortfolio.utils.genericconstants import GenericConstants as Const

# Module level constants
DEFAULT_ENV = Const.DEV_ENV
PROJECT_DIR = Path(__file__).resolve().parents[3]

class Environment():
    def __init__(self, env_type=None):
        if env_type == Const.DEV_ENV:
            self.models_dir = os.path.join(PROJECT_DIR, 'src/models')
            self.data_dir = os.path.join(PROJECT_DIR, 'src/data')
        elif env_type == Const.PROD_ENV:
            self.models_dir = 'prod/models'
            self.data_dir = 'prod/data'

class Config(Environment):
    """Default Configs for training and inference

    After initializing instance of Config, user can import configurations as a
    state dictionary into other files. User can also add additional
    configuration items by initializing them below.
    Example for importing and using `opt`:
    config.py
        >> opt = Config()
    main.py
        >> from config import opt
        >> lr = opt.lr
    NOTE that, config items could be overwriten by passing
    argument `set_config()`. e.g. --voc-data-dir='./data/'
    """
    # Training flags
    log2file = False
    print_freq = 50
    save_freq = 2

    def __init__(self, env_type):
        super().__init__(env_type)

    def _parse(self, kwargs):
        state_dict = self._state_dict()
        for k, v in kwargs.items():
            if k not in state_dict:
                raise ValueError('UnKnown Option: "--%s"' % k)
            setattr(self, k, v)

        # print('======user config========')
        # pprint(self._state_dict())
        # print('==========end============')

    def _state_dict(self):
        """Return current configuration state
        Allows user to view current state of the configurations
        Example:
        >>  from config import opt
        >> print(opt._state_dict())
        """
        return {k: getattr(self, k) for k, _ in Config.__dict__.items() \
                if not k.startswith('_')}

def set_config(**kwargs):
    """ Set configuration to train/test model
    Able to set configurations dynamically without changing fixed value
    within Config initialization. Keyword arguments in here will overwrite
    preset configurations under `Config()`.
    Example:
    Below is an example for changing the print frequency of the loss and
    accuracy logs.
    >> opt = set_config(print_freq=50) # Default print_freq=10
    >> ...
    >> model, meter = train(trainer=music_trainer, data_loader=data_loader,
                            print_freq=opt.print_freq) # PASSED HERE
    """
    opt._parse(kwargs)
    return opt

opt = Config(DEFAULT_ENV)