
try:
    # from corefunction.textToSpeech import speak
    # from corefunction.speechToText import take_command
    from wordContain import isContain
    # from login_page import auto_login
    from datetime import *
    # this module is use to request on server.
    import requests
    # This module use to fetch data from wikipedia
    import wikipedia
    # This module is use to open web browser
    import webbrowser
    # This module is use to work on system os
    import os
    import time
    # import calculator
    # This module is used for Test internet speed
    import speedtest   #pip install speedtest-cli
    # This module tells us that which os we are using basically it tells all the information about our os
    import platform
    # This module is use to automate tasks
    import pyautogui
    import psutil
    import pyjokes
    from googlesearch import search
    import random
    import tkinter as tk
    from PIL import Image, ImageTk
    print("Home module imported")
except Exception as e:
    print(e)

############################################ Weather API #########################################################


def whoAmI():
    # data = auto_login()
    # callme = "sir"
    # if data[1]=="female":
    #     callme = "ma'am"
    # speak(f"hello {callme} you are {data[0]} you are authorize person who can access me and my settings")
    return (f"hello sir you are authorize person who can access me and my settings")

def currentDay ():
    """
    This function tells current day.
    """

    try:
        today = date.today().strftime("%A")
        return (f"Today's day is : {today}")
    except Exception as e:
        print(e)

    today = date.today().strftime("%A")
    speak(f"Today's date is : {today}")

    
def currentDate():
    """
    This function tells current date.
    """

    try:
        date1 = date.today()
        return (date1)
    except Exception as e:
        print(e)


def jokes():
    """
    This function tells joke 
    using pyjoke module.
    """

    # data = auto_login()
    # callme = "sir"
    # if data[1]=="female":
    #     callme = "ma'am"



    try:
        My_joke = pyjokes.get_joke(language="en", category="all")  
        # speak(My_joke)
        return My_joke
        # query=take_command().lower()
        # if "haha " in query or "good one" in query:
        #     speak(f"thanks {callme} should i tell you one more joke")
        #     query = take_command().lower()
        #     if "yeah" in query:
        #         jokes()
        #     else :
        #         return  
    except Exception as e:
        print(e)

def batteryPercantage():
    """
    This function uses psutil
    module to get battery percantage
    """

    try:
        battery = psutil.sensors_battery()
        if battery.percent == 100:
            speak("battery is fully charged")
        else:
            speak(f"battery is {battery.percent} percent charge") 
        if battery.power_plugged == 'true':
            speak("battery is charging")
        else:
            speak("battery is not charging")          
    except Exception as e:
        print(e)        

def fullSystemDetail():
    pass

def osName ():
    """
    This function tells that which 
    operating system  we are using now.
    """
    try:
        os = platform.system()
        speak(f"you are using {os} operating system")
    except Exception as e:
        print(e)


def take_screenshot():
    """
    This function takes a screenshot
    using pyautogui and save it in 
    screenshot directory.
    """
    try:

        isdir = os.path.isdir("screenshot")
        if isdir==True:
            myScreenshot = pyautogui.screenshot()
            speak("taking screenshot")
            lst = os.listdir('screenshot')
            lstLength = int(len(lst))
            path = f"screenshot\\screenshot{lstLength+1}.png"
            myScreenshot.save(path)
            speak("Screenshot taken")
            speak("do you want to see the taken screenshot")
            query = take_command()
            if isContain (query,['yes','yeah','hmm','sure','okay','of course','ok']):
                show_screenshot()
        else :
            os.mkdir("screenshot")
            screenshot()
    except Exception as e:
        print(e)
        speak("Can not take screenshot")

def show_screenshot():
    data = auto_login()
    callme = "sir"
    if data[1]=="female":
        callme = "ma'am"
    if os.path.isdir("screenshot"):
        screenshot_list = os.listdir("screenshot")
        list_length = (len(screenshot_list))
        if list_length !=0:
            screenshot = (screenshot_list[list_length-1])
            os.startfile(f"screenshot\\{screenshot}")
        else :
            speak(f"sorry {callme} but there is no screenshot you have taken.")
            time.sleep(.5)
            speak("if you say than i can take a screenshot for you ")
            speak("do you want to take screenshot ")
            query = take_command().lower()
            if isContain(query,["yes","yeah","okay","of course","sure"]):
                take_screenshot()
    else :
        speak(f"sorry {callme} but there is no screenshot avaliable.")
        time.sleep(.5)
        speak("if you say than i can take a screenshot for you ")
        speak("do you want to take a screenshot ")
        query = take_command().lower()
        if isContain(query,["yes","yeah","okay","of course","sure"]):
            take_screenshot()

def screenshot(query):
    data = auto_login()
    callme = "sir"
    if data[1]=="female":
        callme = "ma'am"
    if "take" in query and "screenshot" in query:
        take_screenshot()
    elif "show" in query and "screenshot" in query :
        show_screenshot()
    else:
        speak(f"{callme}i don't understant what operation do you want to perform on the screenshot")
        speak("to take a screenshot just say take screenshot and i will take it for you")
        speak("and to see a screenshot just say show screenshot")

def speedTest():
    """
    This function used to fetch
    the internet speed.
    """
    try:
        print("In speed Test function.")
        st = speedtest.Speedtest()
        downloadSpeed = st.download()
        downloadSpeed = downloadSpeed/1048576   #for converting bytes in Kbytes we have to divied by 1024 and then To convert from Kbyte to Mbyte we have to divide by 1024 then we can multiply 1024*1024 = 1048576  
        downloadSpeed = "{:.2f}".format(downloadSpeed)
        print("Reached Here")
        return "50kbps"
    except Exception as e:
        print(f'Getting an Exception {e}')
        return "exception"

def current_time ():
    """
    This function tells the 
    current time using datetime module.
    """
    try:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        # speak(f"The time is {current_time}")
        return current_time
    except Exception as e:
        print(e)


    speak("ok sir trying to fetch download speed")
    st = speedtest.Speedtest()
    downloadSpeed = st.download()
    downloadSpeed = downloadSpeed/1048576   #for converting bytes in Kbytes we have to divied by 1024 and then To convert from Kbyte to Mbyte we have to divide by 1024 then we can multiply 1024*1024 = 1048576  
    downloadSpeed = "{:.2f}".format(downloadSpeed)
    speak(f"{downloadSpeed} Megabyte per second")


def news():
    """
    This function use news api and fetch 
    10 latest news and speak news.
    """

    try:
        newsUrl = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=9f17ea0361774831bb8906e2426c1e22'
        json_data = requests.get(newsUrl).json()
        arr = []
        for i in range(0, 10):
            title = json_data['articles'][i]['title']
            description = json_data['articles'][i]['description']
            # print(f"{i + 1} :-{title}")
            # print(f"        {description}")
            arr.append(f'{i+1}*{title} :-- {description}')
    except Exception as e:
        print(e)
    print(arr)
    return (arr)
def weather_data():
    """
        This function use a API. This function send request to open weather site
        fetch data from that site a speak.
    """
    
    data = auto_login()
    callme = "sir"
    if data[1]=="female":
        callme = "ma'am"
    api_address = "http://api.openweathermap.org/data/2.5/weather?appid=40b98f754f6b23dc8725fd2cfc6d9769&q="
    try:

        
        url = api_address + "gorakhpur"

        url = api_address + "gorakhpur"  # in url we add a place address to get particular location weather data



        json_data = requests.get(url).json()
        weather_data = json_data['weather'][0]['main']
        temp_data = json_data['main']['temp']
        temp_data = int(temp_data - 273.15)
        speak(f"Hello {callme} the weather is {weather_data} and the temerature is {temp_data} degree celsius")
        print(f"Hello {callme} the weather is {weather_data} and the temerature is {temp_data} degree celsius")
    
    except Exception as e:
        print(e)




################################################### Greet Function #############################################
def greet():
    """
    This Function used for greeting

    """
    try:
        hour = int(datetime.now().hour)
        today = date.today()
        curr_day = today.strftime("%B %d , %Y")
        now = datetime.now()
        curr_time = now.strftime("%H %M")

        if hour >= 3 and hour <= 11:
            return (f"Hello good morning  It's {curr_day} and the time is {curr_time}")


        elif hour >= 12 and hour <= 18:
            return ("Hello Good After noon ")


        elif hour > 18 and hour <= 24:
            return ("Hello Good evening ")

        else:
            return ("Hello Good night")
    except Exception as e:
        print(e)

######################################### Who are You ######################################################

def whoareyou():
    """
    This function tells about that who is this 
    """
    data = auto_login()
    callme = "sir"
    if data[1]=="female":
        callme = "ma'am"
    try:
        speak(f"Hello {callme}")
        time.sleep(1)
        speak("i am edith your personal assistant")
        speak("would you like to know what can i do")
        query = take_command.lower()
        if 'yes' in query or 'yeah' in query or 'sure' in query:
            features()
    except Exception as e:
        print(e)

def shutdown():
    """
    First this function check os name using platform
    module and then shutdown the system.
    """
    try:
        os = platform.system()
        os = os.lower()
        if os =='windows':
            os.system("shutdown /s")
        elif os =='linux':
            os.system()
        elif os =='macos':
            os.system()
        else:
            speak("Sorry but it can only used in windows , linux , macos")
    except Exception as e:
        print(e)

def restart():
    """
    This function works as shutdown function
    first it checks os name and then restart
    the system.
    """
    try:
        os = platform.system()

        os = os.lower()
        
        if os =='windows':
            os.system("shutdown/r")
        elif os =='linux':
            os.system()
        elif os =='macos':
            os.system()
        else:
            speak("Sorry but it can only used in windows , linux , macos")
    except Exception as e:
        print(e)

def open_website(query):
    """
    This function open any website this 
    function uses search function which is 
    in the google search module.
    """
    try:
        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            webbrowser.open(j)
    except Exception as e:
        print(e)

def features():
    data = auto_login()
    callme = "sir"
    if data[1]=="female":
        callme = "ma'am"
    try:
        speak(f"hello {callme}, i can perform many tasks such as calculating numbers or opening a website for you i can play music for you")
        speak("I can automate some task for you ")
    except Exception as e:
        print(e)

def makeAnote():
    try:
        data = auto_login()
        callme = "sir"
        if data[1]=="female":
            callme = "ma'am"
        if os.path.isdir("notes"):
            lst = os.listdir("notes")
            lstLength = int(len(lst))
            file_path = f"notes\\note{lstLength+1}.txt"
            with open (file_path,"a") as file:
                def write_note():
                    speak(f"Okk {callme} tell me what to write")
                    # query = input("Enter query :")
                    query = take_command()
                    file.write(query+" ")
                    # print("Want to add more sir :")
                    speak(f"Want to add more {callme} :")
                    # query = input("More ??")
                    query = take_command()
                    if isContain (query,['yes','yeah','hmm','sure','okay','of course','ok']):
                        write_note()
                    else:
                        print(f"Done {callme}")
                        speak(f"Done {callme}")
                        speak(f"saving note {callme}")
                        speak("want to see your notes")
                        query = take_command().lower()
                        if isContain (query,['yes','yeah','hmm','sure','okay','of course','ok']):
                            speak(f"{random.choice['opening notes','showing note']}")
                            show_note()

                write_note()
        else:
            os.makedirs("notes")
            makeAnote()
    except Exception as e:
        print(e)

def show_note():
    data = auto_login()
    callme = "sir"
    if data[1]=="female":
        callme = "ma'am"
    if os.path.isdir("notes"):
        note_list = os.listdir("notes")
        list_length = (len(note_list))
        if list_length !=0:
            note = (note_list[list_length-1])
            os.startfile(f"notes\\{note}")
        else :
            speak(f"sorry {callme} but there is no notes avaliable in notebook.")
            time.sleep(.5)
            speak("if you say than i can create note for you ")
            speak("do you want to create note ")
            query = take_command().lower()
            if isContain(query,["yes","yeah","okay","of course","sure"]):
                makeAnote()
    else :
        speak(f"sorry {callme} but there is no notes avaliable in notebook.")
        time.sleep(.5)
        speak("if you say than i can create note for you ")
        speak("do you want to create note ")
        query = take_command().lower()
        if isContain(query,["yes","yeah","okay","of course","sure"]):
            makeAnote()

def note(query):
    if "note" in query and "make" in query or "create" in query:
        makeAnote()
    elif "note" in query and "show" in query:
        show_note()
    else:
        speak("I don't understant what do you want to perform on the note")
        speak("to create a note just say make a note or create a note")
        speak("and to see a note just say show note")

def bye():
    data = auto_login()
    callme = "sir"
    if data[1]=="female":
        callme = "ma'am"
    exit_greetings = ["goodbye","exiting","okk going to sleep","okk bye"]
    speak(f"{random.choice(exit_greetings)} {callme}")
    print(f"{random.choice(exit_greetings)} {callme}")
    quit()

def myBirthday():
    try:
        root = tk.Tk()
        image1 = Image.open("resources\\images\\birthdayImg.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(image=test)
        label1.pack()
        root.after(10000,lambda:root.destroy())
        root.mainloop()
    except Exception as e:
        print(e)

    speak("Hello sir")
    time.sleep(1)
    speak("i am edith your personal assistant")
    speak("would you like to know what can i do")
    query = take_command.lower()
    if 'yes' in query or 'yeah' in query or 'sure' in query:
        features()

def shutdown():
    """
    First this function check os name using platform
    module and then shutdown the system.
    """
    os = platform.system()
    os = os.lower()
    if os =='windows':
        os.system("shutdown /s")
    elif os =='linux':
        os.system()
    elif os =='macos':
        os.system()
    else:
        speak("Sorry but it can only used in windows , linux , macos")

def restart():
    """
    This function works as shutdown function
    first it checks os name and then restart
    the system.
    """
    os = platform.system()

    os = os.lower()
    
    if os =='windows':
        os.system("shutdown/r")
    elif os =='linux':
        os.system()
    elif os =='macos':
        os.system()
    else:
        speak("Sorry but it can only used in windows , linux , macos")


def open_website(query):
    """
    This function open any website this 
    function uses search function which is 
    in the google search module.
    """
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
    	webbrowser.open(j)

def features():
    speak("hello sir, i can perform many tasks such as calculating numbers or opening a website for you i can play music for you")
    speak("I can automate some task for you ")



if __name__ == '__main__':
    # bye()
    pass
