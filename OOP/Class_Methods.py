class Circle :
    pi = 3.14

    #class object attributes
    def __init__(self,yaricap = 1):
       self.yaricap = yaricap

    

    #methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap
    

    def alan_hesapla(self):
        return  self.pi * (self.yaricap ** 2)
    
c1 = Circle() #yaricap =  1
c2 = Circle(5)

print(f'Alan : {c1.alan_hesapla()} ve Cevre : {c1.cevre_hesapla()}')
print(f'Alan : {c2.alan_hesapla()} ve Cevre : {c2.cevre_hesapla()}')