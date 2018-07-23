from Tkinter import *
import tkMessageBox as tkm

while True:
    base = Tk()
    base.title("Constructor")
    base.geometry('315x280')
    x = (base.winfo_screenwidth() - base.winfo_reqwidth()) / 2
    y = (base.winfo_screenheight() - base.winfo_reqheight()) / 3
    base.geometry("+{}+{}".format(x, y))

    topLabel = Label(base, text = "Unsa man nga Strucure imong e acces?", bd = 1, font = 'Default 12 bold')
    topLabel.pack(side = TOP, fill = X)

    newFrame = Frame(base)
    newFrame.pack(side = TOP)

    
    Lb1 = Listbox(newFrame, font = 'Default 12 normal', relief = FLAT, bd = 1)
    Lb1.insert(1, "1. Double_Ended_Queues")
    Lb1.insert(2, "2. PriorityQueues")
    Lb1.insert(3, "3. Queues")
    Lb1.insert(4, "4. Stack")
    Lb1.insert(5, "5. Surprise me")
    Lb1.insert(6, "6.Exit...")
    Lb1.pack(fill = X, anchor = CENTER)




    bottomFrame= Frame(base)
    bottomFrame.pack(side = TOP)

    inputLabel = Label(bottomFrame, text = 'Enter the number here', bd = 1, font = 'System 10 normal')
    inputLabel.pack(side = TOP)
    inputEntry = Entry(bottomFrame, bd = 3)
    inputEntry.pack(side = TOP)

    #def watatops(self):
        #waw = "bobo"
        #if borgz == 1:
        #tkm.showinfo('Hi po', 'waw')
        
    base.mainloop()
#while True:
    #print " "
    #print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"
    #print "| Unsa man nga Strucure imong e acces?|"
    #print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"
    #print " "
    #print " 1. Double_Ended_Queues"
    #print " 2. PriorityQueues"
    #print " 3. Queues"
    #print " 4. Stack"
    #print " 5. Surprise me"
    #print " 6. Exit..."
    #print " "
    #pili_na = int(raw_input("Palihog ug enter sa number: "))
    #print " "
    #if pili_na == 1:
        #import Double_Ended_Queues
    #elif pili_na == 2:
        #import PriorityQueues
    #elif pili_na == 3:
        #import Queues
    #elif pili_na == 4:
        #import Stack
    #elif pili_na == 5:
        #import Surprise
    #elif pili_na == 6:
        #print "Good Bye....."
        #break
    #else:
        #print "BOBO KA"

   