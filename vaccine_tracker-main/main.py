from selenium import webdriver
from datetime import date
import time
import datetime
import requests
import json

driver = webdriver.Firefox(executable_path='geckodriver.exe')
code = "457"  # Cuttack, Odisha
age = 18
telgram_id="1773310075:AAHJ8lKOo1oE5z3pmPuHjbCXE-NKoY8Gfc0"
channel_id="-1001227081973"
today = date.today()
d1 = today.strftime("%d-%m-%Y")

#https://api.telegram.org/bot1773310075:AAHJ8lKOo1oE5z3pmPuHjbCXE-NKoY8Gfc0/getUpdates

def check_sessions():
    try:
        driver.get(
            "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id=" + str(
                code) + "&date="+str(d1))

        json_data = json.loads(driver.find_element_by_id('json').text)

        session_str = ""
        for center in json_data['centers']:
            if len(center['sessions']) == 0:
                continue
            for session in center['sessions']:
                if session['min_age_limit'] == age and session['available_capacity'] > 0:
                    session_str += "Center: " + center['address'] + "," + str(center['pincode']) + " " + " Dose : " + str(
                        session['available_capacity']) + "\n"
                    break
        print(datetime.datetime.now())
        if len(session_str) != 0:
            send_notif_to_telegram(session_str)
            print(session_str)
    except Exception as e:
        print(e)


def send_notif_to_telegram(content):
    resp = requests.get(

    'https://api.telegram.org/bot' + str(telgram_id) + '/sendMessage?chat_id=' + str(channel_id) + '&text=' + content)
    print(resp.status_code)
try:
    while True:
        check_sessions()
        time.sleep(30)
except Exception as e:
    print(e)
finally:
    driver.close()
