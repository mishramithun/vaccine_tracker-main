from selenium import webdriver
from datetime import date
import time
import datetime
import requests
import json

driver = webdriver.Firefox(executable_path='geckodriver.exe')
code = "446"  # Khurdha, Odisha
# age = 45
telgram_id = "1834313143:AAE3YHTAUAovxWwM5WlWFRZ7j94u4QVvUbo"
channel_id = "-1001386313550"
today = date.today()
d1 = today.strftime("%d-%m-%Y")
# https://api.telegram.org/bot1834313143:AAE3YHTAUAovxWwM5WlWFRZ7j94u4QVvUbo/getUpdates


def check_sessions():
    try:
        driver.get(
            "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id=" + str(
                code) + "&date="+str(d1))

        json_data = json.loads(driver.find_element_by_id('json').text)

        session_str_18 = ""
        session_str_45 = ""
        for center in json_data['centers']:
            if len(center['sessions']) == 0:
                continue
            for session in center['sessions']:
                # if session['min_age_limit'] == age and session['available_capacity'] > 0:
                if session['available_capacity'] > 0:
                    if session['min_age_limit'] == 18:
                        if session_str_18 == "":
                            session_str_18 += "Above 18 Vaccine availability Details\n"
                            session_str_18 += "==================================\n"
                        session_str_18 += "Date: " + str(session['date']) + \
                                          "\nCenter: " + center['address'] + "\nPin: " + str(center['pincode']) + \
                                          "\nDose : " + str(session['available_capacity']) + "\n" + \
                                          "------------------------------\n"
                    elif session['min_age_limit'] == 45:
                        if session_str_45 == "":
                            session_str_45 += "Above 45 Vaccine availability Details\n"
                            session_str_45 += "==================================\n"
                        session_str_45 += "Date: " + str(session['date']) + \
                                          "\nCenter: " + center['address'] + "\nPin: " + str(center['pincode']) + \
                                          "\nDose : " + str(session['available_capacity']) + "\n" + \
                                          "------------------------------\n"
                    break
        print(datetime.datetime.now())
        if len(session_str_18) != 0:
            send_notif_to_telegram(session_str_18)
            print(session_str_18)
        if len(session_str_45) != 0:
            send_notif_to_telegram(session_str_45)
            print(session_str_45)
    except Exception as e:
        print(e)


def send_notif_to_telegram(content):
    resp = requests.get('https://api.telegram.org/bot' + str(telgram_id) + '/sendMessage?chat_id=' + str(channel_id) +
                        '&text=' + content)
    print(resp.status_code)


try:
    while True:
        check_sessions()
        time.sleep(30)
except Exception as e:
    print(e)
finally:
    driver.close()
