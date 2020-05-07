# EE 250 Final Project
Spring 2020
Final Project for Janeline Wong and Edison Siu

About the project: Kid friendly Twitter provides a physical interface for kids to view tweets without any swear words.

Major links:
Github: https://github.com/JanelineWong/tweetybird (For both server and testcode)
Access point: https://morning-peak-20774.herokuapp.com/

Video links:
Main Video:
https://urldefense.com/v3/__https://youtu.be/TERKubGkOas__;!!LIr3w8kk_Xxm!5nBwkWfO41mfM8DkOdJEzEonP08c2qS9rSPy6Z7GzJgzUeHe6mM7M9qmKkekrvE$

LCD video:
https://urldefense.com/v3/__https://youtu.be/HQmCOTJeMiI__;!!LIr3w8kk_Xxm!5nBwkWfO41mfM8DkOdJEzEonP08c2qS9rSPy6Z7GzJgzUeHe6mM7M9qmdjL1fLo$

Heroku:
https://urldefense.com/v3/__https://youtu.be/IysS3UAXBSA__;!!LIr3w8kk_Xxm!5nBwkWfO41mfM8DkOdJEzEonP08c2qS9rSPy6Z7GzJgzUeHe6mM7M9qm1q6kxxk$

Terminal:
https://urldefense.com/v3/__https://youtu.be/XPSjkHn2Tco__;!!LIr3w8kk_Xxm!5nBwkWfO41mfM8DkOdJEzEonP08c2qS9rSPy6Z7GzJgzUeHe6mM7M9qmLGeArrU$

Instructions to compile: Everything is hosted in Heroku as a docker, but to run the server locally you could theoretically:
1. Clone the repository into a directory
2. In a virtual environment, type: pip install -r requirements.txt
3. Insert local authorization keys for Twitter API in tweettweet.py
4. python app.py
5. go to localhost: http://127.0.0.1/5000

To test the endpoint in the Raspberry Pi: 
1. sudo apt-get update
2. sudo apt-get install build-essential python-dev python-smbus python-pip
3. sudo pip3 install RPi.GPIO
4. sudo python3 setup.py install
5. python3 main_lcd.py

To test the endpoint without an lcd, in a terminal window:
python3 main.py

Libraries used:
RPLCD
Tweepy
Flask
os
json

