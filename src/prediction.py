import pickle

def predict(processed_data):

    print('---start predict.py----')
    forest = pickle.load(open(r'C:\Users\Karthick Palanivel\Documents\GitHub\Price_prediction\models\forest_pickle.pickle', 'rb'))
    predicted_price = forest.predict(processed_data)
    print(predicted_price)
    print('---end predict.py----')
    return predicted_price


