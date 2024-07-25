import cv2
import numpy as np
import webbrowser
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import pygame
import sys
import time
import socket






l = []
"""

ip_control_motor_speed ='127.0.0.1' 
port_control_motor_speed = 65432
"""
ip_control_motor_speed ='192.168.1.177' 
port_control_motor_speed = 12345

ip_get_value = '127.0.0.2' 
port_get_value = 65433


class page1:
    
 def __init__(self):
    self.pro = Tk()
    self.pro.geometry("1040x570+350+150")

    self.pro.resizable(False,False)
    self.pro.title("SUBMARINE_CONTROL")
    self.pro.iconbitmap('D:\\zyad\\bionic hand\\application\\image\\images.ico')
    title = Label(self.pro,text = 'SUBMARINE_CONTROL',fg ='gold', bg = 'black',font =('tajwal',15,'bold'))
    title.pack(fill = X)


    F1 = Frame(self.pro,width = 238, height = 550,bg = '#0B2F3A')
    F1.place(x =803 , y =29 )
    Title1 = Label(F1,text = 'نافذة تحكم في الغواصة',fg ='white', bg = '#0B2F3A',font =('tajwal',12,'bold'))
    Title1.place(x =42, y =10)
    Title2 = Label(F1,text ="المطور زياد طارق",fg ='white', bg = '#0B2F3A',font =('tajwal',12,'bold'))
    Title2.place(x =90, y =40)
    Title2 = Label(F1,text ="وسائل الاتصال  بنا",fg ='white', bg = '#0B2F3A',font =('tajwal',12,'bold'))
    Title2.place(x =90, y =70)





    B1 = Button(F1, text = "بيانات المشروع علي درايف",width = 26, fg = 'black',bg = '#DBA901',font=('tajawal',11,'bold'),command = self.Open1)
    B1.place(x = 6,y = 110)
    B2 = Button(F1, text = "حسابنا علي الفيس بوك",width = 26, fg = 'black',bg = '#DBA901',font=('tajawal',11,'bold'),command =self.Open2)
    B2.place(x = 6,y = 150)
    B3 = Button(F1, text = "حسابنا علي تليجرام",width = 26, fg = 'black',bg = '#DBA901',font=('tajawal',11,'bold'),command = self.Open3)
    B3.place(x = 6,y = 200)
    B4 = Button(F1, text = " لمحة عن التيم",width = 26, fg = 'black',bg = '#DBA901',font=('tajawal',11,'bold'),command =self.about1)
    B4.place(x = 6,y = 250)
    B5 = Button(F1, text = "لمحةعن المنشروع",width = 26, fg = 'black',bg = '#DBA901',font=('tajawal',11,'bold'),command = self.about2)
    B5.place(x = 6,y = 300)
    B6 = Button(F1, text = "اغلاق البرنامج",width = 26, fg = 'black',bg = '#DBA901',font=('tajawal',11,'bold'),command = quit)
    B6.place(x = 6,y = 350)

    photo = PhotoImage(file = r"C:\Users\zyadt\OneDrive\Desktop\image\image3.png")
    l.append(photo)
    imo = Label(self.pro,image = l)
    imo.place(x = 0, y = 30)








    L1 = Label (self.pro, text = "Name of user:",bg='skyblue',fg = 'black',font = ('tajawal',15) )
    L1.place (x =362, y =200)
    self.En1 = Entry(self.pro, font=("tajawal",15))
    self.En1.place(x = 362,y =230)


    L2 = Label (self.pro, text = "Password:",bg='skyblue',fg = 'black',font = ('tajawal',15))
    L2.place (x =362, y =260)
    self.En2 = Entry(self.pro, font=("tajawal",15),show = "*")
    self.En2.place(x = 362,y =290)
    
    

    B = Button(self.pro ,text = "login",bg = 'white',font=('tajawal',15),width=5, height = 1,command = self.Page2)
    B.place(x = 440,y = 330)
    
    self.u1 = "https://projecthub.arduino.cc/Gabry295/404101bb-d229-486e-a348-a4d77e730331"
    self.u2 ="https://www.facebook.com/zyad.tarek.1291"
    self.u3 = "https://www.facebook.com/login/"
    self.u4 ="https://www.facebook.com/login/"
    self.u5 = "https://www.facebook.com/login/"
    
    
    
    
    
    
    
 def Page2(self):
    passw =self.En2.get()
    user = self.En1.get()
    if user == "zyad" and passw == "1234":
           self.pro.withdraw()
           Page3().Root.mainloop()

    else:
       messagebox.showinfo("Error","incorrect password")
 def Page2_():
      Page3().Root.withdraw()
      Page3().Root.mainloop()
       


 def Open1(self):
      webbrowser.open_new(self.u1)
      
 def Open2(self):
      webbrowser.open_new(self.u2)
      
 def Open3(self):
      webbrowser.open_new(self.u3)
      
 def Open4(self):
      webbrowser.open_new(self.u4)
 def Open5(self):
      webbrowser.open_new(self.u5)
      
   
 def about1(self):
      messagebox.showinfo('المطور','زياد طارق ابراهيم')
   
   
 def about2(self):
      messagebox.showinfo('لمحة عن البرنامج','مشروع لتجكم في يد صناعية')
   
































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
        img1 = PhotoImage(file=r"C:\Users\zyadt\OneDrive\Desktop\image\image2.png")
        l3 = Label(self.Root, image=img1)
        l3.image = img1  # Reference to the image object
        l3.grid()

        self.cap = None

        B = Button(self.Root, text="Start", bg='skyblue', font=('tajawal', 15), width=20, height=2, command=self.start_camera)
        B.place(x=650, y=600)
        B2 = Button(self.Root, text="Stop", bg='skyblue', font=('tajawal', 15), width=20, height=2, command=self.close_camera)
        B2.place(x=650, y=700)
        B4 = Button(self.Root, text="Close", bg='skyblue', font=('tajawal', 15), width=20, height=2, command=quit)
        B4.place(x=650 ,y=800)

        btn_up = Button(self.Root, text="Forward",  bg='skyblue', font=('tajawal', 15), width=10, height=2)
        btn_up.place(x=1100, y=600)
        btn_down = Button(self.Root, text="Reverse",  bg='skyblue', font=('tajawal', 15), width=10, height=2)
        btn_down.place(x=1100, y=750)

        btn_right = Button(self.Root, text="Left",  bg='skyblue', font=('tajawal', 15), width=10, height=2)
        btn_right.place(x=980, y=673)

        btn_left = Button(self.Root, text="Right",  bg='skyblue', font=('tajawal', 15), width=10, height=2)
        btn_left.place(x=1227, y=673)

        btn_HIGH = Button(self.Root, text="UP",  bg='skyblue', font=('tajawal', 15), width=10, height=2)
        btn_HIGH.place(x=1400, y=600)
        btn_LOW = Button(self.Root, text="Down",  bg='skyblue', font=('tajawal', 15), width=10, height=2)
        btn_LOW.place(x=1400, y=750)






        self.f1 = LabelFrame(self.Root)
        self.f1.place(x=0, y=0)
        self.L1 = Label(self.f1)
        self.L1.pack()
        # Add canvas for battery indicators

        speed_button = Button(self.Root, text="Speed", bg='skyblue', font=('tajawal', 15), width=20, height=2, command=self.start_camera)
        speed_button.place(x=0, y=600)
        self.speed_level = Canvas(self.Root, width=300, height=50, bg='white', highlightthickness=0)
        self.speed_level.place(x=280, y=605)
        create_battery(self.speed_level, 0, 0, 300, 50, 10)


        pressure_button = Button(self.Root, text="Pressure", bg='skyblue', font=('tajawal', 15), width=20, height=2, command=self.start_camera)
        pressure_button.place(x=0, y=700)
        self.pressure_level = Canvas(self.Root, width=300, height=50, bg='white', highlightthickness=0)
        self.pressure_level.place(x=280, y=705)
        create_battery(self.pressure_level, 0, 0, 300, 50, 10)

        ##################################  Light     ####################################################
        Light = Button(self.Root,text = 'Light',fg ='black', bg = 'skyblue',font =('tajwal',20,'bold'))
        Light.place(x = 610,y = 240)
        self.light_label = Label(self.Root, text='No Value', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=25,height=1)
        self.light_label.place(x=850, y=240)

        Temp_button = Button(self.Root, text="Temperature", bg='skyblue', font=('tajawal', 15), width=20, height=2, command=self.start_camera)
        Temp_button.place(x=0, y=800)
        self.Temp_level = Canvas(self.Root, width=300, height=50, bg='white', highlightthickness=0)
        self.Temp_level.place(x=280, y=805)
        create_battery(self.Temp_level, 0, 0, 300, 50, 10)

        self.toggle_light = 0
        self.counter = 0


        







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
        angle = Button(self.Root,text = 'angle',fg ='black', bg = 'skyblue',font =('tajwal',20,'bold'))
        angle.place(x = 610,y = 30)

     

  
        self.x_angle_label = Label(self.Root, text='X = ', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=7,height=1)
        self.x_angle_label.place(x=850, y=30)

        self.y_angle_label = Label(self.Root, text='Y = ', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=7,height=1)
        self.y_angle_label.place(x=1030, y=30)

        self.z_angle_label = Label(self.Root, text='Z = ', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=7,height=1)
        self.z_angle_label.place(x=1210, y=30)

        self.connection_val =is_playstation_controller_connected()

  



        #########################################################################################3

    
        
        pos = Button(self.Root,text = 'Acceleration',fg ='black', bg = 'skyblue',font =('tajwal',20,'bold'))
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
        self.pressure_label.place(x=850, y=170)


        Motor = Button(self.Root,text = 'Motor',fg ='black', bg = 'skyblue',font =('tajwal',20,'bold'))
        Motor.place(x = 610,y = 520)
        self.motor_label = Label(self.Root, text='No Value', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=25,height=1)
        self.motor_label.place(x=850, y=520)
        


        Speed = Button(self.Root,text = 'Speed',fg ='black', bg = 'skyblue',font =('tajwal',20,'bold'))
        Speed.place(x = 610,y = 310)
        self.speed_label = Label(self.Root, text='No Value', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=25,height=1)
        self.speed_label.place(x=850, y=310)

        arm = Button(self.Root,text = 'Arm',fg ='black', bg = 'skyblue',font =('tajwal',20,'bold'))
        arm.place(x = 610,y = 380)
        self.arm_label = Label(self.Root, text='No Value', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=11,height=1)
        self.arm_label.place(x=850, y=380)
        self.arm_label1 = Label(self.Root, text='No Value', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=11,height=1)
        self.arm_label1.place(x=1140, y=380)

        Temp = Button(self.Root,text = 'Temperature',fg ='black', bg = 'skyblue',font =('tajwal',20,'bold'))
        Temp.place(x = 610,y = 450)
        self.Temp_label = Label(self.Root, text='No Value', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=25,height=1)
        self.Temp_label.place(x=850, y=450)
        
        
        ################### Labels for Submarine Controls ########################
        self.counter_speed = 0
        self.temp_count = 0
        self.tem_up_down = 0
        self.temp_camera = 0
        self.toggle_motor = 0
        self.ip_control_motor =ip_control_motor_speed
        self.port_control_motor = port_control_motor_speed
        self.ip_get_value_arduino = ip_get_value
        self.port_get_value_arduino = port_get_value

        self.speed_label = Label(self.Root, text='', fg='black', bg='white', font=('tajwal', 1, 'bold'))
        self.speed_label.place(x=0, y=600)
        self.pressure_label = Label(self.Root, text='', fg='black', bg='white', font=('tajwal', 1, 'bold'))
        self.pressure_label.place(x=0, y=600)
        self.light_label = Label(self.Root, text='', fg='black', bg='white', font=('tajwal', 1, 'bold'))
        self.light_label.place(x=0, y=650)
        self.position_label = Label(self.Root, text='', fg='black', bg='white', font=('tajwal', 1, 'bold'))
        self.position_label.place(x=0, y=650)
        self.temp_camera_light = 0
        self.tem_rec = 0
        
        # Initialize joystick
        self.joystick = None
        self.init_joystick()

        # Start checking for pressed buttons
        self.check_button_pressed()
        self.update_data()

    def init_joystick(self):
        """Initializes the joystick."""
        pygame.init()
        pygame.joystick.init()

        joystick_count = pygame.joystick.get_count()
        if joystick_count == 0:
            print("No joystick detected.")
            pygame.quit()
            return

        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    def check_button_pressed(self):
      
        """Checks which button is pressed on the joystick and updates the label."""
        if not self.joystick:
            self.init_joystick()
        
        if self.joystick:
            pygame.event.pump()
            row, row_num_right=self.get_analog_sticks(self.joystick)
            if(row == 0):
                self.counter = self.counter + 1
                if(self.counter >10):
                        btn_up = Button(self.Root, text="Forward",  bg='red', font=('tajawal', 15), width=10, height=2)
                        btn_up.place(x=1100, y=600)
                        self.counter = 0
                        self.temp_count = 0
                        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,"direction forward")

            elif(row == 1):
                self.counter = self.counter + 1
                if(self.counter >10):
                        btn_down = Button(self.Root, text="Reverse",  bg='red', font=('tajawal', 15), width=10, height=2)
                        btn_down.place(x=1100, y=750)
                        self.counter = 0
                        self.temp_count = 0
                        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,"direction reverse")

            elif(row == 2):
                self.counter = self.counter + 1
                if(self.counter >10):
                        btn_right = Button(self.Root, text="Left",  bg='red', font=('tajawal', 15), width=10, height=2)
                        btn_right.place(x=980, y=673)
                        self.counter = 0
                        self.temp_count = 0
                        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,"direction right")

            elif(row == 3):
                self.counter = self.counter + 1
                if(self.counter >10):
                        btn_left = Button(self.Root, text="Right",  bg='red', font=('tajawal', 15), width=10, height=2)
                        btn_left.place(x=1227, y=673)
                        self.counter = 0
                        self.temp_count = 0
                        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,"direction left")


                

                

            elif(row == -1 and self.temp_count == 0):

                btn_up = Button(self.Root, text="Forward",  bg='skyblue', font=('tajawal', 15), width=10, height=2)
                btn_up.place(x=1100, y=600)
                btn_down = Button(self.Root, text="Reverse",  bg='skyblue', font=('tajawal', 15), width=10, height=2)
                btn_down.place(x=1100, y=750)

                btn_right = Button(self.Root, text="Left",  bg='skyblue', font=('tajawal', 15), width=10, height=2)
                btn_right.place(x=980, y=673)

                btn_left = Button(self.Root, text="Right",  bg='skyblue', font=('tajawal', 15), width=10, height=2)
                btn_left.place(x=1227, y=673)
                self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"   ")

                self.temp_count = 1




            pressed_buttons = [i for i in range(self.joystick.get_numbuttons()) if self.joystick.get_button(i)]
            if pressed_buttons:
                self.num = pressed_buttons[0]


                if(self.num == 0):
                    self.counter =self.counter+1
                    if(self.counter > 12):
                        self.arm_label1 = Label(self.Root, text='Arm2 ON', fg='black', bg='green', font=('tajwal', 25, 'bold'),width=11,height=1)
                        self.arm_label1.place(x=1140, y=380)
                        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"Arm2 ON")                     
                        self.counter = 0
                        self.tem_rec = 1

                    
                elif(self.num == 4):
                    self.counter =self.counter+1
     
                    if(self.counter > 15):
                        self.counter_speed = self.counter_speed - 1
                        if(self.counter_speed > 20):
                            self.counter_speed = 20
                            self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"speed {self.counter_speed}")

                        elif(self.counter_speed <= 0):
                            self.counter_speed = 0
                            self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"speed {self.counter_speed}")

                        if( self.counter_speed < 0):
                            self.speed_label = Label(self.Root, text='Zero', fg='black', bg='white', font=('tajwal', 25, 'bold'),width=25,height=1)
                            self.speed_label.place(x=850, y=310)
                            create_battery(self.speed_level, 0, 0, 300, 50, 0)
                            self.counter_speed = 0
                            self.counter = 0
                            self.tem_rec = 1
                            self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"speed {self.counter_speed}")

                        else:
                            str_num = str(self.counter_speed)
                            self.speed_label = Label(self.Root, text=f'{str_num} m/s', fg='black', bg='red', font=('tajwal', 25, 'bold'),width=25,height=1)
                            self.speed_label.place(x=850, y=310)
                            create_battery(self.speed_level, 0, 0, 300, 50, (self.counter_speed*10)/2)
                            self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"speed {self.counter_speed}")
                        self.tem_rec = 1
             
                  
                
               
                
                elif(self.num == 5):
                    self.counter =self.counter+1
                    if(self.counter > 15):
                        self.counter_speed = self.counter_speed + 1
                        if(self.counter_speed > 20):
                            self.counter_speed = 20
                            self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"speed {self.counter_speed}")

                        elif(self.counter_speed <= 0):
                            self.counter_speed = 0                      
                            self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"speed {self.counter_speed}")


                        if( self.counter_speed >= 20):
                            self.speed_label = Label(self.Root, text='Max Speed', fg='black', bg='green', font=('tajwal', 25, 'bold'),width=25,height=1)
                            self.speed_label.place(x=850, y=310)
                            create_battery(self.speed_level, 0, 0, 300, 50, 100)
                            self.counter_speed = 20
                            self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"speed {self.counter_speed}")

                        else:
                            str_num = str(self.counter_speed)
                            self.speed_label = Label(self.Root, text=f'{str_num} m/s', fg='black', bg='green', font=('tajwal', 25, 'bold'),width=25,height=1)
                            self.speed_label.place(x=850, y=310)
                            self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"speed {self.counter_speed}")

                            create_battery(self.speed_level, 0, 0, 300, 50, (self.counter_speed*10)/2)
                        self.counter = 0
                        self.tem_rec = 1


                elif(self.num == 6):
                    self.counter =self.counter+1
                    if(self.counter > 10):
                        btn_LOW = Button(self.Root, text="Down",  bg='red', font=('tajawal', 15), width=10, height=2)
                        btn_LOW.place(x=1400, y=750)
                        self.tem_up_down = 0
                        self.counter = 0
                        self.tem_rec = 1
                        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,"direction Down")
                elif(self.num == 7):
                    self.counter =self.counter+1
                    if(self.counter > 10):
                        btn_HIGH = Button(self.Root, text="UP",  bg='red', font=('tajawal', 15), width=10, height=2)
                        btn_HIGH.place(x=1400, y=600)
                        self.tem_up_down = 0
                        self.counter = 0
                        self.tem_rec = 1
                        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,"direction UP")
                elif(self.num == 8 ):
                    self.counter =self.counter+1
                    if(self.counter > 5 and self.temp_camera == 0):
                        self.start_camera()
                        self.counter = 0
                        self.temp_camera = 1
                        self.tem_rec = 1
                elif(self.num == 9):
                    self.counter =self.counter+1
                    if(self.counter > 5):
                        self.close_camera()
                        self.counter = 0
                        self.temp_camera = 0
                        self.tem_rec = 1
                elif(self.num == 3 ):
                    self.counter =self.counter+1
                    if(self.counter > 10 ):
                        self.arm_label = Label(self.Root, text='Arm1 ON', fg='black', bg='green', font=('tajwal', 25, 'bold'),width=11,height=1)
                        self.arm_label.place(x=850, y=380)
                        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,"Arm1 ON")
                        self.tem_rec = 1

                        self.counter = 0

                elif(self.num == 1):
                    self.counter =self.counter+1
                    if(self.counter > 5):
                        self.arm_label = Label(self.Root, text='Arm1 OFF', fg='black', bg='red', font=('tajwal', 25, 'bold'),width=11,height=1)
                        self.arm_label.place(x=850, y=380)
                        self.tem_rec = 1
                        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,"Arm1 OFF")


                        self.counter = 0
                
                elif(self.num == 10):
                    self.counter =self.counter+1
                    if( self.counter > 12):
                        self.motor_label = Label(self.Root, text='Motor Run', fg='black', bg='green', font=('tajwal', 25, 'bold'),width=25,height=1)
                        self.motor_label.place(x=850, y=520)
                        self.counter = 0
                        self.tem_rec = 1
                        
                        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"Motor ON")




                elif(self.num == 2):
                    self.counter =self.counter+1
                    if(self.counter > 12):
                        self.arm_label1 = Label(self.Root, text='Arm2 OFF', fg='black', bg='red', font=('tajwal', 25, 'bold'),width=11,height=1)
                        self.arm_label1.place(x=1140, y=380)
                        self.counter = 0
                        self.tem_rec = 1
                        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"Arm2 OFF")


                

                elif(self.num == 11):
                    self.counter =self.counter+1
                    if( self.counter > 12):
                        self.motor_label = Label(self.Root, text='Motor OFF', fg='black', bg='red', font=('tajwal', 25, 'bold'),width=25,height=1)
                        self.motor_label.place(x=850, y=520)
                        self.counter = 0
                        self.toggle_motor = 0
                        self.tem_rec = 1
                        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"Motor OFF")

       



                     

            elif(self.tem_up_down == 0):
                        btn_HIGH = Button(self.Root, text="UP",  bg='skyblue', font=('tajawal', 15), width=10, height=2)
                        btn_HIGH.place(x=1400, y=600)
                        btn_LOW = Button(self.Root, text="Down",  bg='skyblue', font=('tajawal', 15), width=10, height=2)
                        btn_LOW.place(x=1400, y=750)
                        self.tem_up_down = 1
                        self.tem_rec = 1

            else:
                if(self.tem_rec ):
                        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"   ")
                        self.tem_rec = 0
                else:
                    pass






          

            
        
                           



                
        
        self.Root.after(2, self.check_button_pressed)

 
        

        

    def close_camera(self):
        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"Camera OFF")
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
        self.temp_camera_light = 0
        self.light_label = Label(self.Root, text='Light OFF', fg='black', bg='red', font=('tajwal', 25, 'bold'),width=25,height=1)
        self.light_label.place(x=850, y=240)
        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"Light OFF")

    def start_camera(self):

        self.close_camera()
        self.f1 = LabelFrame(self.Root)
        self.f1.place(x=0, y=0)
        self.L1 = Label(self.f1)
        self.L1.pack()

        self.cap = cv2.VideoCapture(1)
        self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"Camera ON")
        def update_frame():
            if self.cap.isOpened():
                success, img = self.cap.read()
                if success:
                    img = cv2.resize(img, (600, 580))
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    img = ImageTk.PhotoImage(Image.fromarray(img))
                    self.L1.config(image=img)
                    self.L1.image = img
                self.Root.after(10, update_frame)
        
        if (self.temp_camera_light == 0):
        
            self.light_label = Label(self.Root, text='Light ON', fg='black', bg='green', font=('tajwal', 25, 'bold'),width=25,height=1)
            self.light_label.place(x=850, y=240)
            self.send_data_to_arduino(self.ip_control_motor,self.port_control_motor,f"Light ON")
            self.temp_camera_light = 1
        
        update_frame()

    def get_analog_sticks(self,joystick):

        # Initialize the analog stick values
        left_stick_x = joystick.get_axis(0)
        left_stick_y = joystick.get_axis(1)
        right_stick_x = joystick.get_axis(2)
        right_stick_y = joystick.get_axis(3)

        # Determine cardinal direction for left analog stick
        if left_stick_y < -0.5:
            left_direction = 1  # Up
        elif left_stick_y > 0.5:
            left_direction = 2  # Down
        elif left_stick_x < -0.5:
            left_direction = 3  # Left
        elif left_stick_x > 0.5:
            left_direction = 4  # Right
        else:
            left_direction = 0  # Centered

        # Determine cardinal direction for right analog stick
        if right_stick_y < -0.5:
            right_direction = 1  # Up
        elif right_stick_y > 0.5:
            right_direction = 2  # Down
        elif right_stick_x < -0.5:
            right_direction = 3  # Left
        elif right_stick_x > 0.5:
            right_direction = 4  # Right
        else:
            right_direction = 0  # Centered

        return left_direction - 1, right_direction - 1  # Adjust to return 0 to 3 instead of 1 to 4
    def send_data_to_arduino(self,ip, port, data):
        """Sends data to the Arduino server."""
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Connect to the server
            s.connect((ip, port))
            
            # Send data
            s.sendall(data.encode())
            
            # Receive a response
           
        except Exception as e:
            print(f"An error occurred: {e}")


    def receive_data_from_arduino(self, ip, port):
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Connect to the server
            s.connect((ip, port))
            
            # Send a request (could be any data, here a newline to trigger data sending)
            s.sendall(b'\n')
            
            # Receive the data
            response = s.recv(1024).decode()
            print('Received from server:', response)
            
            # Close the connection
            s.close()
            
            # Parse the received data
            data = response.split(', ')
            pressure = float(data[0].split(': ')[1].split(' ')[0])
            temperature = float(data[1].split(': ')[1].split(' ')[0])
            
            accel_data = data[2].split(': ')[1].split(',')
            accel_x = float(accel_data[0])
            accel_y = float(accel_data[1])
            accel_z = float(accel_data[2])
            
            gyro_data = data[3].split(': ')[1].split(',')
            gyro_x = float(gyro_data[0])
            gyro_y = float(gyro_data[1])
            gyro_z = float(gyro_data[2])
            
            return pressure, temperature, accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z
        except Exception as e:
            print(f"An error occurred: {e}")
            return None# # Schedule to run this method again after 10 milliseconds
        
    def update_data(self):
        data = self.receive_data_from_arduino(self.ip_get_value_arduino, self.port_get_value_arduino)
        if data:
            pressure, temperature, accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z = data

            self.pressure_label = Label(self.Root, text=f'{str(pressure)}hpa', fg='black', bg='red', font=('tajwal', 25, 'bold'),width=25,height=1)
            self.pressure_label.place(x=850, y=170)

            create_battery(self.pressure_level, 0, 0, 300, 50, (pressure/50)*2)

            self.x_label = Label(self.Root, text=f'X ={accel_x}', fg='black', bg='red', font=('tajwal', 25, 'bold'),width=7,height=1)
            self.x_label.place(x=850, y=105)

            self.y_label = Label(self.Root, text=f'Y ={accel_y}', fg='black', bg='red', font=('tajwal', 25, 'bold'),width=7,height=1)
            self.y_label.place(x=1030, y=105)

            self.z_label = Label(self.Root, text=f'Z ={accel_z}', fg='black', bg='red', font=('tajwal', 25, 'bold'),width=7,height=1)
            self.z_label.place(x=1210, y=105)

            self.Temp_label = Label(self.Root, text=f'{temperature} C', fg='black', bg='red', font=('tajwal', 25, 'bold'),width=25,height=1)
            self.Temp_label.place(x=850, y=450)


            self.x_angle_label = Label(self.Root, text=f'X ={gyro_x}', fg='black', bg='red', font=('tajwal', 25, 'bold'),width=7,height=1)
            self.x_angle_label.place(x=850, y=30)

            self.y_angle_label = Label(self.Root, text=f'Y ={gyro_y}', fg='black', bg='red', font=('tajwal', 25, 'bold'),width=7,height=1)
            self.y_angle_label.place(x=1030, y=30)

            self.z_angle_label = Label(self.Root,text=f'Z ={gyro_z}' , fg='black', bg='red', font=('tajwal', 25, 'bold'),width=7,height=1)
            self.z_angle_label.place(x=1210, y=30)

            create_battery(self.Temp_level, 0, 0, 300, 50, int(temperature)*2)

        
            

            
   
        
        self.Root.after(2000, self.update_data) 

            

# Create a Tkinter root window and start the application
page1().pro.mainloop()