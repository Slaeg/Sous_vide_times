from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/times', methods=['GET'])
def get_times():
    food_type = request.args.get('food_type')
    conn = sqlite3.connect('sous_vide.db')
    c = conn.cursor()
    c.execute("SELECT temperature, cooking_time FROM SousVideTimes WHERE food_type=?", (food_type,))
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
