Aim of the project is to setup alert for vaccine for a district. Script will send real time alert to Telegram public channel. Then user can go on cowin portal and book the appointment.

0. Download codebase zip file. or git clone the project.
``` git clone https://github.com/paragsanjay/vaccine_tracker.git```

1. Install Python
Download & Install python from https://www.python.org/downloads/
verify if python is installed on your system.
```python -v```

2. Install Firefox 
Download & Install latest firefox from https://www.mozilla.org/en-US/firefox/new/

3. Download geckdriver
Download geckdriver from https://github.com/mozilla/geckodriver/releases as per your machine.
extract the file and put geckdriver file into project directory.

4. run main.py to test
```python main.py```
You will see firefox opened automatically on your system. it will hit cowin public API for results.
If you faced any issues till this point then contact Parag Mhatre (8793748832)

5. Create Telegram Channel
Download and install Telegram on your desktop or mobile.
Create telegram public channel
![alt text](https://i.ibb.co/BzC2hLB/telegram1.png)

6. Put Chnnel name as in following format
```Raigad Under 45 Vaccine Tracker``` - You can replace ```Raigad``` with disctrict for which you are configuring. ex: Pune

7. Select Public channel and put link of channel as ```raigad_under_45_vaccine_tracker```

8. Next, Click Skip 

9. Now lets create a bot