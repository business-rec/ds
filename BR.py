import numpy as np
from flask import Flask, abort, jsonify, request
import pickle

my_model = pickle.load(open('random_forest_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

app = Flask(__name__)


@app.route('/api', methods=['POST'])

def make_predict():
    # get data from post (4 features)
    data = request.get_json(force=True)
    # transforms
    predict_request = [data['review']]
    predict_request = vectorizer.fit_transform(predict_request)
    # preds
    y_hat = my_model.predict(predict_request)
    # send preds back
    output = {'y_hat': int(y_hat[0])}
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port=9000, debug=True)