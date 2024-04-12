import json
from datetime import datetime
from calendar import monthrange, day_name
import datetime

def save_habits(habits):
    with open('habits.json', 'w') as f:
        json.dump(habits, f, ensure_ascii=False, indent=4)

def load_habits():
    try:
        with open('habits.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Returns an empty dictionary if the file does not exist.

def log_habit():
    habit = input("Which habit did you perform today? ")
    habits = load_habits()
    if habit in habits:
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")
        if "log" not in habits[habit]:  # Ensure the habit has a 'log' key.
            habits[habit]["log"] = []
        habits[habit]["log"].append({"date": current_date, "time": current_time})  # Append date and time separately
        habits[habit]["last_log_date"] = current_date  # Store date separately
        habits[habit]["last_log_time"] = current_time  # Store time separately
        save_habits(habits)
        print("Habit logged.")
    else:
        print("Habit not found. Please setup the habit first.")

def setup_habit():
    habit = input("Enter the habit you want to setup: ")
    occurrences_per_week = input("How many times per week do you want to perform this habit? ")
    habits = load_habits()
    if habit not in habits:
        habits[habit] = {"log": [], "occurrences_per_week": occurrences_per_week, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "status": "active", "type": "weekly", "last_log_at": None, "other": []}
        save_habits(habits)
        print("Habit setup completed.")
    else:
        print("Habit already exists.")

def view_calendar():
    # Imports for working with calendars
    from calendar import monthrange
    import datetime
    try:
        with open('habits.json') as f:
            habits = json.load(f)
        year, month = datetime.datetime.now().year, datetime.datetime.now().month
        days_in_month = monthrange(year, month)[1]
        print(f"Calendar for {datetime.datetime(year, month, 1).strftime('%B %Y')}:")
        for day in range(1, days_in_month + 1):
            date_str = f"{year}-{month:02d}-{day:02d}"
            events = []
            for habit, details in habits.items():
                if "log" in details:
                    for entry in details["log"]:
                        if entry["date"] == date_str:
                            events.append(habit)
            if events:
                print(f"{date_str}: {', '.join(events)}") 
    except FileNotFoundError:
        print("Habits file not found.")


def view_calendar_graphical():


    try:
        with open('habits.json') as f:
            habits = json.load(f)
        year, month = datetime.datetime.now().year, datetime.datetime.now().month
        days_in_month = monthrange(year, month)[1]
        first_weekday, _ = monthrange(year, month)

        print(f"Calendar for {datetime.datetime(year, month, 1).strftime('%B %Y')} \n   Su    Mo    Tu    We    Th    Fr    Sa")
        print("   " * first_weekday, end="")  # Add padding for the first day

        for day in range(1, days_in_month + 1):
            if day == 1:
                print("  ", end="")
            date_str = f"{year}-{month:02d}-{day:02d}"
            events = any(date_str in [log.get("date") for log in habit.get("log", [])] for habit in habits.values())
            # Mark days with events, e.g., with an asterisk or a different symbol
            day_str = f"{'*'+str(day) if events else str(day):>3}"
            if (day + first_weekday) % 7 == 0:  # If the last day of the week, move to the next line
                day_str += '\n'
            else:
                day_str += ' '
            print(day_str, end="  ")

        if (days_in_month + first_weekday) % 7:  # If the last day of the month isn't a Saturday, add a line break
            print()

    except FileNotFoundError:
        print("Habits file not found.")


def show_habits():
    try:
        with open('habits.json') as f:
            habits = json.load(f)

        for habit in habits:    
            print(f"{habit}: {habits[habit]['occurrences_per_week']} times per week")
            print(f"created at {habits[habit]['created_at']}")
            print(f"{len(habits[habit]['log'])} logs")
            print(f"last log at {habits[habit]['last_log_at']}")
    except FileNotFoundError:
        print("Habits file not found.")

def main():
    while True:
        action = input("Do you want to setup a new habit, log something, show habits, or view the calendar? (setup/log/show/view/exit) ").lower()
        if action == 'exit':
            break
        elif action == 'setup':
            setup_habit()
        elif action == 'log':
            log_habit()
        elif action == 'show':
            show_habits()
        elif action == 'view':
            view_calendar_graphical()
        else:
            print("Invalid command.")


if __name__ == '__main__':
    main()
