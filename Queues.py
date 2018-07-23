class Queues:
    def __init__(self, Stack):
        self.Stack = Stack
        
    def view(self):
        print "Mao ni imong mga Piborito"
        for i in range(len(MyFavFood)):
            print (MyFavFood[i])
            
#------- Enqueue and Dequeue ----------
    def Queue_And_Dequeue(self):
        addValue = (raw_input("What is your favorite Food?: "))
        self.Stack.append(addValue)
        print "You Enqueue this data -->{}".format(self.Stack[-1])
        print "You Dequeue this data -->{}".format(self.Stack.pop(0))
        


MyFavFood = ['Milo', 'Hotdog', 'Rice', 'Milk','Jumba']

ThisMe = Queues(MyFavFood)

while True:
    print " "
    print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"
    print "| Mao ni ang gitawag nga Queues |"
    print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"
    print " "
    print " 1. Tan awon ang Data"
    print " 2. Mag dugang ug mag delete ug Data"
    print " 3. Balik sa Root. HAHAHA"
    print " "
    choice = int(raw_input("Palihog ug enter sa number: "))
    print " "
    if choice == 1:
        ThisMe.view()
    elif choice == 2:
        ThisMe.Queue_And_Dequeue()
    elif choice == 3:
        break
    else:
        print "Bogo ka"
