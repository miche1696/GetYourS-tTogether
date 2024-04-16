from ast import Invert
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC 
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt


if __name__ == '__main__':

    data = {
    'text': [
        # setup_habit examples
        "settup",
        "Settup habit",
        "create new habit yoga", 
        "setup a reading habit 3x week",
        "start tracking coding daily",
        "add exercise habit twice weekly",
        "track my sleep schedule", 
        # ... add more setup_habit examples

        # log_habit examples
        "log running today",
        "drank 2L of water",
        "meditated for 15 min",
        "practiced guitar today",
        "did my reading",
        # ... add more log_habit examples

        # show_habit_list examples
        "list my habits",
        "what habits am i tracking",
        "habit list",
        "show habit lst", 
        # ... add more show_habit_list examples

        # show_habit_calendar examples
        "show my habit calendar",
        "view progress calendar",
        "calendar of habits",
        "habit tracker calander", 
        # ... add more show_habit_calendar examples

        # other examples
        "close the application",
        "ecit", 
        "exit", 
        "close",
        "escape",
        # ... add more 'other' examples

        # setup_habit
        "create yoga habit", 
        "setup reading habit",
        "track coding daily", 
        "add exercise habit",
        "track sleep schedule", 

        # log_habit
        "log running today",
        "drank enough water", 
        "meditated 15 min",
        "practiced guitar",
        "completed reading", 

        # show_habit_list
        "show my habits",
        "what habits i track", 
        "view my habit list",

        # show_habit_calendar 
        "view habit calendar",
        "my progress calendar",
        # setup_habit
        "new writing habit",
        "track piano practice",
        "start flossing daily",
        "track my walks", 
        "setup weekly workout", 

        # log_habit
        "did yoga today",
        "water intake good",
        "30 mins meditation",
        "coding practice done",
        "studied French",

        # show_habit_list
        "list all habits", 
        "show tracked habits",
        "my current habits",

        # show_habit_calendar 
        "show habit progress",
        "habit tracking calendar",
        "calendar view please",

        # other
        "i want to exit",
        "close", 
        "close the window",
        "close the app",
        "ckose",

        # other
        "what's the weather",
        "set 10 min timer", 
        "play some music",
        "call mom tomorrow",
        "news headlines today" 
    ],
    'intent': [
        "setup_habit", "setup_habit",

        # setup_habit labels
        "setup_habit", "setup_habit", "setup_habit","setup_habit", "setup_habit", 

        # log_habit labels
        "log_habit", "log_habit", "log_habit", "log_habit", "log_habit",

        # show_habit_list labels
        "show_habit_list", "show_habit_list", "show_habit_list", "show_habit_list",

        # show_habit_calendar labels
        "show_habit_calendar", "show_habit_calendar", "show_habit_calendar", "show_habit_calendar",

        # exit labels
        "exit", "exit", "exit", "exit", "exit",

        "setup_habit", "setup_habit",  "setup_habit", "setup_habit", "setup_habit", 
         "log_habit", "log_habit", "log_habit", "log_habit", "log_habit",
         "show_habit_list", "show_habit_list", "show_habit_list",
         "show_habit_calendar", "show_habit_calendar",
         # setup_habit 
        "setup_habit", "setup_habit", "setup_habit", "setup_habit", "setup_habit", 

        # log_habit
        "log_habit", "log_habit", "log_habit", "log_habit", "log_habit",

        # show_habit_list 
        "show_habit_list", "show_habit_list", "show_habit_list", 

         # show_habit_calendar 
        "show_habit_calendar", "show_habit_calendar", "show_habit_calendar",

        # exit
        "exit", "exit", "exit", "exit", "exit",

        # other
        "other", "other", "other", "other", "other"
        ] 
    }

    # Store trained models in a dictionary
    models = {}
    
    df = pd.DataFrame(data)

    # Feature Engineering
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(df['text'])

    X_train, X_test, y_train, y_test = train_test_split(features, df['intent'], test_size=0.2, random_state=42)  # Modified test_size

    # Kernel choices
    kernels = ['linear', 'rbf', 'poly']
    accuracies = []

    # Train and evaluate models with different kernels
    for kernel in kernels:
        model = SVC(kernel=kernel)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = model.score(X_test, y_test)  # Calculate accuracy
        print(f"Kernel: {kernel}")
        print(classification_report(y_test, y_pred))

        # Store the model
        models[kernel] = model 


    while(True):
        new_input = input("\nInsert here the sentance you want to predict: ")
        if not new_input:  # Check for empty input
            print("Please enter a non-empty sentence")
            continue 
        for kernel_name, model in models.items():
            prediction = model.predict(vectorizer.transform([new_input]))
            print(f"Prediction with {kernel_name} kernel: {prediction}")



