#import necessary modules, Flask creates the web app, request handles incoming requests, jsonify for returning json responses
#render_templete for serving html files and sqlite imports the sqlite3 library for the database
from flask import Flask, request, jsonify, render_template
import sqlite3

#Initializes the Flask app.
app = Flask(__name__)

#Defines the home route ('/'). This route responds to GET requests
@app.route('/', methods=['GET'])
#The function that's called when the home route is accessed
def home():
    #This line serves the index.html file when the home route is accessed
    return render_template('index.html')  # Serve the HTML page

#Defines a route for fetching cooking times
@app.route('/times', methods=['GET'])
#Defines the function to execute when this route is accessed
def get_times():
    #Retrieves the food_type query parameter from the URL and converts it to lowercase
    food_type = request.args.get('food_type', '').lower()
    #Connects to the SQLite database
    conn = sqlite3.connect('sous_vide.db')
    #Creates a cursor object to execute SQL queries
    c = conn.cursor()
    #Executes an SQL query to fetch cooking times for the given food type
    c.execute("SELECT food_type, temperature, cooking_time FROM SousVideTimes WHERE LOWER(food_type) = ?", (food_type,))
    #Retrieves all rows from the query result
    times = c.fetchall()
    conn.close()
    

    
    # Check if any cooking times were found
    if times:
        times = [{'food_type': row[0], 'temperature': row[1], 'cooking_time': row[2]} for row in times]
    else:
        times = {'message': f'No cooking times found for {food_type}'}
        
    return jsonify(times)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

