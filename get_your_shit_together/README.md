# GetYourS-tTogether

Virual assistant - AI powered Habit Tracker & Helper

Main functions:
- Habit helper/assistant : GetYourS**tTogether helps the user to create or remove habits in his/her life. Assisting the user in all the process of discovery a new habit, planning it, making it stick.
- Habit tracker : Supporting the function above with an easy and immediate way to track your progress without much hussle.

User journey:
1) The user goes to the app and finds a login page where he can insert his username (unique) and password.
2) If the user is not registered, there is a button "register" that gives him the chance to register a new username and password to the platform.
2.1) If the user click on "register" a second page gives him the chance to enger an username and a password and register. Once done, the user is taken back to the first login page.
3) Once the user accesses with a registered and correct user/password, the app shows the menu, composed of the main functions : "Insert new habit", "Log habit occurrence", "Show my habits", "Show calendar of my past and future habits". All the information shown from now on is the information of the particular user that just logged in. Every habit, log and other information is the one of the user that just logged. User can't see other users habits.
3.1) If the user clicks on "Insert new habits", another page is shown and shows two text box and a button with written "submit". The user can insert a "name of the habit" (a simple text box), a "number of occurrences per week" (a number), then, clicking "submit" he saves the habit. The information of this habit are now saved on the database correspondent to the user.
3.2) If the user clicks on "Log habit occurrence", another page is shown and shows a dropdown list and a button with written "submit". The drop down list shows all the habit that were previously saved from the user. The user can select only one habit of the list. This is the list that will be logged. Then, pressing the button "submit", the information of the current date and time is saved in the database correspondent to the user. This information is stored in a way that makes then easier to being shown from other function ("show my habits" and "show calendar of my past and future habits")
3.3) If the user clicks on "show my habits", another page is shown and shows the list of all the habits that are currently active on the user correspondent database. The page shows "name of the habit" "number of occurrences per week", "total number of logged events for this habit" and "date and time of the last logged occurrence of this habit". Then on the right of every habit shown, there is a "bin" symbol, that gives the user the possibility of deleting the habit, deleting all the information about this habit from the database of the user hence removing it form the visualization.
3.4) If the user clicks on "Show calendar of my past and future habits", then another page is shown and shows a calendar (like a google or outlook one), showing, with different colors, all the occurrences of the different habits in the past, in each "tile" of the correspondent day that the logged habit took place. Write this function in a way that what is shown is coming from a vector of dates, so that then is easy to add some more dates when the "future planning" function will take place (a function that, based on how much habit occurrences are being logged in the past, plans in the following days future occurrences and suggest them to the user)


v0.1: DONE
- Habit Setup: Easy way to track your progress without much hussle. Limited kind of habits: Running, Training, Quit Smoking, Drink water, Walking. (This list of items should be modifiable in the shape of a vector, in the case there is the wish of adding new possible habits to offer to the user in the future) When deciding to add a new habit, the user has to insert the number of times he desires to do this habit during a week.
- Habit logging: The user can choose one of the habit that he setup in the past, to log an occurrence of the habit. The habit logged is considered to being done in the day of the logging. The information of the log (date and hour of the log) is saved to then being shown on a calendar of all the past occurrences. 
v0.1.1:
- IMPORTANTE : Pending action e logica di reminder/tracking. The app, once the habit is entered by the user with all the information (name, number of desired occurrences per week, etc..) is now taking in consideration the cadence at which the user should do that habit in order to maintain the habit itself. This means planning, with an omogeneous cadence, when the habits occurrences should happen and saving this in a "calendar" of future events the user has to do. Then based on the real act and logging of the user, different notification or actions come from the application itself. In particular : 
    - The user recieves a notification (on its client) that reminds him that there is an upcoming "date in which you should execute the habit". This happens one day before the day of the "future habit occurrence"
    - In the case the occurrence is not satisfied, the app plans again the "calendar of future events" so that it is now manageable to respect the deadline before the end of the week.
    - If the case of occurrence is not safisfied at the point of not being respectable during the current week (because the days remaining are less than the number of remaining occurrence to execute during the week), just simplify the number of needed occurrence to stay "inside" the week that is terminating.
- Show the calendar of past and future occurrences of the habit that are ongoing for the user.
v0.1.2:
- Authentication and different user profiles. The user accesses the platform with its own credentials (username - unique - and password). Every user has its own set of habits and every action is stored in a common database under its username. Use the best common practices to implement this authentication and storage of the users data.
v0.2:
- Virtual assistant: It supports the habit tracking, enabling the or setup of the habit and logging via chat or just via voice.
    --> ML algorthm to recognize the commands of the user.
- Results/Tracking Calendar (DONE). 
- Access to the personal/professional calendar of the user, to support the habit tracking. The calendar gives the user the chance to create some slots of free moments when the habits should be done.
v0.3:
- User authentication. Log in and profiles. 
- Download of the user information and cloud deployment of the database so that it can be retrieved anywhere.
v0.4:
- Reminders, based on a first level "intelligent" planner/virtual assistant. Gathering of all the datas of the user that can be helpful to schedule/maximize the amount of successful tasks. From the acces to the personal/professional calendar. At this stage is just a simple algorithm that takes the possible free slots, classifies the habits in low/medium/high/critical "risk of not keeping the habit ongoing" or "not having the time to keep the pace this week/month.
- Whatsapp/Telegram integration? You can use this app from everywhere, even just "calling" you Virtual assistant or sending him/her a whatsapp audio to keep track of everything, log, etc.. This aims to make the experience smooth and extremely versatile. 
v0.5:
- Gamification experience. Gamification dashboard and achievements. At first static, in thext MVP the achievement will be created with genAI.
- Create incentives, only under the shape of "internal points". 
v0.6:
- AI powered gamification experience.
v0.7:
- Cross-selling of services to improve in that habit, to push it to the next level.
v0.8:
- AI powered cross-selling of services.
v0.9:
- Habit planning/organization with an active "coach"
-0.10:
- Hardware : Tutto questo sistema deve essere a distanza di un tocco o di una parola. Niente inutili interfacce, niente telefonino, niente di niente. Accanto al tuo letto ci deve essere uno bello schermo o un qualcosa tipo una sveglia che effortless ti deve permettere di loggare queste cose, farti vedere dove sei, a che punto del tuo journey ti trovi e rendere tutto questo un gioco che tu verifichi a fine giornata.
mi immagino quasi un mini proiettore che ti proietta sul soffitto la tua situazione, il tuo progresso, i tuoi obiettivi, i tuoi risultati, i tuoi errori, i tuoi successi, i tuoi fallimenti, i tuoi miglioramenti. E tu lo guardi, consultandolo, comodamente dal letto come chek-up prima di andare a dormire. L'esperienza di "habit" diventa quindi un gioco, un passo semplice come quello di leggere un libro. Niente più tacquini, niente più millemila app che ti occupano la memoria. Solo una cosa che ti aiuta a tenere traccia di te stesso e dei tuoi progressi. 
_______________________________________________________

MVP

    Virtual assistant, that "talks" with you. Simple UX.
    
    Typycal user interaction: 
    CASE1 ) Initiate a new habit
        USER : "I want to stick to a new habit"
        GYST : "What habit?"
        U : I want to exercise regularly

    ********FUTURE IMPROVEMENTS 
    HABIT PLANNING/ORGANIZATION (needs to collaborate or connect with other specific platforms that are more vertical in the scope of the habit, in this case the training, to provide a tailored plan)
        G : What kind of training? What is your goal/drive?
        U : Lose fat and stay healty/fit
        G : Perfect, are you familiar with training? Did you train on the past?
        U : No
        G : Do you like to run/cycle or are you interest in weightlifting?
        U : Run/Cycle/Treadmill
    ********END


        G : How many times do you want to train per week?
        U : 2 times
        G : There is a moment of the day you prefer to train?
        U : No.

    ********FUTURE IMPROVEMENTS 
    POSSIBILITY OF CROSS-SELLING OF SUPPORTING EQUIPMENT OR SERVICES
        G : Do you prefer to train indoor or outside?
        U : Indoor.
        G : Do you have access to a treadmill, cyclette or ellyptical? Through a gym membership?
        U : No.
        G : Do you want to subscribe a tailored gym membership to support you on this habit tracking?
        ecc...ecc...
    ********END

    ********FUTURE IMPROVEMENTS 
    Gamification of the habit. Incentives, penalties. Needs integration with portfolios or other platform to make this effective. (Idea is that you could consider to penalyze the user if he/she does not train for a week, with, for example, a "lock" of 50 euro to the app that uses to make shopping)
        G : Do you wish to reinforce this habit with some achievements or penalties?
        U : Yes
        G : Do you want to setup a "salvadenaio" to reward or "punish" you when you stick or not to the habit?
        ecc...ecc...
    ********END

        G : Perfect! I will help you to Get Your S**t Together and support on this new habit!

Now the habit is entered. 
The User can now log the activity:

    ********FUTURE IMPROVEMENTS 
    Support of the activity. In this case for example a running app. (GPS or other integration needed)
        U : Hi, I'm going to run now.
        G : Perfect! I'm start the clock and track the effort/RMPS! Good luck!
        Training goes and information are registered. In particular regarding the time at which the training happens and the lenght, to schedule next sessions.
    ********END

        G : Do you want to log something?
        U : Yes, I went to run today

    ********FUTURE IMPROVEMENTS 
    Detailed loggin of the activity. Even thikning about integrating it with other apps (running app or similar).
        G : Let me retrieve the training details and log the details too!
    ********END

        G : Perfect! Logged! You are X out of 2 training this week! Based on your schedule and things to do, I suggest you to run again in X days, between 6AM and 8AM or 6PM and 8PM! I will remind you anyway! Keep it up! You are doing great! (blablabla)

