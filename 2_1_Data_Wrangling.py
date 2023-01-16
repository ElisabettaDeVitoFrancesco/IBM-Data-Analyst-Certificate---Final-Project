# Import pandas module.


import pandas as pd


# Load the dataset into a dataframe.

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv")


# ## Finding duplicates

# In this section you will identify duplicate values in the dataset.

#  Find how many duplicate rows exist in the dataframe.

duplicates = df[df.duplicated()]
duplicates_nr = len(duplicates.axes[0])
duplicates_nr
len(df[df['Respondent'].duplicated()])


# ## Removing duplicates

# Remove the duplicate rows from the dataframe.

df.drop_duplicates(keep=False, inplace=True)


# Verify if duplicates were actually dropped.

df[df.duplicated()]

len(df.axes[0])


# ## Finding Missing values

# Find the missing values for all columns.

missing_data = df[df.isnull()]
missing_data
df.isnull()
df.isnull().sum().sum()


# Find out how many rows are missing in the column 'WorkLoc'

df['WorkLoc'].isnull().sum()

df['EdLevel'].isnull().sum()

df['Country'].isnull().sum()


# ## Imputing missing values

# Find the  value counts for the column WorkLoc.

work_loc_counts = df['WorkLoc'].value_counts().to_frame()
work_loc_counts

employment_counts = df['Employment'].value_counts().to_frame()
employment_counts

UndergradMajor_counts = df['UndergradMajor'].value_counts().to_frame()
UndergradMajor_counts

ConvertedComp_counts = df['ConvertedComp'].value_counts().to_frame()
ConvertedComp_counts


# Identify the value that is most frequent (majority) in the WorkLoc column.

#make a note of the majority value here, for future reference
# Office
# Employed full-time


# Impute (replace) all the empty rows in the column WorkLoc with the value that you have identified as majority.

df['WorkLoc'] = df['WorkLoc'].fillna('Office')


# After imputation there should ideally not be any empty rows in the WorkLoc column.

# Verify if imputing was successful.

df['WorkLoc'].isnull().sum()


# ## Normalizing data

# There are two columns in the dataset that talk about compensation.
# 
# One is "CompFreq". This column shows how often a developer is paid (Yearly, Monthly, Weekly).
# 
# The other is "CompTotal". This column talks about how much the developer is paid per Year, Month, or Week depending upon his/her "CompFreq". 
# 
# This makes it difficult to compare the total compensation of the developers.
# 
# In this section you will create a new column called 'NormalizedAnnualCompensation' which contains the 'Annual Compensation' irrespective of the 'CompFreq'.
# 
# Once this column is ready, it makes comparison of salaries easy.
# 

# <hr>
# 

# List out the various categories in the column 'CompFreq'

df['CompFreq'].unique()

df[ 'CompFreq'].value_counts().to_frame()


# Create a new column named 'NormalizedAnnualCompensation'. Use the hint given below if needed.

CompFreq = df['CompFreq'].tolist()
type(CompFreq)
CompTotal = df['CompTotal'].tolist()
type(CompTotal)


NormalizedAnnualCompensation = []
for i in range(len(CompFreq)):
    if CompFreq[i] == "Yearly":
        NormalizedAnnualCompensation.append(CompTotal[i])
    elif CompFreq[i] == "Monthly":
        NormalizedAnnualCompensation.append((CompTotal[i]) * 12)
    elif CompFreq[i] == "Weekly":
        NormalizedAnnualCompensation.append((CompTotal[i]) * 52)
    else:
        NormalizedAnnualCompensation.append("Nan")
NormalizedAnnualCompensation
df["NormalizedAnnualCompensation"] = NormalizedAnnualCompensation
df

df["NormalizedAnnualCompensation"].median()


# ## Authors
# 

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

#  Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 
