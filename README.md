# Thesis
File structure for the thesis is as follows:

    Thesis
    ├── dataset                     # Data set that are required for the experiments
    ├── GroupHotel                  # Grouop hotel forecast
    ├── SingleHotel                 # Single hotel occupancy forecast 
    ├── .gitignore                  # git config to ignore files
    ├── DataPreprocessing.ipynb     # Preprocessing code in jupyter
    ├── README.md                   
    └── requirements.txt

## How to run
Latest code for thesis can be found on repository: https://github.com/ahmadabdullah247/thesis.git
Data files can be requested via email.

1. Clone repository
```bash
https://github.com/ahmadabdullah247/thesis.git
cd 'thesis'
```
2. (Optional) For ease of reproducibility I like to keep my project libraries seperate. Feel free to omit this if you like. 
```bash
python -m virtualenv .venv
source .venv/bin/activate
```
3. This will install all the libraries you need to run the server.
```bash
pip install -r requirements.txt
```
