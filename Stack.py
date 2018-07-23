class MyStack:
	def __init__(self,Stack_Data):
		self.Stack_Data = Stack_Data
		
#--------- Display the Data ---------
	def view_stack(self):
		print "Mao ni tanang Data nimo", self.Stack_Data

#--------- Add Data ----------
	def add_Data(self):
		print "You are Required to enter 5 Data"
		i = 0
		while i < 5:
			waw = raw_input("Enter a Data: ")
			i += 1
			self.Stack_Data.insert(0, waw)

#---------- Pop out the Data --------
	def PopFirst(self):
		print "This the first data that remove -->", self.Stack_Data.pop(0)
        
#---------- Insert a Data --------
	def insert_Data(self):
		meow = raw_input("Insert Data: ")
		self.Stack_Data.insert(0, meow)



Data = []

pepep = MyStack(Data)

pepep.add_Data()

while True:
    print " "
    print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"
    print "| Mao ni ang gitawag nga Queues |"
    print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"
    print " "
    print " 1. Tan awon ang Data"
    print " 2. E delete ang una nga Data"
    print " 3. Mag insert ug data"
    print " 4. Balik sa Root. HAHAHA"
    print " "
    choice = int(raw_input("Palihog ug enter sa number: "))
    print " "
    if choice == 1:
	pepep.view_stack()
    elif choice == 2:
    	pepep.PopFirst()
    elif choice == 3:
        pepep.insert_Data()
    elif choice == 4:
		break
    else:
        print "Bogo ka"
