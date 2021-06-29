from pipeline import InferencePipeline

test_review = "this is a pretty awesome book"

pipeline = InferencePipeline()
prediction = pipeline.predict(test_review)

print("{} -> {}".format(test_review, prediction))


# importing the required libraries
from flask import Flask, render_template, request, redirect, url_for
from joblib import load

# load the pipeline object
pipeline = InferencePipeline()

# function to get results for a particular text query
def requestResults(name):
	# get the prediction
	prediction = pipeline.predict(name)
	return str(prediction)


# start flask
# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

# render default webpage
@app.route('/')
def home():
    return render_template('home.html')

# when the post method detect, then redirect to success function
@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))

# get the data for the requested query
@app.route('/success/<name>')
def success(name):
	returned_prediction = requestResults(name)
	if (returned_prediction == 'positive'):
		return render_template('home.html')
	else:
		return render_template('sadhome.html')
    # return "<xmp>" + str(requestResults(name)) + " </xmp> "

# app.run(host='192.168.0.177', debug=True)
app.run(debug=True)