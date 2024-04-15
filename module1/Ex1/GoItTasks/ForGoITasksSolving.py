from datetime import datetime, timedelta

def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday


users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

print(adjust_for_weekend(users))