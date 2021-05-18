
from tkinter import *
import random
from PIL import ImageTk, Image

global question_answer
names = []
asked = []
score =0

question_answer = {
 1: [ "What must you do when you see blue and red flashing lights behind you?" , 'Speed up to get out of the way', 'Slow down and drive carefully' , 'Slow down and stop' , 'Drive on as usual' , 'Slow down and stop',3] ,
 2: [ "You may stop on a motorway only:" , 'if there is an emergency', 'To let down or pick up passengers' , 'to make a U-turn' , 'to stop and take a photo', 'if there is an emergency' , 1],
 3: [ "When coming up to a pedestrian crossing without a raised traffic island, what must you do?" , "Speed up before the pedestrians cross",
 'Stop and give way to pedestrians on any part of the crossing' , "Sound the horn on your vehicle to warn the pedestrians", "slow down to 3Økmh", 'Stop and give way to pedestrians on any part of the crossing' , 2],
 4: ["Can you stop on a bus stop in a private motor vehicle?" , 'Only between midnight and 6am', "Under no circumstances",
 "When dropping off passengers", 'Only if it is less than 5 minutes' , "Under no circumstances", 2],
 5: ["What is the maximum speed you may drive if you have a 'space saver wheel' fitted? (km/h)" , '7Ø km/h' ,
 "199 km/h so you do not hold up traffic", "89 km/h and if the wheel spacer displays a lower limit that applies", "99 km/h", "86 km/h and if the wheel spacer displays a lower limit that applies", 3],
  6: ["When following another vehicle on a dusty road, you should:" 'Speed up to get passed' , "Turn your vehicle's windscreen wipers on",
 "Stay back from the dust cloud",'Turn your vehicles Headlights on', "Stay back from the dust cloud", 3],
 7: ["What does the sign containing the letters 'LSZ' mean", 'Low safety zone', "Low stability zone", "Lone star zone", ' Limited speed zone' , ' Limited speed zone',4],
 8: ["What speed are you allowed to pass a school bus that has stopped to let students get on or off?", '29 km/h',   '39 km/h', '79 km/h', '19 km/h', '29 km/h' , 1],
 9: ["What is the maximum distance a load may extend in front of a car?" , '2 meters forward of the front edge of the front seat ' "4 meters forward of the front edge of the front seat" , "3 meters forward of the front edge of the front seat", '2.5 meters forward of the front edge of the front seat' , 3],
 10: ["To avoid being blinded by the headlights of another vehicle coming towards you what should you do?" , 'Look to the left of the road' , "Look to the centre of the road",
 "Wear sunglasses that have sufficient strength" , 'Look to the right side of the road', 'Look to the left of the road' , 1]
}





class Quiz:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color="orange"# to set it as background color for all the label widgets


        #open image
        self.comp_image= Image.open("computer.jpg")
        self.comp_image=self.comp_image.resize((250,250), Image.ANTIALIAS)
        self.comp_image=ImageTk.PhotoImage(self.comp_image)



        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        #padx, pady How many pixels to pad widget, horizontally (x) and vertically (y), outside widget's borders.
        self.quiz_frame.grid()#This geometry manager organizes widgets in a table-like structure in the parent widget.
               
        #widgets goes below
        self.heading_label=Label(self.quiz_frame, text="Coding quiz", font=("Tw Cen MT","18","bold"),bg=background_color)
        self.heading_label.grid(row=0, padx=20) 
     
        #label image
        self.image_label= Label(self.quiz_frame, image=self.comp_image)
        #self.image_label.grid(row=0, column=1) #on left side
        self.image_label.grid(row=1)
        #label for username
        self.user_label=Label(self.quiz_frame, text="Please enter your username below: ", font=("Tw Cen MT","16"),bg=background_color)
        self.user_label.grid(row=2, padx=20, pady=20) 
        
        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=3,padx=20, pady=20)
        
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="orange", command=self.name_collection)
        self.continue_button.grid(row=4,  padx=20, pady=20)        
        


    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to names list declared at the beginning
        self.continue_button.destroy()
        self.entry_box.destroy() #Destroy name frame then open the quiz runner
      
           

if __name__ == "__main__":
    root = Tk()
    root.title("Coding quiz") 

    quiz_instance = Quiz(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear
