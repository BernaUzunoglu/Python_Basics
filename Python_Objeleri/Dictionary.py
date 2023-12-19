#key - value 

# 41 => Kocaeli , 34 => İstanbul

sehirler = ['Kocaeli', 'İstanbul']
plakalar = [ 41,34]

print(plakalar[sehirler.index('Kocaeli')])
print(plakalar[sehirler.index('İstanbul')])

#dict = {key:value}
plakalar = {'Kocaeli':41 , 'İstanbul':34}

print(plakalar['Kocaeli'])
print(plakalar['İstanbul'])

plakalar['Ankara'] = 6
print(plakalar)


users ={
    'Berna':{
        
        'age':25,
        'roles': ['admin','user'],
        'mail':'berna@gmail.com',
        'address':'Sivas',
        'phone':'123456789'
    },
    'Banu':{
        
        'age':26,
        'roles': 'user',
        'mail':'banu@gmail.com',
        'address':'İstanbul',
        'phone':'325469'
    }
}
print(users['Berna'])
print(users['Berna']['age'])
print(users['Berna']['mail'])
print(users['Berna']['address'])
print(users['Berna']['roles'])