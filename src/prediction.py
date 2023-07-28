import pickle

def predict_forest_price(processed_data):

    # loading forest module
    forest = pickle.load(open('./models/forest_pickle.pickle', 'rb'))
    predicted_price = forest.predict(processed_data)

    return predicted_price



