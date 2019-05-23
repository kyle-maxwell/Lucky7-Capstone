#!/usr/bin/env python3
import json
import os
from werkzeug import secure_filename
from flask import Flask, render_template, request
import pandas as pd
from ML.KMeans import data_classifier

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/test")
def test():
	return json.dumps("TEST")

@app.route('/api/upload', methods = ['POST'])
def upload_file():
	files = request.files.to_dict()

	ontology = check_for_ontology(files)
	if ontology:
		return ontology 


	if (len(list(files.keys())) == 0) :
		return json.dumps({'error' : "Please select a file to analyze before uploading."})
  
	try:
		files = list(files.values())
		seq = [pd.read_csv(file) for file in files]
		df = pd.concat(seq, axis=0)
		#df = pd.read_csv(file)
	except Exception as e:
		return json.dumps({'error' : "Unable to open CSV. Are you sure it's a CSV?"})

	try:
		resp = data_classifier(df)
		print(resp)
		return json.dumps(resp)
	except Exception as e:
		print(e)
		return json.dumps({'error' : "Unable to analyze CSV."})	

def check_for_ontology(files):
	for file in files.keys():
		if '.json' in file:
			data = files[file].read().decode('UTF-8')
			data = json.loads(data)
			print(data)
			return json.dumps(data)
	

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000), debug=True)
