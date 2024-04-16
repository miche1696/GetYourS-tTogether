# GetYourS-tTogether

Virual assistant - AI powered Habit Tracker & Helper

Main functions:
- Habit helper/assistant : GetYourS**tTogether helps the user to create or remove habits in his/her life. Assisting the user in all the process of discovery a new habit, planning it, making it stick.
- Habit tracker : Supporting the function above with an easy and immediate way to track your progress without much hussle.

Whatsapp logging trhough audio.

v0.1: DONE
- Habit Setup and Logging - DONE: Easy way to track your progress without much hussle. Limited kind of habits: Running, Training, Quit Smoking, Drink water, Walking.
- Simple UX with text area. - DONE 
    --> Is it convenient to do it through a whatsapp/telegram chat? --> In MVPv3 this could be a thing.
v0.1.1:
- IMPORTANTE : Pending action e logica di reminder/tracking.
- IMPORTANTISSIMO : Tutto questo sistema deve essere a distanza di un tocco o di una parola. Niente inutili interfacce, niente telefonino, niente di niente. Accanto al tuo letto ci deve essere uno bello schermo o un qualcosa tipo una sveglia che effortless ti deve permettere di loggare queste cose, farti vedere dove sei, a che punto del tuo journey ti trovi e rendere tutto questo un gioco che tu verifichi a fine giornata.
mi immagino quasi un mini proiettore che ti proietta sul soffitto la tua situazione, il tuo progresso, i tuoi obiettivi, i tuoi risultati, i tuoi errori, i tuoi successi, i tuoi fallimenti, i tuoi miglioramenti. E tu lo guardi, consultandolo, comodamente dal letto come chek-up prima di andare a dormire. L'esperienza di "habit" diventa quindi un gioco, un passo semplice come quello di leggere un libro. Niente più tacquini, niente più millemila app che ti occupano la memoria. Solo una cosa che ti aiuta a tenere traccia di te stesso e dei tuoi progressi. 
MArketing campaing:
Ti piacerebbe un'esperienza del genere? Ti piacerebbe avere un'assistente virtuale che ti aiuta a tenere traccia di te stesso e dei tuoi progressi? Si. Ma con chi sto parlando? Con te, che leggi. Ma chi sei? Sono il tuo assistente virtuale. Come ti chiami? Non ho un nome, sono il tuo assistente virtuale. Ma come ti chiamo? Chiamami GYST. GYST? Si, GetYourS**tTogether. Ah, ok. Cosa vuoi fare? Voglio aiutarti a tenere traccia di te stesso e dei tuoi progressi. Come? Ti aiuto a creare nuove abitudini, a rimuovere quelle che non ti servono più e a tenere traccia di tutto questo. Come? Ti faccio delle domande, ti do dei consigli, ti ricordo di fare le cose, ti faccio vedere i tuoi progressi, ti faccio vedere i tuoi risultati, ti faccio vedere i tuoi miglioramenti, ti faccio vedere i tuoi errori, ti faccio vedere i tuoi successi.
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
- Habit planning/organization with an active "coach"s
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

