import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load csv files into memory to be parsed. Downloaded from https://opportunityatlas.org/
income_male = pd.read_csv('college_male.csv')
college_male = pd.read_csv('income_male.csv')
income_female = pd.read_csv('income_female.csv')
college_female = pd.read_csv('college_female.csv')
# merge the 2 dataframes together by id number
df_male = pd.merge(income_male, college_male, on=["cz", "Name"])
df_female = pd.merge(income_female, college_female, on=["cz", "Name"])

# Remove city name from rom so that it can be grouped by state name
# City names are formatted as City, State abbreviation so only the last 2 letters are needed for states
df_male.Name = df_male.Name.str[-2:]
df_female.Name = df_female.Name.str[-2:]
# Get the average staticists from each state
df_graduation_m = df_male.groupby('Name')['GraduationRate'].mean()
df_income_m = df_male.groupby('Name')['Income'].mean()
df_graduation_f = df_female.groupby('Name')['GraduationRate'].mean()
df_income_f = df_female.groupby('Name')['Income'].mean()
# merge the 2 dataframes together by name
df_male = pd.merge(df_graduation_m, df_income_m, on="Name")
df_female = pd.merge(df_graduation_f, df_income_f, on="Name")
df_male['GraduationRate'] = df_male['GraduationRate'] * 100
df_female['GraduationRate'] = df_female['GraduationRate'] * 100

# Plot the dataframes
plt.scatter(df_male["Income"], df_male["GraduationRate"], color='blue', label="Males", )
plt.scatter(df_female["Income"], df_female["GraduationRate"], color='red', label="Females")
# Make the plot pretty :)
plt.title('Average Income At Age 35 vs Graduation Rate in 2014-15')
plt.xlabel('Average Income ($)')
plt.ylabel('College Graduation Rate (%)')
plt.legend(loc='best')

# Add annotations for each plot to show the state
for k, v in df_male.iterrows():
    plt.text(v['Income'], v['GraduationRate'], k)

for k, v in df_female.iterrows():
    plt.text(v['Income'], v['GraduationRate'], k)
plt.show()