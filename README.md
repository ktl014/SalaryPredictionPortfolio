# SalaryPredictionPortfolio
Salary Prediction Project (Python)

## Our task
The specific task here is to identify a harmful algae species at the species taxonomy level, i.e. given an image, return the predicted species classification.

### Getting Started

The approach here is to add a classifier on top of the pre-trained CNN model and fine tune the model parameters by training on our domain specific data, i.e., phytoplankton images.
This is done in <code>main.py</code>.

#### System Requirement
1. Python 3.5 or higher
3. Python libraries: pandas, scikit-learn, scikit-image, matplotlib, numpy, lxml
4. Example: Create a python environment named `hab_env` and install required libraries using `pip`:
    - `virtualenv salary_env`
    - `source salary_env/bin/activate`
    - `pip install --user -r requirements.txt`

It is recommended to run the program on GPU with 12 GB memory. Training (fine tuning) the model on a GPU, with ~10k images in training data, takes ~1 hour for 5 or 6 epochs depending on the hyperparameters used.
The scoring can be done on CPU, but running on GPU is ~10-30x faster than on CPU

#### Download required files:
1. Copy the files and directories in this repo into your work directory.
2. Download the pre-trained ResNet models into the `model` directory of your work directory. 
    - Run `python download_pretrained.py` from the `model` directory.