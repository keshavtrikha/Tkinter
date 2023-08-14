import tkinter as tk
from tkinter import *
from tkinter import messagebox

def show_message(message):
    messagebox.showinfo("Message", message)

def Google_clicked():
    show_message("Search your query through Google")
    from googlesearch import search
    query =input("Enter your query here:")
    for i in search(query,tld="com",num=5,stop=10,pause=2):
        print(i)

def Geolocation_clicked():
    show_message("Get your location coordinates")
    from geopy.geocoders import Nominatim

# Initialize the geolocator
    geolocator = Nominatim(user_agent="John")

# Get coordinates for a specific location
    location = geolocator.geocode("Delhi")
    latitude = location.latitude
    longitude = location.longitude

    print(f"Latitude of input place: {latitude},\nLongitude  of input place: {longitude}")

def speech_clicked():
    show_message("Convert your speech into text ")
    import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

    r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable

    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        print("Text: "+r.recognize_google(audio_text))
    except:
         print("Sorry, I did not get that")

def open_insta_clicked():
    show_message("Instabot Clicked!")
    from instabot import Bot
    bot = Bot()

#login
    bot.login(username = ("username"),password = ("password"))

#upload photo
    bot.upload_photo("yoda.jpeg", caption="biscuit eating baby")

#following
    bot.follow("elonrmuskk")

#send a message
    bot.send_message("Hello", ['user1','user2'])

#get follower info
    my_followers = bot.get_user_followers("dhavalsays")
    for follower in my_followers:
        print(follower)

    bot.unfollow_everyone()


def whatsapp_clicked():
    show_message("Send your whatsapp messages")
    import pywhatkit
    pywhatkit.sendwhatmsg('+91**********','Hello there',12,19)


def open_calculator_clicked():
    show_message("open calculator Clicked!")
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
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
    # take input from the user
     choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
     if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

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
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")

def face_clicked():
    show_message("Face detection opened")
    import cv2

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera (usually your laptop's built-in camera)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    
        cv2.imshow('Frame', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
     

    cap.release()
    cv2.destroyAllWindows()


def open_control_panel_clicked():
    show_message("Here is your control panel")
    import os

    def open():
        os.system('cmd /c control') # thi is what will help you

    root =Tk()
    root.geometry('400x400')
    b = Button(root, text='open control panel', command = (open)).place(x=200, y=200) # you can choose your own position 

    root.mainloop()

def open_exit_clicked():
    show_message("open exit Clicked!")

def exit_application():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Python Menu Example")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
root.config(bg="blue")

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0,bg='yellow')
menu_bar.add_cascade(label='Exit',menu=file_menu)
file_menu.add_command(label="Exit", command=exit_application)

# Create a Buttons menu
buttons_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu options", menu=buttons_menu)
buttons_menu.add_command(label="Google search", command=Google_clicked)
buttons_menu.add_command(label="Geolocation", command=Geolocation_clicked)
buttons_menu.add_command(label="Speech to text", command=speech_clicked)
buttons_menu.add_command(label="Instabot", command=open_insta_clicked)
buttons_menu.add_command(label="Whatsapp", command=whatsapp_clicked)
buttons_menu.add_command(label="Calculator", command=open_calculator_clicked)
buttons_menu.add_command(label="Face detection", command=face_clicked)
buttons_menu.add_command(label="Control Panel", command=open_control_panel_clicked)
buttons_menu.add_command(label="Exit", command=open_exit_clicked)

# Create buttons in the main window
button_frame = tk.Frame(root)
button_frame.pack(padx=40, pady=40)

button1 = tk.Button(button_frame, text="Google search", command=Google_clicked,fg="red")
button1.pack(fill=tk.X, padx=10, pady=5)

button2 = tk.Button(button_frame, text="Geo location", command=Geolocation_clicked,fg="red")
button2.pack(fill=tk.X, padx=10, pady=5)

button3 = tk.Button(button_frame, text="Speech to text", command=speech_clicked,fg="red")
button3.pack(fill=tk.X, padx=10, pady=5)

button4 = tk.Button(button_frame, text="Instabot", command=open_insta_clicked,fg="red")
button4.pack(fill=tk.X, padx=10, pady=5)

button5 = tk.Button(button_frame, text="Whatsapp", command=whatsapp_clicked,fg="red")
button5.pack(fill=tk.X, padx=10, pady=5)

button6 = tk.Button(button_frame, text="Calculator", command=open_calculator_clicked,fg="red")
button6.pack(fill=tk.X, padx=10, pady=5)

button7 = tk.Button(button_frame, text="Face Detection", command=face_clicked,fg="red")
button7.pack(fill=tk.X, padx=10, pady=5)

button8 = tk.Button(button_frame, text="Control Panel", command=open_control_panel_clicked,fg="red")
button8.pack(fill=tk.X, padx=10, pady=5)

button9 = tk.Button(button_frame, text="Exit", command=open_exit_clicked,fg="red")
button9.pack(fill=tk.X, padx=10, pady=5)

# Start the GUI event loop
root.mainloop()
