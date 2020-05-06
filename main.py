# import things
import requests


def main():
    while(True):
        action = input("\nWhat would you like to do?\n\t1) Search User\n\t2) Search Twitter\n\t3) Post Update\n\t4) Quit\n> ")
        if(action.isdigit() and int(action) < 7 and int(action) > 0):
            action = int(action)
            if(action == 1):
                handle = input("Which user would you like to look up?: ")
                while(True):
                    PARAMS = {'name': handle}
                    response = requests.get(url = URL, params = PARAMS)
                    if response.status_code == 200: # Status: OK
                        tweetthing = response.text.split('\"')
                        for x in tweething:
                        	x = x.replace(',','')
                        	x = x.replace('\n', '')
                        	print(x)
                    else:
                        print("Invalid request")
                    break
            elif(action == 2):
                word = input("What would you like to look up on twitter?: ")
                while(True):
                    PARAMS = {'word': word}
                    response = requests.get(url = URL2, params = PARAMS)
                    if response.status_code == 200:
                      tweetthing = response.text.split('\"')
                        for x in tweething:
                        	x = x.replace(',','')
                        	x = x.replace('\n', '')
                        	print(x)
                    else:
                        print("Invalid request")
                    break
            elif(action == 3):
            	print("Coming soon!")
            elif(action == 4)
            	print("Goodbye")
            	break
        else:
        	print('Not a valid option')

main()
