import numpy as np
import pandas as pd
import pickle

def preprocess(raw_dataframe):
    
    """ For reference :
    'one_hot_encoded_array' = encoding given column's with one hot encoder.
    'ohe.categories_' = list of category in each column as separate array.
    'categories' = coverting list of (names of) arrays as single array
    'encoded_dataframe' = converting encoded array and names of array as single dataframe
    'final' = concatenating encoded dataframe and original dataframe
    """

    # catagorical columns
    column=[ 'type_of_property', 'building_condition', 'kitchen_type',  'province','energy_class', 'heating_type',]
    
    # loading one hot encoding trained data and minmax scaler
    ohe = pickle.load(open('./models/ohe.pickle', 'rb'))
    minmax_scaler = pickle.load(open('./models/minmax_scaler.pickle', 'rb'))

    # using onehot encoder
    one_hot_encoded_array = ohe.transform(raw_dataframe[column]).toarray()
    categories = np.concatenate(ohe.categories_)
    encoded_dataframe = pd.DataFrame(one_hot_encoded_array, columns=categories)

    # droping encoded columns from original dataframe
    raw_dataframe = raw_dataframe.drop(columns=[ 'type_of_property', 'building_condition', 'kitchen_type',  'province','energy_class', 'heating_type','postal_code'])
    raw_dataframe = raw_dataframe.astype(int) 
    final = pd.concat([raw_dataframe,encoded_dataframe], axis=1)
 
    # using minmax scaler
    final[['surface_of_the_plot', 'living_room_surface']] = minmax_scaler.transform(final[[ 'surface_of_the_plot', 'living_room_surface']])
    processed=final.drop(columns=['G_F','NS','C_B','0'])

    return processed
