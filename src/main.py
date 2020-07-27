from playsound import playsound
import requests
import time
old = ""
while True:
    try:
        r = requests.get('https://nextpatient.co/p/1132/schedule-widget-compact-appointments.html')

        if "Mon" in r.text or ("Tue" in r.text and "9" in r.text):
            if not old == r.text:
                old = r.text
                playsound("audio.mp3")
        print(r.text)
        time.sleep(1)
        print()
    except BaseException as e:
        print("ERROR")
        print(e)
        playsound("bad.mp3")

