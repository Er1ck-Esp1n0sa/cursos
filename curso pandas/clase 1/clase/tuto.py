import pandas as pd

data = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

print(data)

data2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
'Sue': ['Pretty good.', 'Bland.']})

print("--------------------------------------------------------")
print(data2)

data3 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

print("--------------------------------------------------------")
print(data3)

data4=pd.Series([1, 2, 3, 4, 5])

print("--------------------------------------------------------")
print(data4)

data5=pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

print("--------------------------------------------------------")
print(data5)