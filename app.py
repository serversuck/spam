# Importing essential libraries
from flask import Flask, render_template, request
import pickle
from sklearn.feature_extraction.text import CountVectorizer , TfidfTransformer 
count_vec = CountVectorizer(tokenizer=ptk)
tfidf = TfidfTransformer()


# Load the Multinomial Naive Bayes model and CountVectorizer object from disk
filename = 'spammodel.pkl'
model = pickle.load(open(filename, 'rb'))
count_vec = pickle.load(open('count_vec.pkl','rb'))
app = Flask(__name__)

def predicttt(x):
  xvec = count_vec.transform(x) 
  tfidf.fit(xvec) 
  Xtfidf = tfidf.fit_transform(xvec) 
  r = model.predict(Xtfidf)
  return r

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
    	message = request.form['message']
    	data = [message]
    	my_prediction = predicttt(data)
    	return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)
