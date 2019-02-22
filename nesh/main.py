from flask import Flask, render_template
from flask import request
import numpy as np
import flask
import numpy as np
import sys
import subprocess
import json
from pprint import pprint
from flask_bootstrap import Bootstrap
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
analyser = SentimentIntensityAnalyzer()

app = Flask(__name__, static_url_path='/static')




bootstrap = Bootstrap(app)
@app.route('/')
def home():
	return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():

	
    #grabbing a set of wine features from the request's body
	feature_array = request.form['feature_array']
	print(feature_array)
	#subprocess.call(['python', 'scrape_news.py',feature_array])
	#subprocess.call(['python', 'scrape_earnings.py',feature_array])
	subprocess.call(['python', 'scrape_stocks.py',feature_array])
	#feature_array=[feature_array]
	#with open('news.json') as f:
	#	news = json.load(f)
	#with open('earnings.json') as f:
	#	earnings = json.load(f)
	with open('summary.json') as f:
		summary = json.load(f)
	#pprint(data)
	articles=summary["articles"]
	links=summary["links"]
	date=summary["date"]
	participants=summary["participants"]
	companyName=summary["company_name"]
	quote=summary["quote"]
	trend=summary["trend"]
	stockData=summary["key_stock_data"]
	lastRevenue=summary["lastRevenue"]
	cashflow=summary["cashflow"]
	summaries=summary["summaries"]
	participants = [s for s in participants.split(",") if "-" in s]
	sentiment=[]
	for i in articles:
		score=(analyser.polarity_scores(i))
		if(score['compound']>0.1):
			sentiment.append("Positive sentiment")
		elif(score['compound']<-0.1):
			sentiment.append("Negative sentiment")
		else:
			sentiment.append("Neutral")
		
	
	return render_template('predict.html', articles=articles, links=links,stockData=stockData,companyName=companyName,date=date,participants=participants,
	quote=quote,trend=trend,lastRevenue=lastRevenue,cashflow=cashflow,sentiment=sentiment,summaries=summaries,text=feature_array)
	

if __name__ == '__main__':
    app.run(debug=True)