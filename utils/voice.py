import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

""" RATE"""
engine = pyttsx3.init()  # getting details of current speaking rate                       
rate = engine.getProperty('rate')  #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female & 0 for male

