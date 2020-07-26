from playsound import playsound
import requests
import time
old = ""
while True:
    r = requests.get('https://nextpatient.co/p/1132/schedule-widget-compact-appointments.html')

    if "Sat" not in r.text:
        if not old == r.text:
            old = r.text
            playsound("audio.mp3")
    print(r.text)
    time.sleep(1)
