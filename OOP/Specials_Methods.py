mylist = [1,2,3]
myString = 'my string'

print(len(mylist)) # type => class
print(len(myString)) #type => class

class Movie():
    def __init__(self,title,director,duration) :
        self.title = title
        self.director = director
        self.duration = duration

        print('Movie objesi oluşturuldu.')

    def __str__(self): # str metodunu yazman önce print ile instance alınan nesneyi yazdırınca bellekteki tutulduğu adres yazdırılıyordu.
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print('Film silindi')


m = Movie('film adı','yönetmen adı', 120)

print(mylist)
print(m)

print(len(mylist))
print(len(m))

del m
print(m)