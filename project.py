import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
import pygame
import sys
import threading
import time




def create_battery(canvas, x, y, width, height, percentage):
    # Draw battery outline
    canvas.create_rectangle(x, y, x + width, y + height, outline='black', width=2)
    
    # Draw battery level
    levels = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    colors = ['red', 'orange', 'yellow', 'yellowgreen', 'green']
    
    num_levels = len(levels)
    level_width = width / num_levels
    
    for i in range(num_levels):
        if percentage >= levels[i]:
            fill_color = colors[i % len(colors)]
        else:
            fill_color = 'white'
        
        canvas.create_rectangle(x + i * level_width + 2, y + 2, 
                                x + (i + 1) * level_width - 2, y + height - 2, 
                                fill=fill_color, outline='')


def is_playstation_controller_connected():
    """Check if a PlayStation controller is connected."""
    pygame.init()
    pygame.joystick.init()

    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        return False
    else:
        return True
 


        

class Page3:
    def __init__(self):
        self.Root = Toplevel()
        self.Root.attributes('-fullscreen', True)
        self.Root.resizable(False, False)
        self.Root.title("SUBMARINE_CONTROL")
        self.Root.iconbitmap('D:\\zyad\\bionic hand\\application\\image\\images.ico')
        img1 = PhotoImage(file=r"C:\Users\zyadt\OneDrive\Desktop\image\image1.png")
        l3 = Label(self.Root, image=img1)
        l3.image = img1  # Reference to the image object
        l3.grid()

        self.cap = None

        B = Button(self.Root, text="Start", bg='skyblue', font=('tajawal', 15), width=20, height=2, command=self.start_camera)
        B.place(x=900, y=650)
        B2 = Button(self.Root, text="Stop", bg='skyblue', font=('tajawal', 15), width=20, height=2, command=self.close_camera)
        B2.place(x=1200, y=650)
        B4 = Button(self.Root, text="Close", bg='skyblue', font=('tajawal', 15), width=20, height=2, command=quit)
        B4.place(x=1050 ,y=750)

        self.f1 = LabelFrame(self.Root)
        self.f1.place(x=0, y=0)
        self.L1 = Label(self.f1)
        self.L1.pack()
        # Add canvas for battery indicators

        speed_button = Button(self.Root, text="Speed", bg='skyblue', font=('tajawal', 15), width=20, height=2, command=self.start_camera)
        speed_button.place(x=0, y=600)
        self.speed_level = Canvas(self.Root, width=300, height=50, bg='white', highlightthickness=0)
        self.speed_level.place(x=280, y=605)
        create_battery(self.speed_level, 0, 0, 300, 50, 70)


        pressure_button = Button(self.Root, text="Pressure", bg='skyblue', font=('tajawal', 15), width=20, height=2, command=self.start_camera)
        pressure_button.place(x=0, y=700)
        self.pressure_level = Canvas(self.Root, width=300, height=50, bg='white', highlightthickness=0)
        self.pressure_level.place(x=280, y=705)
        create_battery(self.pressure_level, 0, 0, 300, 50, 70)

        ##################################  Light     ####################################################
        Light = Button(self.Root,text = 'Light',fg ='black', bg = 'skyblue',font =('tajwal',20,'bold'))
        Light.place(x = 610,y = 240)
        self.light_label = Label(self.Root, text='No Value', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=25,height=1)
        self.light_label.place(x=850, y=240)
        light_button = Button(self.Root, text="Light", bg='skyblue', font=('tajawal', 15), width=20, height=2, command=self.start_camera)
        light_button.place(x=0, y=800)
        self.light_level = Canvas(self.Root, width=300, height=50, bg='white', highlightthickness=0)
        self.light_level.place(x=280, y=805)
        create_battery(self.light_level, 0, 0, 300, 50, 70)


        







        ###################### Labels for Finger Status ########################
        self.labels = []
        positions = [100, 200, 300, 400, 500]
        finger_names = ["", "", "", "", ""]

        for i in range(5):
            title = Label(self.Root, text=finger_names[i], fg='black', bg='skyblue', font=('tajwal', 1, 'bold'))
            title.place(x=0, y=positions[i])
            label = Label(self.Root, text='', fg='black', bg='white', font=('tajwal', 1, 'bold'))
            label.place(x=0, y=positions[i])
            self.labels.append(label)
        ############################################################## connection #####################################
        self.connection_val =is_playstation_controller_connected()
        connection = Button(self.Root,text = 'connection',fg ='black', bg = 'skyblue',font =('tajwal',20,'bold'))
        connection.place(x = 610,y = 30)

        self.connection_label = Label(self.Root, text='No Value', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=25,height=1)
        self.connection_label.place(x=850, y=30)
        if(self.connection_val == True):
             self.connection_label = Label(self.Root, text='Connected', fg='black', bg='green', font=('tajwal', 25, 'bold'),width=25,height=1)
             self.connection_label.place(x=850, y=30)
        elif(self.connection_val == False):
             self.connection_label = Label(self.Root, text='Not Connected', fg='black', bg='red', font=('tajwal', 25, 'bold'),width=25,height=1)
             self.connection_label.place(x=850, y=30)



        #########################################################################################3

        self.speed_label = Label(self.Root, text='No Value', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=25,height=1)
        self.speed_label.place(x=850, y=35)
        
        pos = Button(self.Root,text = 'Position',fg ='black', bg = 'skyblue',font =('tajwal',20,'bold'))
        pos.place(x = 610,y = 100)
        self.x_label = Label(self.Root, text='X = ', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=7,height=1)
        self.x_label.place(x=850, y=105)

        self.y_label = Label(self.Root, text='Y = ', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=7,height=1)
        self.y_label.place(x=1030, y=105)

        self.z_label = Label(self.Root, text='Z = ', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=7,height=1)
        self.z_label.place(x=1210, y=105)
        #############################################################################################################
        pressure = Button(self.Root,text = 'Pressure',fg ='black', bg = 'skyblue',font =('tajwal',20,'bold'))
        pressure.place(x = 610,y = 170)
        self.pressure_label = Label(self.Root, text='No Value', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=25,height=1)
        self.speed_label.place(x=850, y=170)
        


        Speed = Button(self.Root,text = 'Speed',fg ='black', bg = 'skyblue',font =('tajwal',20,'bold'))
        Speed.place(x = 610,y = 310)
        self.speed_label = Label(self.Root, text='No Value', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=25,height=1)
        self.speed_label.place(x=850, y=310)

        Speed = Button(self.Root,text = 'Speed',fg ='black', bg = 'skyblue',font =('tajwal',20,'bold'))
        Speed.place(x = 610,y = 310)
        self.speed_label = Label(self.Root, text='No Value', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=25,height=1)
        self.speed_label.place(x=850, y=310)

        arm = Button(self.Root,text = 'Arm',fg ='black', bg = 'skyblue',font =('tajwal',20,'bold'))
        arm.place(x = 610,y = 380)
        self.arm_label = Label(self.Root, text='No Value', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=25,height=1)
        self.arm_label.place(x=850, y=380)

        Camera = Button(self.Root,text = 'Camera',fg ='black', bg = 'skyblue',font =('tajwal',20,'bold'))
        Camera.place(x = 610,y = 450)
        self.camera_label = Label(self.Root, text='No Value', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=25,height=1)
        self.camera_label.place(x=850, y=450)
        
        
        ################### Labels for Submarine Controls ########################
        self.speed_label = Label(self.Root, text='', fg='black', bg='white', font=('tajwal', 1, 'bold'))
        self.speed_label.place(x=0, y=600)
        self.pressure_label = Label(self.Root, text='', fg='black', bg='white', font=('tajwal', 1, 'bold'))
        self.pressure_label.place(x=0, y=600)
        self.light_label = Label(self.Root, text='', fg='black', bg='white', font=('tajwal', 1, 'bold'))
        self.light_label.place(x=0, y=650)
        self.position_label = Label(self.Root, text='', fg='black', bg='white', font=('tajwal', 1, 'bold'))
        self.position_label.place(x=0, y=650)


        self.num = 0
        self.thread1 = threading.Thread(target=self.get_pressed_button())
        self.thread1.daemon = True
        self.thread1.start()
        print(self.num)

        







# إنشاء مؤشرات بطارية بمستويات شحن مختلفة


    def close_camera(self):
        if self.cap:
            self.cap.release()
            self.cap = None
        self.L1.config(image='')
        for label in self.labels:
            label.config(text="No Value")
        self.speed_label.config(text="Speed: 0")
        self.pressure_label.config(text="Pressure: 0")
        self.light_label.config(text="Light: Off")
        self.position_label.config(text="Position: 0, 0, 0")

    

    def start_camera(self):
        self.close_camera()
        self.f1 = LabelFrame(self.Root)
        self.f1.place(x=0, y=0)
        self.L1 = Label(self.f1)
        self.L1.pack()

        self.cap = cv2.VideoCapture(0)

        while self.cap.isOpened():
            success, img = self.cap.read()
            if not success:
                break
            img = cv2.resize(img, (600, 600))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(img))
            self.L1.config(image=img)
            self.L1.image = img
            self.Root.update()

    def get_pressed_button(self):
        """Initializes the joystick and returns the number of the pressed button on a PlayStation controller."""
        pygame.init()
        pygame.joystick.init()

        joystick_count = pygame.joystick.get_count()
        if joystick_count == 0:
            print("No joystick detected.")
            pygame.quit()
            sys.exit()

        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        start_time = pygame.time.get_ticks()  # Get the current time
        running = True
        while running:
            # Check if 10 milliseconds have passed
           

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Get the state of buttons
            pressed_buttons = [
                i for i in range(joystick.get_numbuttons()) if joystick.get_button(i)
            ]

            if pressed_buttons:
                pygame.quit()
                self.num = pressed_buttons[0]
            time.sleep(1)

        pygame.quit()


        # إنشاء كانفاس للرسم عليه

Page3().Root.mainloop()
