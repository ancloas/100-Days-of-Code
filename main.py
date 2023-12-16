
from bs4 import BeautifulSoup
import requests

response= requests.get(url='https://news.ycombinator.com/newest', )
response.raise_for_status()
print(response.text)



def get_title_with_highest_pts_on_page(soup)





















# print(soup.prettify)

# getting first anchor tag
# print(soup.a)

# getting all elements by tag name: EX all anchor elements
# print(soup.find_all('a'))
# print([tag.get('href') for tag in soup.find_all('a')])


# getting elements by attribute
# heading = soup.find_all(attrs={'class':'heading'})
# print(heading)

# getting element by tag and element

# section_Heading = soup.find(name='h3', class_='heading')
# print(section_Heading)


# # selecting-css selector to get the element
# company_url= soup.select_one(selector='p a')   
# print(company_url)
# name=soup.select_one(selector='#name')
# print(name.string)
# headings=soup.select(selector='.heading')
# print([heading.string for heading in headings])