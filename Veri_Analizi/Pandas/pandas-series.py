import pandas as pd
import numpy as np

#data
numbers = [20,30,40,50]
letters = ['a','b','c','d']
scalar = 5
dict = {'a':10,'b':20,'c':30,'d':40}
random_numbers = np.random.randint(10,100,10)

# pandas_series = pd.Series()
pandas_Numbereries = pd.Series(numbers,['a','b','c','d'])#numpy da seriler homojen olması gerekirken pandasda homojen olmaya bilir.
print(pandas_Numbereries)
pandas_series = pd.Series(letters,[5,6,7,8])# elemen sayısı kadar index girilmeli
print(pandas_series)
pandas_series = pd.Series(scalar,[0,1,2,3]) # [] içerinde index bilgisi verdik.0,1,2,3, indexlere 5 değerini atadı 
print(pandas_series)
pandas_series = pd.Series(dict)
print(pandas_series)
pandas_series = pd.Series(random_numbers)
print(pandas_series)

result = pandas_Numbereries.iloc[0] #iloc ile satır ve sutun index numarasını belirtiyoruz.
print(result)
result = pandas_Numbereries.iloc[:2]
print(result)
result = pandas_Numbereries.iloc[-2:]
print(result)
result = pandas_Numbereries['a']
print(result)
result = pandas_Numbereries[['a','c']]
print(result)

result = pandas_Numbereries.ndim # => 1 boyulu dizi
print(result)
result = pandas_Numbereries.dtype 
print(result)
result = pandas_Numbereries.shape 
print(result)

result = pandas_Numbereries.sum()
print(result)
result = pandas_Numbereries.max()
print(result)
result = pandas_Numbereries.min()
print(result)
result = pandas_Numbereries + pandas_Numbereries
print(result)
result = pandas_Numbereries + 50
print(result)
result = np.sqrt(pandas_Numbereries)
print(result)
result = pandas_Numbereries >= 50
print(result)
result = pandas_Numbereries % 2 == 0 
print(result)


opel2018 = pd.Series([20,30,40,10],['astra','corsa','mokka','insignia'])
opel2019 = pd.Series([40,30,20,10],['astra','corsa','grandland','insignia'])

total = opel2018 + opel2019
print(total['astra'])
# print(total['combo']) # olmayan bilgi hata verir