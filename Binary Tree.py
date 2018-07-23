class Vorgz_Node:
    def __init__(self, value):
        self.value = value
        self.LeftAnak = None
        self.RightAnak = None
    def insert(self, data):
        if self.value == data:
            return False
        elif self.data > data:
            if self.LeftAnak:
                return self.LeftAnak.insert(data)
            else:
                self.LeftAnak = Vorgz_Node(data)
                return True
        else:
            if self.RightAnak:
                return self.RightAnak.insert(Ndata)
            else:
                self.RightAnak = Vorgz_Node(Ndata)
                return True
    def find(self, data):
        if(self.value == data):
            if self.LeftAnak:
                return True
            elif self.data > data:
                return self.LeftAnak.find(data)
            else:
                return False
        else:
            if self.data > data:
                return self.RightAnak.find(data)
            else:
                return False
    def preorder(self):
        if self:
            print (str(self.value))
            if self.LeftAnak:
                self.LeftAnak.preorder()
            if self.RightAnak:
                self.RightAnak.preorder()






class Tree:
    def __init__(self):
        self.ugat = None
    def insert(self, data):
        if self.ugat:
            return self.ugat.insert(data)
        else:
            self.ugat = Vorgz_Node(data)
            return True
    
    def find(self, data):
        if self.ugat:
            return self.ugat.find(data)
        else:
            return False

    def PrintTree(self):
        if self.LeftAnak:
            self.LeftAnak.PrintTree()
        print( self.data),
        if self.RightAnak:
            self.RightAnak.PrintTree()


    def preorder(self):
        print ("This is a Pre-order")
        self.ugat.preorder()

Final = Tree()
Final.insert(1)
Final.insert(2)
Final.insert(3)
Final.insert(4)
Final.insert(5)
Final.insert(6)
Final.insert(7)
Final.insert(8)
Final.insert(9)
Final.insert(10)
Final.insert(11)
Final.insert(12)
Final.insert(13)
print final.PrintTree
Final.preorder()




