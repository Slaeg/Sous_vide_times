from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # Serve the HTML page

@app.route('/times', methods=['GET'])
def get_times():
    food_type = request.args.get('food_type', '').lower()
    try:
        conn = sqlite3.connect('sous_vide.db')
        c = conn.cursor()
        c.execute("SELECT food_type, temperature, cooking_time FROM SousVideTimes WHERE LOWER(food_type) = ?", (food_type,))
        times = c.fetchall()
        conn.close()
    except sqlite3.Error as e:
        return jsonify({'error': f"Database error: {e}"}), 500

    if times:
        times = [{'food_type': row[0], 'temperature': row[1], 'cooking_time': row[2]} for row in times]
    else:
        times = {'message': f'No cooking times found for {food_type}'}
    
    return jsonify(times)

@app.route('/food_types', methods=['GET'])
def get_food_types():
    query = request.args.get('query', '').lower()
    try:
        conn = sqlite3.connect('sous_vide.db')
        c = conn.cursor()
        c.execute("SELECT DISTINCT food_type FROM SousVideTimes WHERE food_type LIKE ?", ('%' + query + '%',))
        food_types = c.fetchall()
        conn.close()
    except sqlite3.Error as e:
        return jsonify({'error': f"Database error: {e}"}), 500

    food_types = [food_type[0] for food_type in food_types]
    return jsonify(food_types)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
