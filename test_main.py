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


        
print('Initializing Nexus')

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate', 150)

# Speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <  12:
        speak('Good Morning' )

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon' )

    else:
        speak('Good Evening')            
    
    
    speak('How may I help you ?')



# This function will take command from the microphone

def takeCommand():
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
            speak('I did not get any word from you. Kindly say it again. Or perhaps your network connection')
            

        return voice_spoken.lower() 
    
wishMe() 
voice_spoken = takeCommand()



#Logic for executing basic tasks as per the voice_spoken
if 'who are you' in voice_spoken:
    speak('I am a virtual assistant built by my creator zac. I\'m doing great and here to help you out') 

elif 'how are you' in voice_spoken:
    reply = ['Thanks for asking!... I am doing well.','The best I can be... Assuming you are at your best too',
    'Much better now that you are with me.','Like you, but better']    
    speak(random.choice(reply))

elif 'hello' in voice_spoken or 'hey' in voice_spoken:
            greeting_back = ['Yes', 'greetings to you','Nice to hear from you']
            speak(random.choice(greeting_back))

elif 'time' in voice_spoken:
    strTime = datetime.datetime.now().strftime('%H:%M:%S') 
    speak(f'the time is {strTime}') 

elif 'date' in voice_spoken:
    now=datetime.datetime.now()
    daytoday=datetime.datetime.today()
    weekday=calendar.day_name[daytoday.weekday()] # to get day of the week
    currentmonth=now.month
    daynow=now.day
    yearnow=now.year
    monthnames=['january','february','march','april','may','june','july','august',
                'september','october','november','december']
    daysofmonth=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th',
                '11th','12th','13th','14th','15th','16th','17th','18th','19th',
                '20th','21st','22nd','23rd','24th','25th','26th','27','29th',
                '30th','31st']
    speak(f'Today is {weekday} {daysofmonth[daynow-1]} of {monthnames[currentmonth-1]} {yearnow}')

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
        
        
        speak(f'The weather in {location} is {weather_info} and the temperature is {temp} degrees celcious ')


    city = 'kampala'
    city = city+" weather"
    weather(city)

            
elif 'wikipedia' in voice_spoken or 'what' in voice_spoken or 'who' in voice_spoken:
    voice_spoken = voice_spoken.replace('on wikipedia', '')
    voice_spoken = voice_spoken.replace('wikipedia', '')
    voice_spoken = voice_spoken.replace('what', '')
    voice_spoken = voice_spoken.replace('who', '')
    voice_spoken = voice_spoken.replace('is', '')
    voice_spoken = voice_spoken.replace('are', '')

    speak(f'getting information about {voice_spoken}, ..give me a second')
    results = wikipedia.summary(voice_spoken, sentences=2)
    speak(results)
    print(results)

elif 'news' in voice_spoken:
    speak('Getting the latest news...')
    webbrowser.open('https://news.google.com/topstories')
    
elif 'open google' == voice_spoken:
    speak('opening google...')
    webbrowser.open('https://www.google.com')

elif 'open youtube' == voice_spoken:
    speak('opening youtube')
    webbrowser.open('https://www.youtube.com/')
    
elif 'facebook' in voice_spoken:
    speak('opening facebook')
    webbrowser.open('https://www.facebook.com/')

elif 'instagram' in voice_spoken:
    speak('opening instagram')
    webbrowser.open('https://www.instagram.com/')    
    
elif 'play music' in voice_spoken or 'music' in voice_spoken:
    speak('Playing music')
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
    speak(f'Loading your results on {search}')      

elif 'open code' == voice_spoken or 'vs code'  in voice_spoken:
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
    speak(f'Loading your results on {search}')    

elif 'joke' in voice_spoken or 'jokes' in voice_spoken or 'funny' in voice_spoken or 'fun' in voice_spoken or 'bored' in voice_spoken:
    jokes_list = ['why did the scarecrow keep gettin promoted?..  Because he was outstanding in his field',
    'What did Batman say to Robin before they got in the car?..  Robin, get in the car.','What\'s red and shaped like a bucket?.... A blue bucket painted red.',
    'Did you hear about the two thieves who stole a calendar?..  They each got six months.','Why was the math teacher late to work?...  She took the rhombus.',
    'My daughter thinks I don\'t give her enough privacy....  At least that\'s what she wrote in her diary.','Why can\'t you trust an atom?.... Because they make up everything.',
    'The guy that invented the umbrella was gonna call it the brella....  But he hesitated.','Fun fact: Australia\'s biggest export is boomerangs. It\'s also their biggest import.',
    'Before the invention of the wheel…   everything was a drag!','What do you call it when Dwayne Johnson buys a cutting tool?... Rock pay for scissors.',
    'What did the duck say when she bought a lipstick?... Put it on my bill!','What did the little mountain say to the bigger mountain?...  Hi Cliff!',
    'Why are there gates around cemeteries?...  Because people are dying to get in!','Do you remember that joke I told you about my spine?... It was about a weak back!',
    'Today I gave my dead batteries away....  They were free of charge.','What does a zombie vegetarian eat?... "Graaaaaaaains!','What did the blanket say as it fell off the bed?... Oh sheet!',
    'Why shouldn\'t you write with a broken pencil?.. Because it\'s pointless!']

    speak(random.choice(jokes_list))
    
elif 'thanks' in voice_spoken or 'thank you' in voice_spoken or 'i like you' in voice_spoken:
    speak('I\'m glad you\'re happy')

else:
    string = voice_spoken.split() 
    search = ''
    for i in string:
        search += i
        search += '+'
    speak('Sorry I did not get that. But this is what I got for you on google')
    webbrowser.open(f'https://www.google.com/search?q={search}&oq={search}&aqs=chrome..69i57.4597j0j4&sourceid=chrome&ie=UTF-8')
    


    










