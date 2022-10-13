import pandas as pd
import os
print(os.getcwd())
df_degrees= pd.read_csv(r'./group-3/Resources/degrees-that-pay-back.csv')
#cleaing  the degrees data frame.
df_degrees ['Starting Median Salary'] = df_degrees ['Starting Median Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_degrees ['Starting Median Salary'] = df_degrees ['Starting Median Salary'].astype(float)

df_degrees ['Mid-Career Median Salary'] = df_degrees ['Mid-Career Median Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_degrees ['Mid-Career Median Salary'] = df_degrees ['Mid-Career Median Salary'].astype(float)

df_degrees ['Mid-Career 10th Percentile Salary'] = df_degrees ['Mid-Career 10th Percentile Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_degrees ['Mid-Career 10th Percentile Salary'] = df_degrees ['Mid-Career 10th Percentile Salary'].astype(float)

df_degrees ['Mid-Career 25th Percentile Salary'] = df_degrees ['Mid-Career 25th Percentile Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_degrees ['Mid-Career 25th Percentile Salary'] = df_degrees ['Mid-Career 25th Percentile Salary'].astype(float)

df_degrees ['Mid-Career 75th Percentile Salary'] = df_degrees ['Mid-Career 75th Percentile Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_degrees ['Mid-Career 75th Percentile Salary'] = df_degrees ['Mid-Career 75th Percentile Salary'].astype(float)

df_degrees['Mid-Career 90th Percentile Salary'] = df_degrees['Mid-Career 90th Percentile Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_degrees['Mid-Career 90th Percentile Salary'] = df_degrees['Mid-Career 90th Percentile Salary'].astype(float)

print(df_degrees.head())

#now cleaing the college data frame .
df_college= pd.read_csv(r'./group-3/Resources/salaries-by-college-type.csv')

df_college ['Starting Median Salary'] = df_college ['Starting Median Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_college ['Starting Median Salary'] = df_college ['Starting Median Salary'].astype(float)


df_college ['Mid-Career Median Salary'] = df_college ['Mid-Career Median Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_college ['Mid-Career Median Salary'] = df_college ['Mid-Career Median Salary'].astype(float)


df_college ['Mid-Career 10th Percentile Salary'] = df_college ['Mid-Career 10th Percentile Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_college ['Mid-Career 10th Percentile Salary'] = df_college ['Mid-Career 10th Percentile Salary'].astype(float)

df_college ['Mid-Career 25th Percentile Salary'] = df_college ['Mid-Career 25th Percentile Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_college ['Mid-Career 25th Percentile Salary'] = df_college ['Mid-Career 25th Percentile Salary'].astype(float)
            
            
            
df_college ['Mid-Career 75th Percentile Salary'] = df_college ['Mid-Career 75th Percentile Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_college ['Mid-Career 75th Percentile Salary'] = df_college ['Mid-Career 75th Percentile Salary'].astype(float)
            

df_college ['Mid-Career 90th Percentile Salary'] = df_college ['Mid-Career 90th Percentile Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_college ['Mid-Career 90th Percentile Salary'] = df_college ['Mid-Career 90th Percentile Salary'].astype(float)
            
 #now cleaning the region data
 
df_region= pd.read_csv(r'./group-3/Resources/salaries-by-region.csv') 
df_region ['Starting Median Salary'] = df_region ['Starting Median Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_region ['Starting Median Salary'] = df_region ['Starting Median Salary'].astype(float)


df_region ['Mid-Career Median Salary'] = df_region ['Mid-Career Median Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_region['Mid-Career Median Salary'] = df_region ['Mid-Career Median Salary'].astype(float)

df_region['Mid-Career 10th Percentile Salary'] = df_region ['Mid-Career 10th Percentile Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_region ['Mid-Career 10th Percentile Salary'] = df_region ['Mid-Career 10th Percentile Salary'].astype(float)



df_region['Mid-Career 25th Percentile Salary'] = df_region ['Mid-Career 25th Percentile Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_region ['Mid-Career 25th Percentile Salary'] = df_region ['Mid-Career 25th Percentile Salary'].astype(float)

df_region['Mid-Career 75th Percentile Salary'] = df_region ['Mid-Career 75th Percentile Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_region ['Mid-Career 75th Percentile Salary'] = df_region ['Mid-Career 75th Percentile Salary'].astype(float)
  
df_region ['Mid-Career 90th Percentile Salary'] = df_region['Mid-Career 90th Percentile Salary'].str.replace(',', '').str.replace('.', '').str.replace('$', '')
df_region ['Mid-Career 90th Percentile Salary'] = df_region ['Mid-Career 90th Percentile Salary'].astype(float)
                                                            
                                                                         
print(df_degrees.head()) 
print(df_college.head())
print(df_region.head())                                                     