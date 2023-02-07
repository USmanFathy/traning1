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
job_links = []
job_locations = []
job_salaries = []

for data in company:
    comany_names.append(data.find('div' , class_='company-name').text)
    comany_jobs.append(data.find('a' , class_='job-title').text)
    job_links.append(f"https://arc.dev/remote-jobs{data.find('a' , class_='job-title')['href']}")

for link in job_links:
    page_two = requests.get(link)
    page_two_content = page_two.content
    soup_2 = BeautifulSoup(page_two_content , 'lxml')
    div = soup_2.find('div' , class_= 'sc-a9bceba6-0 dtrGJF')

    locations = div.find('div' , class_='sc-b9ad719a-0 jzcFMg').div.div.span.text
    job_locations.append(locations)

    salary = div.find('div' , class_='sc-b9ad719a-0 eSLzbJ').div.div.span.text
    job_salaries.append(salary)



data_jobs ={
    'company-name':comany_names , 
    'job-titles' : comany_jobs,
    'job-links' : job_links,
    'job-location' : job_locations,
    'job-salary' : job_salaries,
}


dataframe = pd.DataFrame(data_jobs )

dataframe.to_csv('jobs.csv' , index=False)