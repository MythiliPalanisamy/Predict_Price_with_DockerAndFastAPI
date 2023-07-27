from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Union
from enum import Enum
from src.prediction import *
from src.preprocessing import *

app = FastAPI()

"""class BuildingConditionEnum(str, Enum):
    GOOD = 'good'
    TO_RENOVATE = 'to renovate'"""

class data(BaseModel):
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

@app.get('/predict')
def prediction():
    return ('welcome to predict your dream house')

#preprocessing and prediction.py
@app.post('/predict')
def predict(property: data):
    print('--- first of app.py---')
    raw_data = {'type_of_property' : property.type_of_property, 'postal_code': property.postal_code,  'energy_class' : property.energy_class,'bedrooms' : property.bedrooms, 'bathrooms': property.bathrooms, 'toilets': property.toilets, 'number_of_frontages':property.number_of_frontages ,'kitchen_type': property.kitchen_type,
       'heating_type':property.heating_type, 'surface_of_the_plot':property.surface_of_the_plot,  'living_room_surface':property.living_room_surface, 'province':property.province , 'building_condition':property.building_condition}
    processed = preprocess(raw_data)
    print('----in app.py----')
    predicted_price = predict(processed)
    return predicted_price

