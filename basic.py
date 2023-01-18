import pandas as pd


d = {"A" : ["John","Deep","Julia","Kate","Sandy"], 
                     "MonthSales" : [25,30,35,40,45]}

# Create DataFrame
df =pd.DataFrame(d)

# Print Head
# print(df.head())

# Print info
# print(df.info())

# Print Some Common Statistics Information [count, mean, min, max, 50%, 25%]
# print(df.describe())


# Pandas has 3 main components. [1. values, 2. columns, 3. index]
# print values (Attribute): Returns 2D numpy array
# print(df.values)

# Print columns: 
# print(df.columns)

# Print rows: Object of RangeIndex class
# print(df.index)
# print(df.index.stop)