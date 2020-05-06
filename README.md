# EE 250 Final Project
Spring 2020
Final Project for Janeline Wong and Edison Siu

About the project: Kid friendly Twitter provides a physical interface for kids to view tweets without any swear words.

Major links:
Server Github: https://github.com/JanelineWong/tweetybird
Access point: https://morning-peak-20774.herokuapp.com/

Instructions to compile: Everything is hosted in Heroku as a docker, but to run the server locally you could theoretically:
1. Clone the repository into a directory
2. In a virtual environment, type: pip install requirements.txt
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

