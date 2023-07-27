from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Union
from enum import Enum
from src.prediction import *
from src.preprocessing import *
import json


app = FastAPI()

"""class BuildingConditionEnum(str, Enum):
    GOOD = 'good'
    TO_RENOVATE = 'to renovate'"""

class Data(BaseModel):
        type_of_property : Optional[str] = None
        postal_code : Optional[int] = None
        energy_class : Optional[str] = None
        bedrooms : Optional[int] = None
        bathrooms : Optional[int] = None
        toilets : Optional[int] = None
        number_of_frontages : Optional[int] = None
        kitchen_type : Optional[str] = None
        heating_type : Optional[str] = None
        surface_of_the_plot : Optional[int] = None
        living_room_surface : Optional[int] = None
        province : Optional[str] = None
        building_condition : Optional[str] = None

@app.get('/')
def index():
    return {'''Enter the following details to predict the value of house:    1) Type of property    2) postal code    3) Bedrooms    4) Energy class    5) Surface of the plot    6) Living room surface    7) Number of frontages    8) Building condition     9) Bathrooms     10) Toilets    11) Kitchen type    12) Heating type    13) province '''}


# preprocessing and prediction.py
@app.post('/predict')
def predict(property : Data):
  
    property = json.loads(property.json())
    df = pd.DataFrame(property, index=[0])
    print(df)
    processed = preprocess(df)
    price = predict_price(processed)

    return {'predicted_price ' : price[0]}

    
    

