from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for the purpose of example
medicines = [
    {"name": "MedicineA", "dosage_per_kg": 0.5},
    {"name": "MedicineB", "dosage_per_kg": 1.0},
    # Add more medicines...
]

@app.route('/search', methods=['GET'])
def search_medicine():
    query = request.args.get('name')
    if query:
        # In a real-world application, you'd query your database here
        # This is just filtering the dummy data
        results = [medicine for medicine in medicines if query.lower() in medicine['name'].lower()]
        return jsonify(results)
    else:
        return jsonify({"message": "Please provide a medicine name"}), 400

if __name__ == '__main__':
    app.run(debug=True)  # Turn off debug when deploying
