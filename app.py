
from flask import Flask, request, jsonify
from database import get_connection
app = Flask(__name__)

@app.route('/')
def home():
    return "Bus Booking API is Running!"

@app.route('/api/book', methods=['POST'])
def book_ticket():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO bookings (passenger_name, source, destination, seats, travel_date) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (data['name'], data['source'], data['destination'], data['seats'], data['travel_date']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Ticket Booked"}), 201

if __name__ == '__main__':
    app.run(debug=True
