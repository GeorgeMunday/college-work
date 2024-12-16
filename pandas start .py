# Importing the pandas library and aliasing it as 'pd'
import pandas as pd

# Creating a DataFrame using a dictionary with data for 'Name', 'Height', and 'Qualification'
data = {
    'Name': ['John', 'Emma', 'Michael', 'Sophia'],
    'Height': [5.5, 6.0, 5.8, 5.3],
    'Qualification': ['BSc', 'BBA', 'MBA', 'BSc']
}

# Creating a DataFrame 'df' from the data dictionary
df = pd.DataFrame(data)

# Printing the DataFrame to see its contents
print(df)

# Shows the version of pandas library being used
print(pd.__version__)

# Creating a list 'a' of integers
a = [1, 7, 2]

# Converting the list 'a' into a pandas Series
myvar = pd.Series(a)

# Printing the pandas Series to view the data
print(myvar)

# Creating a dictionary 'dat' with 'calories' and 'duration' data for 3 days
dat = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# Creating a DataFrame 'df' from the 'dat' dictionary with custom row indices "day1", "day2", and "day3"
df = pd.DataFrame(dat, index = ["day1", "day2", "day3"])

# Printing the new DataFrame with the custom index
print(df)

