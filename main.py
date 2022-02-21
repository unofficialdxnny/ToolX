import sys
import os
import random
import django


            
### Code for dice

class bcolors:
    HEADER = '\033[32m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




banner = """

                                                                             
\033[1;94m                         ________    ________         ____            ____    _____           _____       _____ 
\033[1;94m                        /        \  /        \    ____\_  \__     ____\_  \__|\    \          \    \     /    / 
\033[1;94m                       |\         \/         /|  /     /     \   /     /     \\\    \          \    |   |    /  
\033[1;94m                       | \            /\____/ | /     /\      | /     /\      |\\    \          \    \ /    /   
\033[1;92m                       |  \______/\   \     | ||     |  |     ||     |  |     | \|    | ______   \    |    /    
\033[1;92m                        \ |      | \   \____|/ |     |  |     ||     |  |     |  |    |/      \  /    |    \   v2.0.2  
\033[1;96m                         \|______|  \   \      |     | /     /||     | /     /|  /            | /    /|\    \   
\033[1;96m                                  \  \___\     |\     \_____/ ||\     \_____/ | /_____/\_____/||____|/ \|____|  
\033[1;96m                                   \ |   |     | \_____\   | / | \_____\   | / |      | |    |||    |   |    |  
\033[1;96m                                    \|___|      \ |    |___|/   \ |    |___|/  |______|/|____|/|____|   |____|  
\033[1;96m                                                 \|____|         \|____|                                             

\033[1;36m [\033[1;37m+\033[1;36m]\033[1;94m Created By @unofficialdxnny \033[1;94m\033[1;33m\033[1;31m
              
          
"""



exit = """


\033[1;93m         _            _       _    _                   _             _       _        _          _      _                
\033[1;93m       /\ \         / /\    / /\ / /\                /\ \     _    /\_\    /\ \     /\_\       /\ \   /\_\              
\033[1;93m       \_\ \       / / /   / / // /  \              /  \ \   /\_\ / / /  _ \ \ \   / / /      /  \ \ / / /         _    
\033[1;93m       /\__ \     / /_/   / / // / /\ \            / /\ \ \_/ / // / /  /\_\\ \ \_/ / /      / /\ \ \\ \ \__      /\_\  
\033[1;93m      / /_ \ \   / /\ \__/ / // / /\ \ \          / / /\ \___/ // / /__/ / / \ \___/ /      / / /\ \ \\ \___\    / / /  
\033[1;93m     / / /\ \ \ / /\ \___\/ // / /  \ \ \        / / /  \/____// /\_____/ /   \ \ \_/      / / /  \ \_\\__  /   / / /   
\033[1;93m    / / /  \/_// / /\/___/ // / /___/ /\ \      / / /    / / // /\_______/     \ \ \      / / /   / / // / /   / / /    
\033[1;93m   / / /      / / /   / / // / /_____/ /\ \    / / /    / / // / /\ \ \         \ \ \    / / /   / / // / /   / / /     
\033[1;93m  / / /      / / /   / / // /_________/\ \ \  / / /    / / // / /  \ \ \         \ \ \  / / /___/ / // / /___/ / /      
\033[1;93m /_/ /      / / /   / / // / /_       __\ \_\/ / /    / / // / /    \ \ \         \ \_\/ / /____\/ // / /____\/ /       
\033[1;93m \_\/       \/_/    \/_/ \_\___\     /____/_/\/_/     \/_/ \/_/      \_\_\         \/_/\/_________/ \/_________/        

\033[1;96m    By @unofficialdxnny                                                                                                                            


"""

import keyboard as kb

kb.press('F11')


menu = """

1. Dice Menu                            6. Calculator
                       
2. Guess                                7. Encode In Hash
                
3. Password Generator                   8. Encode To Base64

4. IP Lookup                             

5. Instagram User Details

0. Exit

"""


while True:
   

    os.system("cls")
    print(banner)

    print("")
    
    print(menu)

    import time
    from datetime import datetime
       
    now = datetime.now()
    print(now.strftime("%m/%d/%Y %H:%M:%S"), end="\r", flush=True)
    time.sleep(1)

    print("")
    opt = int(input("Please Select An Option : "))
    print("\n")

    print("")

    if opt == 1:
        import time
        os.system('cls')
        print(banner)
        ds = int(input("What Is The Largest Number Of Your Dice : "))
        print("")
        dice = random.randint(1,ds)
        print(dice)
        import keyboard as kb
 
        time.sleep(5)
        

    elif opt == 2:
        import time
        os.system('cls')
        print(banner)
        print("")
        lower = int(input("What Is The Lower Number Your Number Is Between? : "))    
        print("")          
        upper = int(input("What Is The Upper Number Your Number Is Between? : "))
        print("")
        dice = random.randint(lower,upper)
        print(dice)
     
        time.sleep(5)

    elif opt == 3:
        os.system('cls')
        print(banner)
        print("")
        import time
        os.system('cls')
        print(banner)
        len = int(input("What Is The Required Length Of Your Password? : "))
        import secrets
        password = secrets.token_urlsafe(len)
        print(password)
      
       
        time.sleep(5)
        
    
    elif opt == 4:
        os.system('cls')
        print(banner)
        print("")
        import time
        import requests
        import json

        # IP address to test
        ip_address = input("What Is The Victims IP Address? : ")
        print("")

        # URL to send the request to
        request_url = 'https://geolocation-db.com/jsonp/' + ip_address
        # Send request and decode the result
        response = requests.get(request_url)
        result = response.content.decode()
        # Clean the returned string so it just contains the dictionary data for the IP address
        result = result.split("(")[1].strip(")")
        # Convert this data into a dictionary
        result  = json.loads(result)
        print("")
        print(result)
      
        
        time.sleep(5)

    elif opt == 5:
        os.system('cls')
        print(banner)
        print("")
        import time
        from instagramy import InstagramUser
        # user input
        name = input("Enter The Name Of User : ")
        print("")
        # instance of instagram user
        user = InstagramUser(name)
        # total followers
        followers = user.number_of_followers
        print('Total followers:', followers)
        # total followings
        following = user.number_of_followings
        print('Total followings:',following)
        # total number of posts
        posts = user.number_of_posts
        print('Total posts:',posts)
        # bio description
        bio = user.biography
        print('Bio:\n', bio)
        # link in bio
        link_in_bio = user.website
        print('Link in Bio:', link_in_bio)

        check = int(input("Check For Yourself? (1/2) : "))
        if check == 1:
            import webbrowser as browser
            browser.open("https://instagram.com/{name}")
        elif check == 2:
            print("Going To Main Menu")
          
     
        
        time.sleep(5)
    
    elif opt == 6:
        # Program make a simple calculator

# This function adds two numbers
        def add(x, y):
            return x + y

# This function subtracts two numbers
        def subtract(x, y):
            return x - y

# This function multiplies two numbers
        def multiply(x, y):
            return x * y

# This function divides two numbers
        def divide(x, y):
            return x / y


        print("Select operation.")
        print("")
        print("1.Add")
        print("")
        print("2.Subtract")
        print("")
        print("3.Multiply")
        print("")
        print("4.Divide")
        print("")
        while True:
    # take input from the user
            choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(num1, "+", num2, "=", add(num1, num2))

                elif choice == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))

                elif choice == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))

                elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
                time.sleep(5)


    
    elif opt == 7:
        import hashlib
        import time
        my_string = input("What Is The Message You Would Like To Encode? : ")
        hash_object = hashlib.sha512(b'Hello World')
        hex_dig = hash_object.hexdigest()
        print(hex_dig)
        time.sleep(5)



    elif opt == 8:
        import base64
        import time

        message = input("What Is Your Text Message? : ")
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        

        print(base64_bytes)
        time.sleep(5)



    



    elif opt == 0:
        import sys
        os.system('cls')
        print(exit)
        import webbrowser as browser
        browser.open("https://github.com/unofficialdxnny")
        browser.open("https://instagram.com/unofficialdxnny")
        browser.open("https://discord.gg/tT2cS8c44p")
        sys.exit()
