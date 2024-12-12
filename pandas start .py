import pandas as pd

# Creating a DataFrame
data = {
'Name': ['John', 'Emma', 'Michael', 'Sophia'],
'Height': [5.5, 6.0, 5.8, 5.3],
'Qualification': ['BSc', 'BBA', 'MBA', 'BSc']
}
df = pd.DataFrame(data)
print(df)



#shows pandas version you are useing
print(pd.__version__)

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)



dat = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(dat, index = ["day1", "day2", "day3"])

print(df) 

