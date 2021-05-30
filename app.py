from flask import Flask, jsonify, request,render_template
import pickle
app = Flask(__name__)


@app.route('/SepalLengthCm/<float:SepalLengthCm>')
def home(SepalLengthCm):
    with open('./artifacts/lr.model.pickle', 'rb') as f:
            model = pickle.load(f)
    prediction=model.predict()
    print(prediction)
    return {'predicted petallength is:',prediction}


if __name__ =='__main__':
    app.run(debug=True, port="5001")
