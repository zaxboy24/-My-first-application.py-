class DEQ:
    
    def __init__(self, FullData):
        self.FullData = FullData
#-------- Mag Display ra ------------
    def display(self):
        print "Mao ni ang tanang Data", (self.FullData)
    
#--------Mag Insert ug Data sa Tuo ------
    def insertRigth(self):
        daValue = str(raw_input("Insert Data from right: "))
        self.FullData.append(daValue)
    

#--------- E Delete ang data sa Pinaka-una -----------
    def deleteFirst(self):
        print "Element was remove from First --> {}".format(self.FullData.pop(0))
        return

#--------Mag Insert ug Data sa Wala ------
    def insertLeft(self):
        daValue = str(raw_input("Insert Data from Left: "))
        self.FullData.insert(0, daValue)
        

#--------- E Delete ang data sa Pinaka-ulahi -----------
    def deleteLast(self):
        print "Element was remove from Last --> {}".format(self.FullData.pop(-1))
        return

    
Data = ['Gwapo', 'Kapoy', 'Dula', 'Coffe', 'Tulog']
pare = DEQ(Data)



while True:
    print " "
    print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"
    print "| Mao ni ang gitawag nga Double Ended Queue |"
    print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"
    print " "
    print " 1. Tan awon ang Data"
    print " 2. Mag Butang ug data sa tuo"
    print " 3. Mag Butang ug data sa wala"
    print " 4. Balik sa Root. HAHAHA"
    print " "
    choice = int(raw_input("Palihog ug enter sa number: "))
    print " "
    if choice == 1:
        pare.display()
    elif choice == 2:
        pare.insertRigth()
        pare.deleteFirst()
    elif choice == 3:
        pare.insertLeft()
        pare.deleteLast()
    elif choice == 4:
        break
    else:
        print "BOGO KA"
