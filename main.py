import json
from calendar import monthrange, day_name
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import spacy
from spacy.matcher import Matcher

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

def log_habit(habit):
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

def setup_habit(habit, occurrences_per_week):
    habits = load_habits()
    if habit not in habits:
        habits[habit] = {"log": [], "occurrences_per_week": occurrences_per_week, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "status": "active", "type": "weekly", "last_log_at": None, "other": []}
        save_habits(habits)
        print("Habit setup completed.")
        return True
    else:
        print("Habit already exists.")
        return False

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

def main_gui_classic():
    def setup_habit_wrapper():
        def on_submit():
            habit = habit_entry.get()
            occurrences_per_week = occurrences_entry.get()

            ## TO DO - Message back the user in case of success or insuccess
            setup_habit(habit, occurrences_per_week)
            messagebox.showinfo("Habit Setup", f"Habit '{habit}' setup with {occurrences_per_week} occurrences per week.")
            setup_window.destroy()

        setup_window = tk.Tk()
        setup_window.title("Setup Habit")

        tk.Label(setup_window, text="Habit:").pack()
        habit_entry = tk.Entry(setup_window)
        habit_entry.pack()

        tk.Label(setup_window, text="Occurrences per week:").pack()
        occurrences_entry = tk.Entry(setup_window)
        occurrences_entry.pack()

        submit_button = tk.Button(setup_window, text="Submit", command=on_submit)
        submit_button.pack()

        setup_window.mainloop()

    def log_habit_wrapper():
        def submit():
            habit = habit_var.get()
            # Integrate with your backend logic to log the habit here.
            log_habit(habit)
            # For demonstration, print the selected habit:
            print(f"Logging habit: {habit}")
            messagebox.showinfo("Success", f"Successfully logged habit: {habit}")
            log_window.destroy()

        habits = load_habits()
        habit_names = list(habits.keys())

        log_window = tk.Tk()
        log_window.title("Log a Habit")

        tk.Label(log_window, text="Select habit:").pack()

        habit_var = tk.StringVar(log_window)
        habit_dropdown = ttk.Combobox(log_window, textvariable=habit_var, values=habit_names)
        habit_dropdown.pack()

        log_button = tk.Button(log_window, text="Log Habit", command=submit)
        log_button.pack()

        log_window.mainloop()

    def show_habits_wrapper():
        habits = load_habits()
        if habits is None:
            return

        habits_window = tk.Tk()
        habits_window.title("Habit List")

        for habit, details in habits.items():
            tk.Label(habits_window, text=f"{habit}: {details['occurrences_per_week']} times per week", font=('Helvetica', 10, 'bold')).pack()
            tk.Label(habits_window, text=f"Created at: {details['created_at']}", font=('Helvetica', 8)).pack()
            tk.Label(habits_window, text=f"{len(details['log'])} logs", font=('Helvetica', 8)).pack()
            if details['last_log_at']:
                tk.Label(habits_window, text=f"Last logged: {details['last_log_at']}", font=('Helvetica', 8)).pack()
            else:
                tk.Label(habits_window, text="Not logged yet", font=('Helvetica', 8)).pack()
            tk.Label(habits_window, text="---------------------------------------").pack()

        habits_window.mainloop()

    def view_calendar_graphical_wrapper():
        def show_calendar(year, month, habits):
            root = tk.Tk()
            root.title(f"{datetime(year, month, 1).strftime('%B %Y')}")
            days_in_month = monthrange(year, month)[1]
            first_weekday, _ = monthrange(year, month)

            days_frame = tk.Frame(root)
            days_frame.pack()

            # Prepare the grid
            for i in range(7):  # 7 days in a week
                tk.Label(days_frame, text=["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"][i]).grid(row=0, column=i)

            # Fill days
            for day in range(1, days_in_month + 1):
                day_date = datetime(year, month, day).strftime("%Y-%m-%d")
                day_widget = tk.Text(days_frame, width=20, height=10, borderwidth=2, relief="groove")
                day_events = []
                # Check for habit events on this day
                for habit, details in habits.items():
                    for log in details.get("log", []):
                        if log["date"] == day_date:
                            day_events.append(habit)
                day_widget.insert("end", f"{day}\n" + "\n".join(day_events))
                day_widget.config(state="disabled")
                row, column = divmod(first_weekday + day - 1, 7)
                day_widget.grid(row=row + 1, column=column, padx=1, pady=1)

            root.mainloop()   # Create the main window

        try:
            with open('habits.json') as f:
                habits = json.load(f)
            year, month = datetime.now().year, datetime.now().month
            show_calendar(year, month, habits)
        except FileNotFoundError:
            messagebox.showerror("Error", "Habits file not found.")

    window = tk.Tk()
    window.title("Habit Tracker")

    # Create buttons for each action
    tk.Button(window, text="Setup Habit", command=setup_habit_wrapper).pack(pady=10)
    tk.Button(window, text="Log Habit", command=log_habit_wrapper).pack(pady=10)
    tk.Button(window, text="Show Habits", command=show_habits_wrapper).pack(pady=10)
    tk.Button(window, text="View Calendar", command=view_calendar_graphical_wrapper).pack(pady=10)
    tk.Button(window, text="Exit", command=window.quit).pack(pady=10)

    window.mainloop()

def main_gui():
    def setup_habit_wrapper():
        def on_submit():
            habit = habit_entry.get()
            occurrences_per_week = occurrences_entry.get()

            ## TO DO - Message back the user in case of success or insuccess
            setup_habit(habit, occurrences_per_week)
            messagebox.showinfo("Habit Setup", f"Habit '{habit}' setup with {occurrences_per_week} occurrences per week.")
            setup_window.destroy()

        setup_window = tk.Tk()
        setup_window.title("Setup Habit")

        tk.Label(setup_window, text="Habit:").pack()
        habit_entry = tk.Entry(setup_window)
        habit_entry.pack()

        tk.Label(setup_window, text="Occurrences per week:").pack()
        occurrences_entry = tk.Entry(setup_window)
        occurrences_entry.pack()

        submit_button = tk.Button(setup_window, text="Submit", command=on_submit)
        submit_button.pack()

        setup_window.mainloop()

    def log_habit_wrapper():
        def submit():
            habit = habit_var.get()
            # Integrate with your backend logic to log the habit here.
            log_habit(habit)
            # For demonstration, print the selected habit:
            print(f"Logging habit: {habit}")
            messagebox.showinfo("Success", f"Successfully logged habit: {habit}")
            log_window.destroy()

        habits = load_habits()
        habit_names = list(habits.keys())

        log_window = tk.Tk()
        log_window.title("Log a Habit")

        tk.Label(log_window, text="Select habit:").pack()

        habit_var = tk.StringVar(log_window)
        habit_dropdown = ttk.Combobox(log_window, textvariable=habit_var, values=habit_names)
        habit_dropdown.pack()

        log_button = tk.Button(log_window, text="Log Habit", command=submit)
        log_button.pack()

        log_window.mainloop()

    def show_habits_wrapper():
        habits = load_habits()
        if habits is None:
            return

        habits_window = tk.Tk()
        habits_window.title("Habit List")

        for habit, details in habits.items():
            tk.Label(habits_window, text=f"{habit}: {details['occurrences_per_week']} times per week", font=('Helvetica', 10, 'bold')).pack()
            tk.Label(habits_window, text=f"Created at: {details['created_at']}", font=('Helvetica', 8)).pack()
            tk.Label(habits_window, text=f"{len(details['log'])} logs", font=('Helvetica', 8)).pack()
            if details['last_log_at']:
                tk.Label(habits_window, text=f"Last logged: {details['last_log_at']}", font=('Helvetica', 8)).pack()
            else:
                tk.Label(habits_window, text="Not logged yet", font=('Helvetica', 8)).pack()
            tk.Label(habits_window, text="---------------------------------------").pack()

        habits_window.mainloop()

    def view_calendar_graphical_wrapper():
        def show_calendar(year, month, habits):
            root = tk.Tk()
            root.title(f"{datetime(year, month, 1).strftime('%B %Y')}")
            days_in_month = monthrange(year, month)[1]
            first_weekday, _ = monthrange(year, month)

            days_frame = tk.Frame(root)
            days_frame.pack()

            # Prepare the grid
            for i in range(7):  # 7 days in a week
                tk.Label(days_frame, text=["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"][i]).grid(row=0, column=i)

            # Fill days
            for day in range(1, days_in_month + 1):
                day_date = datetime(year, month, day).strftime("%Y-%m-%d")
                day_widget = tk.Text(days_frame, width=20, height=10, borderwidth=2, relief="groove")
                day_events = []
                # Check for habit events on this day
                for habit, details in habits.items():
                    for log in details.get("log", []):
                        if log["date"] == day_date:
                            day_events.append(habit)
                day_widget.insert("end", f"{day}\n" + "\n".join(day_events))
                day_widget.config(state="disabled")
                row, column = divmod(first_weekday + day - 1, 7)
                day_widget.grid(row=row + 1, column=column, padx=1, pady=1)

            root.mainloop()   # Create the main window

        try:
            with open('habits.json') as f:
                habits = json.load(f)
            year, month = datetime.now().year, datetime.now().month
            show_calendar(year, month, habits)
        except FileNotFoundError:
            messagebox.showerror("Error", "Habits file not found.")

        # Function to detect intent
    
    def interpret_user_input():
        user_input = text_entry.get("1.0", "end").strip()  # Get user input from the text box
        detect_intent(user_input)  # Pass the user input to the intent detection function

    def detect_intent(text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text.lower())  # Convert text to lowercase for case insensitivity
        matcher = Matcher(nlp.vocab)
        
        # Define patterns for each intent
        setup_habit_patterns = [
            [{"LEMMA": {"IN": ["setup", "start", "create"]}}, {"LEMMA": "habit"}],
            [{"LEMMA": "add"}, {"LEMMA": "new"}, {"LEMMA": "habit"}]
        ]
        
        log_habit_patterns = [
            [{"LEMMA": {"IN": ["log", "record", "track"]}}, {"LEMMA": "habit"}],
            [{"LEMMA": "add"}, {"LEMMA": "log"}, {"LEMMA": "habit"}],
            [{"LEMMA": "record"}, {"LEMMA": "activity"}]
        ]
        
        show_habits_patterns = [
            [{"LEMMA": {"IN": ["show", "display", "list"]}}, {"LEMMA": "habit"}],
            [{"LEMMA": "view"}, {"LEMMA": "habits"}],
            [{"LEMMA": "see"}, {"LEMMA": "habits"}]
        ]
        
        show_calendar_patterns = [
            [{"LEMMA": {"IN": ["show", "display", "view", "see"]}}, {"LEMMA": "calendar"}]
        ]

        # Add patterns to the matcher for each intent
        for pattern in setup_habit_patterns:
            matcher.add("SETUP_HABIT", pattern)
        for pattern in log_habit_patterns:
            matcher.add("LOG_HABIT", pattern)
        for pattern in show_habits_patterns:
            matcher.add("SHOW_HABITS", pattern)
        for pattern in show_calendar_patterns:
            matcher.add("SHOW_CALENDAR", pattern)

        # Find matches
        matches = matcher(doc)
        
        # Based on matches, execute corresponding functions
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]
            if string_id == "SETUP_HABIT":
                setup_habit_wrapper()
            elif string_id == "LOG_HABIT":
                log_habit_wrapper()
            elif string_id == "SHOW_HABITS":
                show_habits_wrapper()
            elif string_id == "SHOW_CALENDAR":
                view_calendar_graphical_wrapper()
            else:
                print("Command not recognized.")

        


    window = tk.Tk()
    window.title("Habit Tracker")

    tk.Button(window, text="Setup Habit", command=setup_habit_wrapper).pack(pady=10)
    tk.Button(window, text="Log Habit", command=log_habit_wrapper).pack(pady=10)
    tk.Button(window, text="Show Habits", command=show_habits_wrapper).pack(pady=10)
    tk.Button(window, text="View Calendar", command=view_calendar_graphical_wrapper).pack(pady=10)
    tk.Button(window, text="Exit", command=window.quit).pack(pady=10)
    
    # Text entry box for free-form user input
    text_entry = tk.Text(window, height=5, width=50)
    text_entry.pack(pady=10)
    # Button to interpret the user input
    tk.Button(window, text="Interpret User Input", command=interpret_user_input).pack(pady=10)


    window.mainloop()

if __name__ == '__main__':
    main_gui()
    ##main()