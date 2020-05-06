# import things
import requests
import socket
import time
from RPLCD.gpio import CharLCD
from RPi import GPIO

lcd = CharLCD(pin_rs = 26, pin_e=19, pin_backlight=15,pins_data=[13, 6, 5, 11],
              numbering_mode=GPIO.BCM,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              compat_mode = True,
              auto_linebreaks=True)

URL = "https://morning-peak-20774.herokuapp.com/handle"
URL2 = "https://morning-peak-20774.herokuapp.com/search"

framebuffer = [
    'Hello!',
    '',
]

def write_to_lcd(lcd, framebuffer, num_cols):
    """Write the framebuffer out to the specified LCD."""
    lcd.home()
    for row in framebuffer:
        lcd.write_string(row.ljust(num_cols)[:num_cols])
        lcd.write_string('\r\n')

def loop_string(string, lcd, framebuffer, row, num_cols, delay=0.2):
    padding = ' ' * num_cols
    s = padding + string + padding
    for i in range(len(s) - num_cols + 1):
        framebuffer[row] = s[i:i+num_cols]
        write_to_lcd(lcd, framebuffer, num_cols)
        time.sleep(delay)
def main():
    while(True):
        action = input("\nWhat would you like to do?\n\t1) Search User\n\t2) Search Twitter\n\t3) Post Update\n\t4) Quit\n> ")
        if(int(action) < 7 and int(action) > 0):
            action = int(action)
            if(action == 1):
                handle = input("Which user would you like to look up?: ")
                while(True):
                    PARAMS = {'name': handle}
                    response = requests.get(url = URL, params = PARAMS)
                    print(response)
                    if response.status_code == 200: # Status: OK
                        tweetthing = response.text.split('\"')
                        for x in tweetthing:
                            x = x.replace(',','')
                            x = x.replace('\n','')
                            x = x.replace('[', '')
                            x = x.replace(']','')
                            print(x)
                            framebuffer = [
                                handle,
                                '',
                            ]
                            # loop_string(x, lcd, framebuffer, 1, 16)
                        time.sleep(1)
                    else:
                        print("Invalid request")
                    break
            if(action == 2):
                word = input("What would you like to look up on twitter?: ")
                while(True):
                    PARAMS = {'word': word}
                    response = requests.get(url = URL2, params = PARAMS)
                    if response.status_code == 200: # Status: OK
                        tweetthing = response.text.split('\"')
                        for x in tweetthing:
                            x = x.replace(',','')
                            x = x.replace('\n','')
                            x = x.replace('[', '')
                            x = x.replace(']','')
                            print(x)
                            framebuffer = [
                                word,
                                '',
                            ]
                            # loop_string(x, lcd, framebuffer, 1, 16)
                        time.sleep(1)
                    else:
                        print("Invalid request")
                    break
            if(action == 3):
                print("Pending Twitter approval!!!")
            if(action == 4)
                print("GOODBYE")
                break
# Driver code 
if __name__ == '__main__': 
    main()
    GPIO.cleanup() # cleanup all GPIO
