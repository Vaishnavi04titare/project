import pickle
from flask import Flask, render_template,request,url_for
import numpy as np

app = Flask(__name__, template_folder='template')  # still relative to module
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    print(int_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='stress is {}'.format(output))
if __name__ == '__main__':
    app.run(debug=True)