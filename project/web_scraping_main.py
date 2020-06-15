# there are two way by which we can scrab a website
# 1 use the api
# 2 html web Scraping  using some like bs4
import requests
from bs4 import BeautifulSoup

url="https://www.amazon.in/s?k=best+laptop&ref=nb_sb_noss_2"#"https://www.amazon.in"#"https://www.codewithharry.com/"   ##https://www.amazon.in/
# step 1 get the html  # by sending request ,url chahiyeh toh request kareyga ,ki please give me your url
r=requests.get(url)
htmlcontent=r.content # with the help of this method all the content of the page wil store in a variable of name htmlcontent
#print(htmlcontent)

# step 2 parse the html

soup=BeautifulSoup(htmlcontent,'html.parser')
#print(soup.prettify)  # with the help of prettify
# step 3 htmltree traversal the html

title=soup.titleeep
print(title)
