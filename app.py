#import libraries
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle


#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))



#xgb_model = joblib.load('xgb')
#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    features = ['h_type', 'area', 'bath', 'pool']
    pred = pd.DataFrame(int_features)
    pred = pred.transpose()
    pred.columns = features
    prediction = model.predict(pred)
    prediction = np.exp(prediction)
    output = round(prediction[0])

    return render_template('index.html', prediction_text='Property rent price is: RM{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)