import pyttsx3  
# initialize Text-to-speech engine  
engine = pyttsx3.init()  
# convert this text to speech
str="Type word to say any thing "
print(str)
while (True):
    text = input()
    if (text=="q"):
        break        
    
    engine.say(text)  
    # play the speech  
    engine.runAndWait()  