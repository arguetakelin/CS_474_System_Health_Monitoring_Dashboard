
#import the necessary packages
from flask import Flask, render_template, jsonify
import mysql.connector # type: ignore #For database
#import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
#from gevent.pywsgi import WSGIServer

#To initialize Flask app
app = Flask(__name__) 

#MySQL connection
db_config = {
    'host': ' localhost', 
    'user': 'root ',
    'password': 'Honduras504',
    'database': 'System_monitoring'
}


def get_db_connection():
    return mysql.connector.connect(**db_config)

#function to get system metrics data from the database
def fetch_metrics():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True) # dictionary=True will get the column names 
        cursor.execute("SELECT * FROM System_metrics") #Here it will execute SQL query to get all the records from the table
        data = cursor.fetchall()
        cursor.close() #close connetion
        conn.close()   
        return data

#route to render the main dashboard page
@app.route('/')
def index():
    metrics_data = fetch_metrics() #retrieve metrics data from the database
    return render_template('index.html', metrics=metrics_data)

#API endpoint to return metrics data as json for JavaScript to use in charts
@app.route('/data')
def data():
    #fetch metrics data from the database
    metrics_data = fetch_metrics()
    return jsonify(metrics_data)

if __name__=='__main__':
    app.run(debug=True)

    
