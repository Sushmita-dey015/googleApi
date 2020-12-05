import speech_recognition as sr
 
r=sr.Recognizer()
print('say something....')

with sr.Microphone() as m:
    audio=r.listen(m)
try:
    text=r.recognize_google(audio,language='bn')
    print(text)
except:
    print('Sorry,say again!!')
