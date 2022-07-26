def tempconversion(t):
    
    class Temperature:
        def __init__(self,t):
            self.a = t
            self.f = (round((self.a *(1.8)),2) + 32.00)
            self.b = t 
            self.c =   (round((self.b -32.00)/1.8,2))
        # YOUR CODE GOES HERE
        def convertcelsius(self):
            
            print(str(self.c) + " degree celsius")
            
            
        def convertfahrenheit(self):
            print(str(round((self.a *(1.8)),2) + 32.00) + " degree fahrenheit")
            
        
    temp=Temperature(t)
    temp.convertcelsius()
    temp.convertfahrenheit()