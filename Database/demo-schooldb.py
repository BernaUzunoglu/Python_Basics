import mysql.connector
from datetime import datetime
from connection import connection #connection.py dosyası import edildi


class Student:
    connection = connection
    mycursor = connection.cursor()
    def __init__(self,studentNumber,name,surname,birthdate,gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):#instance fonk.
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)#Student sınıfındaki cursor kullandığımız için sınıftan çağırıyoruz.

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('Hata:', err)
        finally:
            Student.connection.close()
    
    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)#Student sınıfındaki cursor kullandığımız için sınıftan çağırıyoruz.

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('Hata:', err)
        finally:
            Student.connection.close()

# ahmet = Student("102","Ahmet","Yılmaz",datetime(2005, 5, 17),"E")
# ahmet.saveStudent()# tek bir öğrenci kayıtıt için oluşturulan nesne

ogrenciler = [
    ("401","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    ("402","Ali","Can",datetime(2005, 6, 17),"E"),
    ("403","Canan","Tan",datetime(2005, 7, 7),"K"),
    ("404","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    ("405","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    ("406","Ali","Cenk",datetime(2003, 8, 25),"E")
]

Student.saveStudents(ogrenciler)



