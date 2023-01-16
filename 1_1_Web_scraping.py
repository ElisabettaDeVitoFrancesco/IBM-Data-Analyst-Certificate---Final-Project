# ## Extract information from the given web site
# You will extract the data from the below web site: <br> 
#this url contains the data you need to scrape
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"


# The data you need to scrape is the **name of the programming language** and **average annual salary**.<br> It is a good idea to open the url in your web broswer and study the contents of the web page before you start to scrape.

# Import the required libraries
from bs4 import BeautifulSoup
import requests

# Download the webpage at the url

data_lang = requests.get(url).text


# Create a soup object

soup_lang = BeautifulSoup(data_lang, "html5lib")


# Scrape the `Language name` and `annual average salary`.

import pandas as pd

data_lang = []

data_lang_header = []

headers = soup_lang.find_all("table")[0].find("tr")

for header in headers:
    data_lang_header.append(header.get_text())

HTML_data_lang = soup_lang.find_all("table")[0].find_all("tr")[1:]
 
for element in HTML_data_lang:
    sub_data_lang = []
    for sub_element in element:
        sub_data_lang.append(sub_element.get_text())
        
    data_lang.append(sub_data_lang)

dataFrame_lang = pd.DataFrame(data = data_lang, columns = data_lang_header)

dataFrame_lang


# Save the scrapped data into a file named *popular-languages.csv*
dataFrame_lang.to_csv('popular-languages.csv')


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

# |  Date (YYYY-MM-DD) |  Version | Changed By  |  Change Description |
# |---|---|---|---|
# | 2020-10-17  | 0.1  | Ramesh Sannareddy  |  Created initial version of the lab |
# 

#  Copyright &copy; 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01).
# 
