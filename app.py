from flask import Flask, jsonify
from datetime import datetime, date

app = Flask(__name__)

# Define the events
events = {
    "New Years": (1, 1),
    "Valentine's Day": (2, 14),
    "St. Patrick's Day": (3, 17),
    "April Fool's Day": (4, 1),
    "Mother's Day": (5, 12),
    "End Of School": (6, 15),
    "4th of July": (7, 4),
    "Start Of School": (8, 31),
    "Rosh Hashanah": (9, 15),
    "Halloween": (10, 31),
    "Thanksgiving": (11, 23),
    "Christmas": (12, 25)
}

@app.route('/days_until_next_event', methods=['GET'])
def get_days_until_next_event():
    today = date.today()
    min_days_left = float('inf')
    closest_event = ""

    for event, (month, day) in events.items():
        event_date_this_year = date(today.year, month, day)

        # If today's date is after the event, calculate for next year's event
        if today > event_date_this_year:
            event_date_next_year = date(today.year + 1, month, day)
            days_left = (event_date_next_year - today).days
        else:
            days_left = (event_date_this_year - today).days

        if days_left < min_days_left:
            min_days_left = days_left
            closest_event = event

    return jsonify({'Days until next event': min_days_left, 'Next event': closest_event})

if __name__ == '__main__':
    app.run(debug=True)
