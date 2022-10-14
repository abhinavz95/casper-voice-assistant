import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

print("Initializing casper")

MASTER = "abhinav sir"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour >= 0 and hour < 12:
        speak("good morning" + MASTER)

    elif hour >= 12 and hour < 18:
        speak("good afternoon" + MASTER)

    else:
        speak("good evening" + MASTER)

    speak("i am casper voice assistent .how may i help you today?")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("is there anything else, that can i help with? ")   
        return "None"
    return query



if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower()

        #logic fortasks
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'open youtube' in query.lower():
             url = "youtube.com"
             chrome_path = 'C://Program Files//Google//Chrome//Application//chrome.exe %s'
             webbrowser.get(chrome_path).open(url)

        elif 'open google' in query.lower():
             url = "google.com"
             chrome_path = 'C://Program Files//Google//Chrome//Application//chrome.exe %s'
             webbrowser.get(chrome_path).open(url)

        elif 'open reddit' in query.lower():
             url = "reddit.com"
             chrome_path = 'C://Program Files//Google//Chrome//Application//chrome.exe %s'
             webbrowser.get(chrome_path).open(url)

        elif 'open whatsapp'in query.lower():
            url = "web.whatsapp.com"
            chrome_path = 'C://Program Files//Google//Chrome//Application//chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        

             
    

        