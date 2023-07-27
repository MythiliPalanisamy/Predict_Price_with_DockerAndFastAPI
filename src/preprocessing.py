import numpy as np
import pandas as pd
import pickle
from src.prediction import *


def preprocess(raw_dataframe):
    
    # initialising catagorical columns which can be used later for one hot encoding
    column=[ 'type_of_property', 'building_condition', 'kitchen_type',  'province','energy_class', 'heating_type',] # catagorical
    
    # loading saved one hot encoding trained data
    ohe = pickle.load(open(r'C:\Users\Karthick Palanivel\Documents\GitHub\Price_prediction\models\ohe.pickle', 'rb'))
    
    # converting test data
    one_hot_encoded_array = ohe.transform(raw_dataframe[column]).toarray()

    # 'ohe.categories_' gives list of category in each column as separate array. 
    # concatenating it as single array
    categories = np.concatenate(ohe.categories_)

    # creating new dataframe with one hot encoded array with respective categories
    encoded_dataframe = pd.DataFrame(one_hot_encoded_array, columns=categories)

    # droping encoded columns from original dataframe
    raw_dataframe = raw_dataframe.drop(columns=[ 'type_of_property', 'building_condition', 'kitchen_type',  'province','energy_class', 'heating_type','postal_code'])

    # changing entire dataset into integer
    raw_dataframe = raw_dataframe.astype(int)

    # concatenating encoded dataframe and original dataframe
    final = pd.concat([raw_dataframe,encoded_dataframe], axis=1)
 
    # loading saved minmax scaler
    minmax_scaler = pickle.load(open(r'C:\Users\Karthick Palanivel\Documents\GitHub\Price_prediction\models\minmax_scaler.pickle', 'rb'))

    final[['surface_of_the_plot', 'living_room_surface']] = minmax_scaler.transform(final[[ 'surface_of_the_plot', 'living_room_surface']])

    processed=final.drop(columns=['G_F','NS','C_B','0'])

    return processed
