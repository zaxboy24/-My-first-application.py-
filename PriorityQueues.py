import time
class PriorityQueues:
    def __init__(self, Full):
        self.Full = Full
#---------- To view the Data ------------
    def view(self):
        print "Mao ni ang tanang data", (self.Full)
        return

#---------- To Add a Data ------------
    def add(self):
        getNum = int(raw_input("Enter a number do you want to add: "))
        self.Full.append(getNum)
        print "imong gi add nga data: {}".format(getNum)
        
#---------- To Find the minimum Value ------------
    def findMin(self):
        rat = min(self.Full)
        print "Mao ni ang pinakagamay nga data {}".format(rat)

#---------- To Find the maximum Value ------------
    def findMax(self):
        cat = max(self.Full)
        print "Mao ni ang pinakagamay nga data {}".format(cat)

#---------- To Delete the minimum Value ------------
    def deleteMin(self):
        dog = min(self.Full)
        self.Full.remove(dog)
        print "Mao ni ang na wala nga data {}".format(dog)

#---------- To Delete the maximum Value ------------
    def deleteMax(self):
        bat = max(self.Full)
        self.Full.remove(bat)
        print "Mao ni ang na wala nga data {}".format(bat)

#---------- To Sor the Data ------------
    def sort(self):
        self.Full.sort()
        print "Inganion pag sort bogo --->", self.Full
    






TheList = [4, 6, 1, 5, 7, 2, 3, 8, 9]


wata = PriorityQueues(TheList)

while True:
    time.sleep(0.5)
    print " "
    print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
    print "Mao ni ang gitawag nga Priority Queue "
    print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
    print " "
    print " 1. Tan awon ang Data"
    print " 2. Tan mag dugang ug Data"
    print " 3. Pangitaon ang pinaka-gamay nga Data"
    print " 4. Pangitaon ang pinaka-dako nga Data"
    print " 5. Walaon ang pinaka-gamay nga Data"
    print " 6. Walaon ang pinaka-dako nga Data"
    print " 7. E sort ang Data"
    print " 8. Balik sa root! HAHAHA"
    print " "
    choice = int(raw_input("Palihog ug enter sa number: "))
    print " "
    if choice == 1:
        wata.view()
    elif choice == 2:
        wata.add()
    elif choice == 3:
        wata.findMin()
    elif choice == 4:
        wata.findMax()
    elif choice == 5:
        wata.deleteMin()
    elif choice == 6:
        wata.deleteMax()
    elif choice == 7:
        wata.sort()
    elif choice == 8:
        break
    else:
        print "BOGO KA"
