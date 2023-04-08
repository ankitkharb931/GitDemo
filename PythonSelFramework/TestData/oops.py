#function when used inside a class --- it is called a method

class Calculator:
    num =100   # num is a class variable
    def __init__(self,a,b):    # default constructor  #self , a,b are 3 parameters
        # instance variable will agian change it's value and become 4,5
        self.firstNumber =a
        self.secondNumber =b
        # firstnumber , secondNUmber are 2 instance variable

        print("a")

    def getData(self):      #as inside a class it is a method
        print("i")

    def Sum (self):
       return self.firstNumber + self.secondNumber  # neeche jo 2,3 values di hui hai vo aake a,b ka place lengi
    #to call  this method we have to create object for this class
    #for that you have to come outside to the class

obj = Calculator(2,3)     #new object is  created  , 2,3  are 2 arguments
obj.getData()
obj.num

obj1 = Calculator(4,5)
obj1.getData()
print(obj1.num)

#default constructor will be called automatically here
Lecture -21 -3:35

# instance variable differs for each object

#variables can never be called by its name
-- self.secondNumber----for instance variable
    Calculator.num ----for class variable-----although --self.num  can also be used
    


