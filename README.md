![house](./assets/house.jpg)
# Price_prediction
This project @ BeCode.org as part of the AI Bootcamp in Gent.

# Description:
* This project is based on collecting data from 10,000 houses.
* Clean and Analyse the data.
* Based on the data predict price value of new house 

# Installation:
[![pandas](https://img.shields.io/badge/pandas-1.3.5-red)](https://pandas.pydata.org/pandas-docs/version/1.3/getting_started/install.html)
[![numpy](https://img.shields.io/badge/numpy-1.21.6-orange)](https://pypi.org/project/numpy/1.21.6/)
[![scikit](https://img.shields.io/badge/scikit_learn-1.0.2-yellow)](https://pypi.org/project/scikit-learn/1.0.2/)
[![xgboost](https://img.shields.io/badge/xgboost-1.6.2-green)](https://xgboost.readthedocs.io/en/stable/install.html)
[![seaborn](https://img.shields.io/badge/seaborn-0.12.1-blue)](https://seaborn.pydata.org/installing.html)
[![matplotlib](https://img.shields.io/badge/matplotlib-3.5.3-indigo)](https://seaborn.pydata.org/installing.html)
[![fastapi](https://img.shields.io/badge/fastapi-0.100.0-purple)](https://pypi.org/project/fastapi/)
[![pydantic](https://img.shields.io/badge/fastapi-2.0.3-orange)](https://pypi.org/project/pydantic/)
[![uvicorn](https://img.shields.io/badge/uvicorn-0.22.0-yellow)](https://pypi.org/project/uvicorn/)
[![pickleshare]((https://img.shields.io/badge/pickleshare-0.7.5-green))](https://pypi.org/project/pickleshare/)

* clone this repository
* use `pip install <module name>` to install the required models.

# Usage
* open the terminal and redirect to where your repository is.
* run the server with `uvicorn app:app --reload`. whereas `app:` is the name of `.py` file and `:app` is the name of initialisation of `FastAPI`.
* now open `127.0.0.1:8000` to see welcome page and `127.0.0.1:8000/docs` to go to prediction page.
* follow the instructions in schema to enter the details to get the prediction.

# Docker deployment

I was able to create docker image of size 1.82GB and run docker container to get the same result as my local machine. attaching dockerfile to the repository.

# Completion:
* Name - Mythili Palanisamy
* Repository - Price_prediction
* Submission - 28/07/2023 4:00 PM
