import pandas as pd


# The dataset is available on the IBM Cloud at the below url.

dataset_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"


# Load the data available at dataset_url into a dataframe.

df_survey = pd.read_csv(dataset_url)


# ## Explore the data set

# It is a good idea to print the top 5 rows of the dataset to get a feel of how the dataset will look.

# Display the top 5 rows and columns from your dataset.

df_survey.head(5)


# ## Find out the number of rows and columns

# Start by exploring the numbers of rows and columns of data in the dataset.
 
# Print the number of rows in the dataset.

rows_nr = len(df_survey.axes[0])
print(rows_nr)


# Print the number of columns in the dataset.

cols_nr = len(df_survey.axes[1])
print(cols_nr)


# ## Identify the data types of each column
# 

# Explore the dataset and identify the data types of each column.
# 

# Print the datatype of all columns.

df_survey_types = [df_survey.dtypes]
print(df_survey_types)


# Print the mean age of the survey participants.

avg_age = df_survey['Age'].mean()
avg_age


# The dataset is the result of a world wide survey. Print how many unique countries are there in the Country column.

unique_countries = df_survey['Country'].unique()
unique_countries


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
