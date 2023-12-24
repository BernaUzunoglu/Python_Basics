# Inheritance (Kalıtım ): Miras alma
#Person => name , lastname , age , eat() , run(), drink() 
# Student(Person) , Teacher(Person)  python da clasın nesnesi üretilirken () içerisine inherit olacak sınıfın adı yazlıyor.
#Animal = > Dog(Animal), Cat(Animal )


class Person():
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')

    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self, fname , lname, number):
        Person.__init__(self,fname,lname) # ifade yazlarak temel sınıfın constructurunı ezmeyi engellemiş olduk
        self.studentNumber = number
        print('Student Created') 

    #override
    def who_am_i(self):
       print('I am a student') # temel sınıfın metodunu ezdik ovveride yaptık.
    

    def sayHello(self):
        print('Hello I am student')


class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname )#super olunca self göndermeye gerek yok
        self.branch = branch

    def who_am_i(self):
       print(f'I am a {self.branch} teacher')


p1 = Person('Berna','Uzunoğlu')
s1 = Student('Lina' , 'Aksoy', 12354) # Student classı Person dan inherit olarak oluşturulduğu için içerisindeki kalıtım ile aktarılmış oldu.
t1 = Teacher('Banu','Aksoy','Math')

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eat()
s1.eat()
s1.sayHello()

print(p1.firstName + ' '+ p1.lastName)
print(s1.firstName + ' '+ s1.lastName +' Numarası : '+ str(s1.studentNumber))
print(t1.firstName + ' '+ t1.lastName +' ' +t1.branch)
