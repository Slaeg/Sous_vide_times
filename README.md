# Sous Vide Cooking Time Web App

## Project Overview

This web application is a tool for finding optimal sous vide cooking times and temperatures for various food types. It was initially developed as a learning project to practice working with databases, web APIs, and frontend development. The project has since been successfully deployed in a real restaurant setting, demonstrating its practical utility in the food service industry.

## Features

- SQLite database containing sous vide cooking times and temperatures for different foods
- Flask backend providing an API for accessing the database
- Simple HTML/JavaScript frontend for user interaction
- Autocomplete functionality for food type search

## Tech Stack

- Backend: Python, Flask, SQLite
- Frontend: HTML, CSS, JavaScript (with jQuery and jQuery UI)
- Database: SQLite

## Project Structure

- `import_data.py`: Script to import data from CSV into SQLite database
- `server.py`: Flask server providing API endpoints
- `sous_vide.db`: SQLite database (generated from CSV data)
- `sous_vide.csv`: Source data for cooking times and temperatures
- `index.html`: Main HTML page for the web interface
- `script.js`: JavaScript file handling frontend logic
- `styles.css`: CSS file for styling the web interface

## Setup and Installation

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Install required Python packages:
   ```
   pip install flask
   ```
4. Run the `import_data.py` script to create and populate the database:
   ```
   python import_data.py
   ```
5. Start the Flask server:
   ```
   python server.py
   ```
6. Open a web browser and navigate to `http://localhost:5000` to use the application.

## Usage

### Web Interface
Navigate to `http://localhost:5000` in your web browser. Enter a food type into the form and press the 'Search' button to get the cooking time and temperature.

### API
To query the API directly, send a GET request to `/times` with the `food_type` query parameter:
```
http://localhost:5000/times?food_type=Apples
```

## Learning Objectives

Through this project, the aim was to:
- Understand how to design, create, and populate a SQLite database
- Gain experience with the Flask web framework and creating APIs
- Learn how to handle user input and display results in a web interface
- Practice frontend development with HTML, CSS, and JavaScript

## Real-World Application

This project moved beyond a learning exercise and was successfully deployed in a restaurant setting. It served as a practical tool for kitchen staff to quickly access sous vide cooking information, demonstrating how a personal learning project can solve real-world problems in the food service industry.

## Current Status

The project is currently in a stable, deployed state. While it continues to serve its purpose in its current form, active development and support have been discontinued. Users are welcome to fork and modify the project for their own needs.

## Contributing

While active development has ceased, the codebase remains available for educational purposes. Feel free to fork the project and adapt it to your needs.

## License

[Add your chosen license here]

