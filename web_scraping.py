from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# idhar define kia ki yeh wale url to request bhejna hai
myurl='https://www.newegg.com/p/pl?d=best+graphic'  # net nhi tha tore reequest nhi ja pa rahi  thi,because we want net for sending the request

# opening up and grabing the page

uClient=uReq(myurl) # uReq is a files inside the urllib package .so it will request for url,and save it into uClient

page_html=uClient.read()   # it will read the html data,so we need something for storing the html soure ,thaT  why we will store it into a vasriablee_html

# so abh pura ek page_htmlmai script save hogya hai so ,abh link ko close kar denge

   #  after that we have to close it,because tune us link ko hit kia and uske piche ka pura script leylia
uClient.close() # ek bar request bheja n fir close kar deyna ka
# html parsing
# page_soup mai pura file html ke form mai save ho gya
page_soup=soup(page_html,'html.parser')  #becaue page_html mai sabh filehai,so uske andar script hai,eslia humusko lenge and than usko htmlparse mai convert karenge # as i called soup function it willcal the beautifulsoup which is inside the bs4
#page_soup.h1



#    .close()
# grabs each produts
# page soup mai pura file aa gya,abh usmai operation hoga
containers=page_soup.findAll("div",{"class" :"item-container"})  # will the help of this it will differnt the one product to another

# to open file in a csv
# usko kaise ptA CHAYEGA KI FILE KE TYPE KYA HAI BY EXTENSION
filename="produts.csv"  # it will be create file of this name and by using the extension also it will make it csv of this file
#2 pehle mai file create kar dia abh usfile mai write karna hai,toh usfile ko write mode mai open karenge
f=open(filename,'w')  # file ko write mode mai on kar dia,
# abh jabh v esfile mai kuch likhna hai file ka variable ka nam jo esmai F dia hai,usko write method call karo and write karo
headers="brand\n"    # so it will take a header in the above

f.write(headers)    # with the header word file ko pta chala ki header mai kya likhna hai
for container in containers:
	#print(containers)
	#break
	brand=container.a.img["title"]
	#print(brand)
	#break
	#brand=container.div.div.div.div.a["title"]  # tag ke andar tag ko . sey represent karenfe,and fir value mil gya use tag ke andar toh [] mai value deydeng
#	print(brand)
#	break  #<div class="item-container">

	#title_continer=container.a#findAll("a",{"class":"item_title"})
	#print(title_continer)
	#break
#	/*
#	produts_name=title_container[0].text  # because the name is inside the the title_container

#	ship_container=container.findAll("li",	{"class":"price-ship"})
#	shipping=ship_container[0].text.strip()  # strip will remove the space from front and from back

	print("brand::", brand)
#	print("produts_name::",+produts_name)
#	print("shipping::",+shipping)


	f.write(brand+","+"\n")   # container sey leyga brand mai ,n with the help of write method wah jo humne file ko write mode
	# mai open kia hai usmai write kareyga

f.close()

  #note agar piche csv file open hai n tum yeh prgm run kar rahey ho toh error ayegga
  # eslia hamesha pehle csv file close karo than run this progrm