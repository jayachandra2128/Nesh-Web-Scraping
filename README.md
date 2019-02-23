# Nesh-Web-Scraping
This application is built using python and flask. The purpose of this project is to develop a smart system that can put all the important 
information like stocks, articles and recent updates about a company in one place. It can even serve you smarter by automatic text summarisation of articles and sentiment analysis of articles.  scrape_stocks.py is python file that is responsible for scraping all the important information over web from websites NASDAQ, Montley fool. main.py is a flask application that is retreiving all the scraped information in and displaying it to a user in beautiful way.

Insights that are included in this application are:
1) Last known Stock Price and Stock Price Trend.
2) What News Articles were published about the company from Montley fool. 
3) Analysis of Earnings Call Transcript - When did the call happen, Who all was on the call.
4) Financial Numbers like Market Cap, Net Cash Flow, Last Year’s Revenue, 1 year target, Share volume, Current yield, Todays high/low, Earnings per share(EPS).
5) Sentiment Analysis of articles.
6) Text summarization of articles.

## Project Title
Nesh - Smart Assistant for Oil and Gas

## Installing dependencies - Please install all required libraries before running

pip install gensim

pip install flask

pip install numpy

pip install pprintpp

pip install Flask-Bootstrap

pip install textblob

pip install vaderSentiment

## Running the application
1) Once after installing python version 3 and flask, download the folder nesh from above.
2) Open cmd and change current directory to nesh folder which contains main.py file.
3) Run python main.py in cmd and there runs the amazing app on your local host which is smarter in helping you out.

