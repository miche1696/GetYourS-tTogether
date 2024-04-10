import json
from datetime import datetime

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
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if "log" not in habits[habit]:  # Ensure the habit has a 'log' key.
            habits[habit]["log"] = []
        habits[habit]["log"].append({"date": current_datetime})
        save_habits(habits)
        print("Habit logged.")
    else:
        print("Habit not found. Please setup the habit first.")

def setup_habit():
    habit = input("Enter the habit you want to setup: ")
    occurrences_per_week = input("How many times per week do you want to perform this habit? ")
    habits = load_habits()
    if habit not in habits:
        habits[habit] = {"log": [], "occurrences_per_week": occurrences_per_week}
        save_habits(habits)
        print("Habit setup completed.")
    else:
        print("Habit already exists.")

def main():
    while True:
        action = input("Do you want to setup a new habit or log something? (setup/log/exit) ").lower()
        if action == 'exit':
            break
        elif action == 'setup':
            setup_habit()
        elif action == 'log':
            log_habit()
        else:
            print("Invalid command.")


if __name__ == '__main__':
    main()
