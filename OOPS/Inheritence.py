class A:                                #definition of classA
    def __init__(self):                 #constructor of classA
        print("init of A")

    def methodOfA(self):                #method of classA
        print("methodOfA")

class B:
    def __init__(self):
        print("init of B")

    def methodOfB(self):
        print("methodOfB")


class C:
    def __init__(self):
        print("init of C")

    def methodOfC(self):
        print("methodOfC")


class D(A):                             #Single-Level Inheritence
    def __init__(self):
        print("init of D")

    def methodOfD(self):
        print("methodOfD")

class E(D):                             #Multi-Level Inheritence
    def __init__(self):
        print("init of E")

    def methodOfE(self):
        print("methodOfE")

class F(A, B, C):                       #Heirarchical Inheritence
    def __init__(self):
        print("init of F")

    def methodOfF(self):
        print("methodOfF")

class G(A):                             
    def __init__(self):
        super().__init__()              #Using super() method to call the constructor of the parent class
        print("init of G")

    def methodOfG(self):
        print("methodOfG")

class H(B, C):                          #Multiple Inheritence, Creating Diamond Problem (Not allowed in java)
    def __init__(self):
        super().__init__()              #This super() method will call the constructor of the left most parent 
        print("init of H")              #in this case its classB
                                        #this thing is tackled using MRO(Method Resolution Order) in python
    def methodOfH(self):
        print("methodOfH")

obj1 = A()
obj2 = B()
obj3 = C()
obj4 = D()
obj5 = E()
obj6 = F()
obj7 = G()
obj8 = H()


obj1.methodOfA()

obj2.methodOfB()

obj3.methodOfC()

obj4.methodOfD()
obj4.methodOfA()

obj5.methodOfA()
obj5.methodOfD()
obj5.methodOfE()

obj6.methodOfA()
obj6.methodOfB()
obj6.methodOfC()
obj6.methodOfF()


obj7.methodOfA()
obj7.methodOfG()

obj8.methodOfB()
obj8.methodOfC()
obj8.methodOfH()

