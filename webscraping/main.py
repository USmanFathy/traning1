from bs4 import BeautifulSoup

import pandas as pd



with open('webscraping/index.html' ,'r') as html_file :
    soup = BeautifulSoup(html_file ,features='lxml')



# print(soup.prettify())


# title = soup.title.text

# print(title)


# div = soup.find('div' , class_='css-footer' )
# print(div.prettify())


# div = soup.find('div' , class_='css-footer' )
# head_div = div.h2.text

# print(head_div)



# div = soup.find('div' , class_='css-footer' )
# head_link = div.a['href']

# print(head_link)



# divs = soup.findAll('div' , class_='css-content' )
# divs_titles = []
# divs_descriptions = []
# divs_linkes = []
# for div in divs :
#     divs_titles.append(div.h2.text)
#     divs_descriptions.append(div.p.text)
#     divs_linkes.append(div.a['href'])


# print(divs_titles)
# print(divs_descriptions)
# print(divs_linkes)


divs = soup.findAll('div' , class_='css-content' )
divs_titles = []
divs_descriptions = []
divs_linkes = []
for div in divs :
    divs_titles.append(div.h2.text)
    divs_descriptions.append(div.p.text)
    divs_linkes.append(div.a['href'])



my_data = {
    "titles" : divs_titles,
    "descriptions" : divs_descriptions,
    "linkes" : divs_linkes,
}


df = pd.DataFrame(my_data)


df.to_csv('my_data.csv' , index=False)