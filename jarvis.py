import pyttsx3
import datetime
import speech_recognition as  sr
import wikipedia
import webbrowser
import os
from groq import Groq
from groq import Client


engin = pyttsx3.init('sapi5')
voices = engin.getProperty('voices')
# print(voices[1].id)
engin.setProperty('voice',voices[1].id)
def speak(audio):
    engin.say(audio)
    engin.runAndWait()
    
def wihMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Mornig...!")
    elif hour>=12 and hour<18:
        speak("Good After Noon ...!")
    else:
        speak("Good Night..!")
        
    speak("I am Jarvis How may i help You today..!")    
    
def ai(query):
    
    os.environ["GROQ_API_KEY"] = "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"  # Only for testing
    groq_api_key = os.getenv("GROQ_API_KEY")
    client = Client(api_key=groq_api_key)
    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": query
            },
            
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
   
    response_text = ""
    for chunk in completion:
        text = chunk.choices[0].delta.content or ""
        response_text += text  
        print(text, end="")  
    speak(response_text)
    return True
        
friendsay=""
def frd(query):
    global friendsay
    os.environ["GROQ_API_KEY"] = "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"  # Only for testing
    groq_api_key = os.getenv("GROQ_API_KEY")
    client = Client(api_key=groq_api_key)
    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": f"i say : {query} \n my friend say what just give me 1 ans "
            }
            
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    for chunk in completion:
        text = chunk.choices[0].delta.content or ""
        friendsay += text  
        print(text, end="")  
    
    return friendsay

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.. > ")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language='en-in')        
            print(f"User Said >> {query}\n")
        except Exception as e:
            # print(e)
            print("plese Say It Again..!!")
            return "None"
        return query
    
if __name__== '__main__':
    speak("Hy Name Is Jarvis How Can I Help You Today  ")
    words=["give me","write","make","generate"]
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
                speak('searching in wikipdia')
                query = query.replace("wikipedia" ,"")
                result = wikipedia.summary(query, sentences = 2)
                speak("according to wikipesia")
                print(result)
                speak(result)
                
        elif 'search in youtube ' in query:
                part=query.split("about",1)
                speak(f"searching about {part} on YouTube")
                webbrowser.open(f"https://youtube.com/{part}")
                
        elif 'open youtube' in query:
                speak("Opening Youtube")
                webbrowser.open("youtube.com")
        elif 'open github' in query:
                speak("Opening GitHub")
                webbrowser.open
                
        elif 'youtube music' in query:
                speak("Opening YouTube Music")
                webbrowser.open("https://music.youtube.com")
                
        elif 'open google' in query:
                speak("Opening Google")
                webbrowser.open("https://www.google.co.in")
                
        elif 'search in google' in query:
                parts = query.split("for",1)
                speak(f"Searching On Goole For {parts}")
                webbrowser.open(f"https://www.google.com/search?q={parts}")
                
        elif 'play music' in query:
                music_dir = 'D:\\Music\\'
                song = os.listdir(music_dir)
                print(song)
                os.startfile(os.path.join(music_dir,song[0]))
                
                
        elif 'time' in query:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                print(str_time)
                speak(f"Time is {str_time}")
                
            
        elif ' gta 5' in query:
                speak("Opening GTA 5")
                app_path = 'D:\\Grand Theft Auto V [Steam] (2015)\\Grand Theft Auto V\\GTA5.exe'
                os.startfile(app_path)   
                
            
            
        elif ' ' in query:
            if 'give me' in query:
                    ai(query)
                    
            else:
                    ans = frd(query)
                    speak(ans)
                    
                    
        elif 'make' in query:
                ai(query)
                
                
        elif 'write' in query:
                ai(query)
                
                
        elif 'how to make ' in query:
                ai(query)
                
            
                
        
    
            