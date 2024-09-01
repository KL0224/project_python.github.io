'''
sudo apt install python3-venv
python3 -m venv myenv
source myenv/bin/activate
'''
import pyttsx3
import speech_recognition # virtual
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)

    print("Robot:...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)

    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello master"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "president" in you:
        robot_brain = "Putin"
    elif "bye" in you:
        robot_brain = "Bye master"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I don't know"
    
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()


