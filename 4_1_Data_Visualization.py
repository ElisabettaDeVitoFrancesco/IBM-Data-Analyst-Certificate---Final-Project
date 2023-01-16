import pandas as pd


# Load the dataset into a dataframe.

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv")
df.head()


# ## Distribution

# ### Determine how the data is distributed

# The column `ConvertedComp` contains Salary converted to annual USD salaries using the exchange rate on 2019-02-01.
 
# This assumes 12 working months and 50 working weeks.

# Plot the distribution curve for the column `ConvertedComp`.

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
mpl.style.use('ggplot')

#mean_comp = df['ConvertedComp'].mean()
#df['ConvertedComp'].fillna(mean_comp, inplace=True)
#df['ConvertedComp'] = df['ConvertedComp'].fillna(mean_comp)
#df['ConvertedComp'].isnull().sum()

sns.distplot(df['ConvertedComp'], hist=False)
plt.title('Distribution curve of annual compensation in $')
plt.xlabel('Compensation ($)')
plt.ylabel('Density')
#plt.xticks(range(0,2000000))
plt.show()

# Plot the histogram for the column `ConvertedComp`.

plt.hist(df['ConvertedComp'], bins = 20)
plt.title('Histogram of annual compensation in $')
plt.xlabel('Compensation ($)')
plt.ylabel('Frequency')


# What is the median of the column `ConvertedComp`?

median_comp = df['ConvertedComp'].median()
median_comp #57745.0


# How many responders identified themselves only as a **Man**?

df['Gender'].value_counts().to_frame() #10480


# Find out the  median ConvertedComp of responders identified themselves only as a **Woman**?

df_woman = df[df['Gender'] == "Woman"]
median_comp_women = df_woman['ConvertedComp'].median()
median_comp_women #57708.0

df_reduced = df[['ConvertedComp', 'Gender']]
df_gender = df_reduced.groupby('Gender').describe()
#df_gender = df.groupby('Gender')
df_gender.head()


# Give the five number summary for the column `Age`?

df_summary = df.describe()
df_age_summary = df_summary['Age'].to_frame()
df_age_summary[3:8]


# Plot a histogram of the column `Age`.

plt.hist(df['Age'], bins = 10)
plt.title('Frequency of developer jobs based on age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.xticks(range(0,100,10))


# ## Outliers
# ### Finding outliers

# Find out if outliers exist in the column `ConvertedComp` using a box plot?

mean_comp = df['ConvertedComp'].mean()
df_NoNan = df
df_NoNan['ConvertedComp'].fillna(mean_comp, inplace=True)
df_NoNan['ConvertedComp'] = df_NoNan['ConvertedComp'].fillna(mean_comp)
df_NoNan['ConvertedComp'].isnull().sum()
plt.boxplot(df_NoNan['ConvertedComp'])
plt.title('Converted compensation in $')
plt.ylabel('Compensation ($)')

df_summary = df.describe()
df_ConvComp_summary = df_summary['ConvertedComp']
df_ConvComp_summary[3:8]


# Find out the Inter Quartile Range for the column `ConvertedComp`.

#(Nan were not removed)

q1_convcomp = df['ConvertedComp'].quantile(0.25) #26868.0

q3_convcomp = df['ConvertedComp'].quantile(0.75) #100000.0

IQR_convcomp = q3_convcomp - q1_convcomp #73132.0


# Find out the upper and lower bounds.

min_ConvComp = df_ConvComp_summary[3] #0
max_ConvComp = df_ConvComp_summary[7] #2000000.0

q1_convcomp = df['ConvertedComp'].quantile(0.25) #26868.0
q3_convcomp = df['ConvertedComp'].quantile(0.75) #100000.0


# Identify how many outliers are there in the `ConvertedComp` column.

convcomp = df['ConvertedComp']
count_out_up_convcomp = convcomp[convcomp > (q3_convcomp+1.5*IQR_convcomp)].count()
count_out_up_convcomp #811

count_out_down_convcomp = convcomp[convcomp < (q1_convcomp-1.5*IQR_convcomp)].count()
count_out_down_convcomp #0

q3_convcomp+(1.5*IQR_convcomp) #245136.0


# Create a new dataframe by removing the outliers from the `ConvertedComp` column.

wisker_up_convcomp = q3_convcomp+1.5*IQR_convcomp #245136.0

df2 = df.drop(df[df['ConvertedComp'] >= wisker_up_convcomp].index)
df2

mean_comp2 = df2['ConvertedComp'].mean()
df2_NoNan = df2
df2_NoNan['ConvertedComp'].fillna(mean_comp2, inplace=True)
df2_NoNan['ConvertedComp'] = df2_NoNan['ConvertedComp'].fillna(mean_comp2)
df2_NoNan['ConvertedComp'].isnull().sum()
plt.boxplot(df2_NoNan['ConvertedComp'])
plt.title('Converted compensation in $')
plt.ylabel('Compensation ($)')

q1_convcomp2 = df2['ConvertedComp'].quantile(0.25) 
q3_convcomp2 = df2['ConvertedComp'].quantile(0.75) 
IQR_convcomp2 = q3_convcomp2 - q1_convcomp2

convcomp2 = df2['ConvertedComp']
count_out_up_convcomp2 = convcomp2[convcomp2 > (q3_convcomp2+1.5*IQR_convcomp2)].count()
count_out_up_convcomp2 #68

count_out_down_convcomp2 = convcomp2[convcomp2 < (q1_convcomp2-1.5*IQR_convcomp2)].count()
count_out_down_convcomp2 #0

wisker_up_convcomp2 = q3_convcomp2+1.5*IQR_convcomp2
wisker_up_convcomp2 #209689.0

df3 = df2.drop(df2[df2['ConvertedComp'] >= wisker_up_convcomp2].index)
df3

mean_comp3 = df3['ConvertedComp'].mean()
df3_NoNan = df3
df3_NoNan['ConvertedComp'].fillna(mean_comp3, inplace=True)
df3_NoNan['ConvertedComp'] = df3_NoNan['ConvertedComp'].fillna(mean_comp3)
df3_NoNan['ConvertedComp'].isnull().sum()
plt.boxplot(df3_NoNan['ConvertedComp'])
plt.title('Converted compensation in $')
plt.ylabel('Compensation ($)')

df2['ConvertedComp'].median() #52704.0 #57828.0

df3['ConvertedComp'].median() #57349.0

df2['ConvertedComp'].mean() #59883.20838915799 #66462.39312380234

df3['ConvertedComp'].mean() #65446.30706357025

avg_age = df['Age'].mean() #30.778894788947888
df_age_NoNan = df
df_age_NoNan['Age'].fillna(avg_age, inplace=True)
df_age_NoNan['Age'] = df_age_NoNan['Age'].fillna(avg_age)
df_age_NoNan['Age'].isnull().sum()
plt.boxplot(df_age_NoNan['Age'])
plt.title('Age summary')
plt.ylabel('Age')

plt.boxplot(df3_NoNan['Age'])


# ## Correlation

# ### Finding correlation

# Find the correlation between `Age` and all other numerical columns.

#df3 = df3.fillna(0.0)
df3_numeric = df3.select_dtypes(include=np.number)

df3.plot(kind='scatter', x='Respondent', y='Age', color='r')

df3_numeric.corr().style.background_gradient(cmap="Blues")

df3.plot(kind='scatter', x='Age', y='CompTotal', color='g')    

df.plot(kind='scatter', x='ConvertedComp', y='Age', color='b')

df.plot(kind='scatter', x='WorkWeekHrs', y='Age')

df.plot(kind='scatter', x='CodeRevHrs', y='Age')


# ## Authors
# 

# In[ ]:





# Ramesh Sannareddy
# 

# ### Other Contributors
# 

# Rav Ahuja
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
# | ----------------- | ------- | ----------------- | ---------------------------------- |
# | 2020-10-17        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |
# 

# Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2022-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 
