import pyttsx3
from pyttsx3.engine import Engine
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import calendar
from bs4 import BeautifulSoup
import requests
from PyQt5 import QtCore, QtGui, QtWidgets



import pyttsx3
from pyttsx3.engine import Engine
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import calendar
from bs4 import BeautifulSoup
import requests


class mainP:

    def __init__(self):
        pass

    # Speak function will pronounce the string which is passed to it
    def speak(self, text):
        """Speak function will pronounce the string which is passed to it"""

        print('Initializing Nexus')
        engine = pyttsx3.init('sapi5')
        rate = engine.getProperty('rate')
        voices = engine.getProperty('voices')
        engine.setProperty('voices', voices[0].id)
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()
        # engine.stop()

    def takeCommand(self):
        """ function takes command from the microphone"""

        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('Listening...')
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)
            
        try:
            print('Recognizing...')
            voice_spoken = r.recognize_google(audio, language='en-US')
            print(f'user said: {voice_spoken}\n')

        except Exception as e:
            self.speak('I did not get any word from you. Kindly say it again. Or perhaps your network connection')
            

        return voice_spoken.lower()


class Voice(mainP):
    def __init__(self):
        self.greeting()

    def greeting(self):
        hour = int(datetime.datetime.now().hour)

        if hour >= 0 and hour < 12:
            self.speak('Good Morning')

        elif hour >= 12 and hour < 18:
            self.speak('Good Afternoon')

        else:
            self.speak('Good Evening')

        self.speak('How may I help you ?')

    def to_speak(self, voice_spoken):
        # Logic for executing basic tasks as per the voice_spoken
        if 'who are you' in voice_spoken:
            self.speak('I am a virtual assistant built by my creator zac. I\'m doing great and here to help you out')

        elif 'how are you' in voice_spoken:
            reply = ['Thanks for asking!... I am doing well.', 'The best I can be... Assuming you are at your best too',
            'Much better now that you are with me.', 'Like you, but better']
            self.speak(random.choice(reply))

        elif 'hello' in voice_spoken or 'hey' in voice_spoken:
            greeting_back = ['Yes', 'greetings to you', 'Nice to hear from you']
            self.speak(random.choice(greeting_back))

        elif 'time' in voice_spoken:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            self.speak(f'the time is {strTime}')

        elif 'date' in voice_spoken:
            now = datetime.datetime.now()
            daytoday = datetime.datetime.today()
            # to get day of the week
            weekday = calendar.day_name[daytoday.weekday()]
            currentmonth = now.month
            daynow = now.day
            yearnow = now.year
            monthnames = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                        'september', 'october', 'november', 'december']
            daysofmonth = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th',
                        '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th',
                        '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27', '29th',
                        '30th', '31st']
            self.speak(f'Today is {weekday} {daysofmonth[daynow-1]} of {monthnames[currentmonth-1]} {yearnow}')

        elif 'weather' in voice_spoken or 'temperature' in voice_spoken:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

            def weather(city):
                city = city.replace(" ", "+")
                res = requests.get(
                    f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
                print("Searching...\n")
                soup = BeautifulSoup(res.text, 'html.parser')
                location = soup.select('#wob_loc')[0].getText().strip()
                time = soup.select('#wob_dts')[0].getText().strip()
                weather_info = soup.select('#wob_dc')[0].getText().strip()
                temp = soup.select('#wob_tm')[0].getText().strip()

                self.speak(f'The weather in {location} is {weather_info} and the temperature is {temp} degrees celcious')

            city = 'kampala'
            city = city + "weather"
            weather(city)

        elif 'wikipedia' in voice_spoken or 'what' in voice_spoken or 'who' in voice_spoken:
            voice_spoken = voice_spoken.replace('on wikipedia', '')
            voice_spoken = voice_spoken.replace('wikipedia', '')
            voice_spoken = voice_spoken.replace('what', '')
            voice_spoken = voice_spoken.replace('who', '')
            voice_spoken = voice_spoken.replace('is', '')
            voice_spoken = voice_spoken.replace('are', '')

            self.speak(f'getting information about {voice_spoken}, ..give me a second')
            results = wikipedia.summary(voice_spoken, sentences=2)
            print(results)
            self.speak(results)

        elif 'news' in voice_spoken:
            self.speak('Getting the latest news...')
            webbrowser.open('https://news.google.com/topstories')

        elif 'open google' == voice_spoken:
            self.speak('opening google...')
            webbrowser.open('https://www.google.com')

        elif 'open youtube' == voice_spoken:
            self.speak('opening youtube')
            webbrowser.open('https://www.youtube.com/')

        elif 'facebook' in voice_spoken:
            self.speak('opening facebook')
            webbrowser.open('https://www.facebook.com/')

        elif 'instagram' in voice_spoken:
            self.speak('opening instagram')
            webbrowser.open('https://www.instagram.com/') 

        elif 'play music' in voice_spoken or 'music' in voice_spoken:
            self.speak('Playing music')
            songs_dir = 'C:\\Users\\R\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'search' in voice_spoken and 'youtube' in voice_spoken:
            voice_spoken = voice_spoken.replace('search', '')
            voice_spoken = voice_spoken.replace('on youtube', '')
            voice_spoken = voice_spoken.replace('youtube', '')
            voice_spoken = voice_spoken.replace('in', '')
            voice_spoken = voice_spoken.replace('for', '')
            string = voice_spoken.split()
            search = ''
            for i in string:
                search += i

            webbrowser.open(f'https://www.youtube.com/results?search_query={search}')
            self.speak(f'Loading your results on {search}')

        elif 'open code' == voice_spoken or 'vs code' in voice_spoken:
            codePath = 'C:\Program Files\Microsoft VS Code\Code.exe'
            os.startfile(codePath)

        elif 'search' in voice_spoken and 'google' in voice_spoken:
            voice_spoken = voice_spoken.replace('search', '')
            voice_spoken = voice_spoken.replace('on google', '')
            voice_spoken = voice_spoken.replace('google', '')
            voice_spoken = voice_spoken.replace('in', '')
            voice_spoken = voice_spoken.replace('for', '')
            string = voice_spoken.split()
            search = ''
            for i in string:
                search += i
                search += '+'

            webbrowser.open(f'https://www.google.com/search?q={search}&oq={search}&aqs=chrome..69i57.4597j0j4&sourceid=chrome&ie=UTF-8')
            self.speak(f'Loading your results on {search}')

        elif 'joke' in voice_spoken or 'jokes' in voice_spoken or 'funny' in voice_spoken or 'fun' in voice_spoken or 'bored' in voice_spoken:
            jokes_list = ['why did the scarecrow keep gettin promoted?..  Because he was outstanding in his field',
            'What did Batman say to Robin before they got in the car?..  Robin, get in the car.', 'What\'s red and shaped like a bucket?.... A blue bucket painted red.',
            'Did you hear about the two thieves who stole a calendar?..  They each got six months.', 'Why was the math teacher late to work?...  She took the rhombus.',
            'My daughter thinks I don\'t give her enough privacy....  At least that\'s what she wrote in her diary.', 'Why can\'t you trust an atom?.... Because they make up everything.',
            'The guy that invented the umbrella was gonna call it the brella....  But he hesitated.', 'Fun fact: Australia\'s biggest export is boomerangs. It\'s also their biggest import.',
            'Before the invention of the wheel…   everything was a drag!', 'What do you call it when Dwayne Johnson buys a cutting tool?... Rock pay for scissors.',
            'What did the duck say when she bought a lipstick?... Put it on my bill!', 'What did the little mountain say to the bigger mountain?...  Hi Cliff!',
            'Why are there gates around cemeteries?...  Because people are dying to get in!', 'Do you remember that joke I told you about my spine?... It was about a weak back!',
            'Today I gave my dead batteries away....  They were free of charge.', 'What does a zombie vegetarian eat?... "Graaaaaaaains!', 'What did the blanket say as it fell off the bed?... Oh sheet!',
            'Why shouldn\'t you write with a broken pencil?.. Because it\'s pointless!']

            self.speak(random.choice(jokes_list))

        elif 'thanks' in voice_spoken or 'thank you' in voice_spoken or 'i like you' in voice_spoken:
            self.speak('I\'m glad you\'re happy')

        else:
            string = voice_spoken.split()
            search = ''
            for i in string:
                search += i
                search += '+'
            self.speak('Sorry I did not get that. But this is what I got for you on google')
            webbrowser.open(f'https://www.google.com/search?q={search}&oq={search}&aqs=chrome..69i57.4597j0j4&sourceid=chrome&ie=UTF-8')


class Ui_MainWindow(object):

    def buttonClicked(self):
        voice = Voice()
        voice_spoken = voice.takeCommand()
        self.text_label.setText(voice_spoken)
        self.text_label_2.setText("Listening .....   \n\nRecognizing ..... \n\nFINISHED...   ")
        voice.to_speak(voice_spoken)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 600)
        MainWindow.setStyleSheet("*{\n"
"font-family:Verdana\n"
"}\n"
"\n"
"#biggy_frame{\n"
"background:rgb(0, 65, 98)\n"
"}\n"
"QFrame{\n"
"background:#007f5d;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"#small_frame{\n"
"background:white;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"#speak{\n"
"color: white;\n"
"font: 24px;\n"
"background:transparent\n"
"}\n"
"\n"
"#button{\n"
"background:white;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"#nex{\n"
"background:white;\n"
"color:rgb(0, 103, 74);\n"
"font:24px;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"#toolButton{\n"
"background:transparent\n"
"}\n"
"\n"
"#text_label{\n"
"color:rgb(70, 70, 70);\n"
"background:transparent;\n"
"border:1px solid #007f5d;\n"
"font-size:18px;\n"
"}\n"
"\n"
"#text_label_2{\n"
"background: none;\n"
"font-size: 18px;\n"
"color:rgb(138, 138, 138);\n"
"border: 1px solid rgb(50, 0, 150)\n"
"}\n"
"\n"
"#text_edit1{\n"
"color:white;\n"
"background-color:rgba(58, 58, 58, 50)\n"
"}\n"
"\n"
"#user_says{\n"
"font-size: 15px;\n"
"color: white;\n"
"background:rgb(116, 116, 116);\n"
"border-radius:6px;\n"
"}\n"
"#response{\n"
"font-size: 15px;\n"
"color: white;\n"
"background:rgb(116, 116, 116);\n"
"border-radius:6px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.biggy_frame = QtWidgets.QFrame(self.centralwidget)
        self.biggy_frame.setGeometry(QtCore.QRect(0, 0, 791, 581))
        self.biggy_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.biggy_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.biggy_frame.setObjectName("biggy_frame")
        self.small_frame = QtWidgets.QFrame(self.biggy_frame)
        self.small_frame.setGeometry(QtCore.QRect(370, 10, 391, 551))
        self.small_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.small_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.small_frame.setObjectName("small_frame")
        self.text_label = QtWidgets.QLabel(self.small_frame)
        self.text_label.setGeometry(QtCore.QRect(10, 70, 371, 91))
        self.text_label.setWordWrap(True)
        self.text_label.setObjectName("text_label")
        self.text_label_2 = QtWidgets.QLabel(self.small_frame)
        self.text_label_2.setGeometry(QtCore.QRect(10, 220, 371, 321))
        self.text_label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_label_2.setScaledContents(True)
        self.text_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.text_label_2.setWordWrap(True)
        self.text_label_2.setIndent(0)
        self.text_label_2.setObjectName("text_label_2")
        self.user_says = QtWidgets.QLabel(self.small_frame)
        self.user_says.setGeometry(QtCore.QRect(280, 30, 101, 31))
        self.user_says.setObjectName("user_says")
        self.response = QtWidgets.QLabel(self.small_frame)
        self.response.setGeometry(QtCore.QRect(10, 180, 101, 31))
        self.response.setObjectName("response")
        self.speak = QtWidgets.QLabel(self.biggy_frame)
        self.speak.setGeometry(QtCore.QRect(60, 500, 241, 51))
        self.speak.setObjectName("speak")
        self.button = QtWidgets.QPushButton(self.biggy_frame)
        self.button.setGeometry(QtCore.QRect(110, 500, 61, 61))
        self.button.clicked.connect(self.buttonClicked)
        self.button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/download (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button.setIcon(icon)
        self.button.setIconSize(QtCore.QSize(45, 45))
        self.button.setObjectName("button")
        self.nex = QtWidgets.QLabel(self.biggy_frame)
        self.nex.setGeometry(QtCore.QRect(10, 40, 351, 71))
        self.nex.setObjectName("nex")
        self.toolButton = QtWidgets.QToolButton(self.biggy_frame)
        self.toolButton.setGeometry(QtCore.QRect(190, 10, 211, 131))
        self.toolButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/bot1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(80, 100))
        self.toolButton.setObjectName("toolButton")
        self.text_edit1 = QtWidgets.QTextEdit(self.biggy_frame)
        self.text_edit1.setGeometry(QtCore.QRect(40, 150, 291, 301))
        self.text_edit1.setObjectName("text_edit1")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_label.setText(_translate("MainWindow", ""))
        self.text_label_2.setText(_translate("MainWindow", ""))
        self.user_says.setText(_translate("MainWindow", "  User said:"))
        self.response.setText(_translate("MainWindow", "Response:"))
        self.speak.setText(_translate("MainWindow", "Tap          Speak"))
        self.nex.setText(_translate("MainWindow", " Nexus"))
        self.text_edit1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Verdana\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Introducing Nexus. Your  personal virtual assistant</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> Nexus is capable of doing  your daily tasks for you for example telling the time, date, weather, information about anything and so much more </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> To start Nexus, tap the  button below</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
