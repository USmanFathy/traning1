from bs4 import BeautifulSoup
import requests 
import pandas as pd


page = requests.get("https://arc.dev/remote-jobs") # to fetch data from this url 

page_content = page.content    #to fetch content

soup = BeautifulSoup(page_content , 'lxml')

# print(soup.prettify())

# company_name= soup.findAll('div' , class_='company-name')

# print(company_name)
# company_job= soup.findAll('a' , class_='job-title')

# print(company_job)

company= soup.findAll('div' , class_='sc-ba46ca07-0 dROrNK job-card')


comany_names = []
comany_jobs = []

for data in company:
    comany_names.append(data.find('div' , class_='company-name').text)
    comany_jobs.append(data.find('a' , class_='job-title').text)



data_jobs ={
    'company-name':comany_names , 
    'job-titles' : comany_jobs
}


dataframe = pd.DataFrame(data_jobs )

dataframe.to_csv('jobs.csv' , index=False)