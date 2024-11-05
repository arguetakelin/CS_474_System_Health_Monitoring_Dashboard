
from flask import Flask, render_template, jsonify
import mysql.connector # type: ignore #For database
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import io 

#To initialize Flask app
app = Flask(__name__) 

#MySQL connection
db_config = {
    'host': ' ', 
    'user': ' ',
    'password': ' ',
    'database': 'System_monitoring'
}

#function to retrieve system metrics from the database
def fetch_metrics():

    try: 
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True) # dictionary=True will get the column names 
        cursor.execute("SELECT * FROM System_metrics") #Here it will execute SQL query to get all the records from the table
        data = cursor.fetchall()
        cursor.close() #close the connetion
        conn.close()   
        return data
    except mysql.connector.Error as err:
            print ("Error getting data:", err)
            return[] #return  an empty list if there is an error


@app.route('/')

def index():
    #Fetch data from the database to display on the webpage
    metrics_data = fetch_metrics()
    return render_template('index.html', metrics=metrics_data)

@app.route('/data')
def data():
    #fetch metrics data from the database
    metrics_data = fetch_metrics()
    return jsonify(metrics_data)

if __name__=='__main__':
    app.run(debug=True)

    




