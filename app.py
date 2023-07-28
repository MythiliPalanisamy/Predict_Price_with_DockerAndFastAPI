from fastapi import FastAPI,Request, status
from pydantic import BaseModel, Field
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from typing import Optional
from src.prediction import *
from src.preprocessing import *
import json

app = FastAPI()

# possible input for user reference (for schema)

Property = ['apartment', 'bungalow', 'castle', 'chalet', 'country-cottage','duplex', 'exceptional-property', 'farmhouse', 'flat-studio','ground-floor', 'house', 'kot', 'loft', 'manor-house', 'mansion','mixed-use-building', 'other-property', 'penthouse','service-flat', 'town-house', 'triplex', 'villa']
EnergyClass = ['A', 'A+', 'A++', 'B', 'C',  'D', 'E', 'F', 'G']
KitchenType = ['Hyper equipped', 'Installed', 'Not installed','Semi equipped', 'USA hyper equipped', 'USA installed','USA semi equipped', 'USA uninstalled']
HeatingType = ['Carbon', 'Electric', 'Fuel oil', 'Gas', 'Pellet', 'Solar','Wood']
province = ['Antwerp', 'Brussels Capital Region', 'East Flanders','Flemish Brabant', 'Hainaut (West)', 'Limburg', 'Liège','Luxembourg (shared with Eastern Hainaut)', 'Namur','Walloon Brabant', 'West Flanders']
BuildingCondition = ['As new', 'Good', 'Just renovated', 'To be done up','To renovate', 'To restore']



class Data(BaseModel):
        type_of_property: Optional[str] = Field(None, description = f"can be one of the items in following list \n {Property}")
        postal_code : Optional[int] = Field(None, description = "should be Belgium postal code")
        energy_class : Optional[str] = Field(None, description = f"can be one of the items in following list \n {EnergyClass} ")
        bedrooms : Optional[int] = Field(None, description = "Enter number of bedrooms in the house")
        bathrooms : Optional[int] = Field(None, description = "Enter number of bathrooms in the house")
        toilets : Optional[int] = Field(None, description = "Enter number of toilets in the house")
        number_of_frontages : Optional[int] = Field(None, description = "Enter number of frontages in the house")
        kitchen_type : Optional[str] = Field(None, description = f"can be one of the items in following list \n {KitchenType}")
        heating_type : Optional[str] = Field(None, description = f"can be one of the items in following list \n {HeatingType}")
        surface_of_the_plot : Optional[int] = Field(None, description = "Enter surface of the plot")
        living_room_surface : Optional[int] = Field(None, description = "Enter living room surface of the plot")
        province : Optional[str] = Field(None, description = f"can be one of the items in following list \n {province}")
        building_condition : Optional[str] = Field(None, description = f"can be one of the items in following list \n {BuildingCondition}")

@app.get('/')
def index():
    return {'''Enter the following details to predict the value of house:    1) Type of property    2) postal code    3) Bedrooms    4) Energy class    5) Surface of the plot    6) Living room surface    7) Number of frontages    8) Building condition     9) Bathrooms     10) Toilets    11) Kitchen type    12) Heating type    13) province '''}

#handling errors
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):

    if exc.errors()[0]['type']=='string_type':

        error_location = exc.errors()[0]['loc']
        error_msg = exc.errors()[0]['msg']
        input_value = exc.errors()[0]['input']
        error_message = f" Error Message: {error_msg} instead got input as {input_value} at {error_location}"

        return PlainTextResponse(content=error_message, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    else:
         
         error_message = "Input should be valid number instead got string" 
      
         return PlainTextResponse(content=error_message, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

# preprocessing and prediction.py
@app.post('/predict')
def predict(property : Data):

    property = json.loads(property.json())
    df = pd.DataFrame(property, index=[0])
    
    processed = preprocess(df)
    price = predict_forest_price(processed)

    return {'predicted_price ' : price[0]}



    
    

