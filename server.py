from flask import Flask, request, jsonify, render_template  # Add render_template to your imports
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # Serve the HTML page

@app.route('/times', methods=['GET'])
def get_times():
    food_type = request.args.get('food_type', '').lower()  # Convert input to lowercase
    conn = sqlite3.connect('sous_vide.db')
    c = conn.cursor()
    # Use LOWER() function in SQL to make the comparison case-insensitive
    c.execute("SELECT temperature, cooking_time FROM SousVideTimes WHERE LOWER(food_type) = ?", (food_type,))
    times = c.fetchall()
    conn.close()
    

    
    # Check if any cooking times were found
    if times:
        # Convert the list of times to a list of dictionaries for a more user-friendly JSON response
        times = [{'temperature': temperature, 'cooking_time': cooking_time} for temperature, cooking_time in times]
    else:
        # If no cooking times were found, return a message indicating this
        times = {'message': f'No cooking times found for {food_type}'}
        
    return jsonify(times)

if __name__ == '__main__':
    app.run(debug=True)
