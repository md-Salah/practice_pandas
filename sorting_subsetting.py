import pandas as pd


d = {"A" : ["John","Deep","Julia","Kate","Sandy"], 
                     "MonthSales" : [25,30,35,40,45]}

# Create DataFrame
df =pd.DataFrame(d)

# Sorting values by MonthSales columns
# sorted_df = df.sort_values("MonthSales")
# print(sorted_df.head())

# Sorting values based on multiple columns
# sorted_df = df.sort_values(["A", "MonthSales"], ascending=[True, False])
# print(sorted_df.head())


# Subsetting Columns
# Selecting columns that you need, Suppose you need column "A" only
# new_df = df["A"]
# print(new_df.head())

# Select multiple columns, Suppose you need column "A" and "MonthSales"
# new_df = df[["A", "MonthSales"]]
# print(new_df.head())


# subsetting/ Filtering Rows
# new_df = df[ df["A"] == "Julia" ] 
# print(new_df)

# Concate conditions
# new_df = df[ (df["A"] == "Julia") & (df["MonthSales"] > 30) ] 
# print(new_df)

# isin() method to check multiple or
# names = ["John", "Deep", "Julia"]
# new_df = df[ df["A"].isin(names) ]
# print(new_df)
