import re
import codecs
import urllib.request
import os
import pandas as pd
import scrawl as sc
import sys
from scrawl import logger
from scrawl import strip_html
from os.path import expanduser
from datetime import datetime
import time
start_time=datetime.now().strftime("%H:%M:%S")
home = expanduser("~")
sc.create_files()
site='fbm'
site_url='www.fbm.com'
input_file = '/mnt/xml_dir/'+site+'_products'
feed_dir=''+home+'/service/data/feed/premierip/new/'+site+''
if not os.path.exists(feed_dir):
    os.mkdir(feed_dir)
item_dir=''+home+'/service/data/feed/premierip/item/'+site+''
if not os.path.exists(item_dir):
    os.mkdir(item_dir)
output_file=''+home+'/service/data/feed/premierip/xls/PremierIP/'+site+'.csv'
count=0
prod_count=0
flag=sys.argv[0]

#function
def fetch_and_save(url,filename):
    if os.path.exists(filename):
        logger.info('File exists {}'.format(filename))
    else:
        req=urllib.request.Request(
                url,
                data=None,
                headers={
                    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
                       }
        )
        f=urllib.request.urlopen(req)
        source=f.read().decode('utf-8')
        with open(filename,'w') as f:
            f.write(source)

def download_prof():
    if os.path.exists(input_file) : 
        os.remove(input_file) 
    pg=1
    global count
    while True:
        url='http://www.fbm.com/who-we-are/page/{}/?search%5Bkeyword%5D=&view=all'.format(pg)
        filename='{}/{}__{}.html'.format(feed_dir,site,pg)
        pg+=1
        try:fetch_and_save(url,filename)
        except:continue
        with codecs.open(filename,'r','utf-8') as f: con=f.read()
        if re.findall('class="no-results">',con):break
        content=re.search('role="button">.*?class="person-listing__link(.*?)class="rainmaker-pagination">',con,re.S).group(1)
        li=content.split('class="person-listing__link')
        for i in li:
            prod_url=re.search('<a\s*href="(.*?)"',i,re.S).group(1).strip()
            prod_id=re.search('\.com\/(.*?)\/',i,re.S).group(1).strip()
            if prod_url=='' or prod_id=='' : continue
            ifilename='{}/{}_item_{}.gz'.format(item_dir,site,prod_id)#grr_item_alice-denenberg.gz
            with open(input_file,'a') as f:f.write('FILE: {} URL: {}\n'.format(ifilename,prod_url))
            count+=1
            logger.info('{} profiles found'.format(count))
            try:
                fetch_and_save(prod_url,ifilename)
                logger.info('Url {}'.format(prod_url))
                logger.info('Filename {} '.format(ifilename))
            except:
                logger.info('Unable to fetch {}'.format(prod_url))
                continue
#download_prof()

def process_listing():
    with open(input_file,'r') as f:
        name_list,email_list,phone_list,title_list,location_list,url_list=[],[],[],[],[],[]
        global prod_count
        for product in f:
            File=re.search('FILE:\s*(.+?) URL',product).group(1).strip()
            prod_id=re.search('item_(.*?).gz',product).group(1).strip()
            url=re.search('URL:\s*(.+?)\n',product).group(1).strip()
            if File!='':
                with codecs.open(File,'r','utf-8') as f:
                    pg=f.read()
                
                name=re.search('"page-title">(.*?)<',pg)
                if name : name= strip_html(name.group(1)) 
                
                email=re.search('"email":"(.*?)"',pg) 
                if email : email = strip_html(email.group(1))

                phone=re.search('"telephone":"(.*?)"',pg)
                if phone : phone=strip_html(phone.group(1))

                title=re.search('"jobTitle":"(.*?)"',pg)
                if title : title=strip_html(title.group(1))
                
                location=re.search('ProfessionalService","name":"(.*?)"',pg)
                if location : location=strip_html(location.group(1))
                
                name_list.append(name)
                email_list.append(email)
                phone_list.append(phone)
                title_list.append(title)
                location_list.append(location)
                url_list.append(url)
                prod_count+=1
                logger.info('Completed {} products'.format(prod_count))
    dic={
        'Site Url':site_url,
        'Name':name_list,
        'Url':url_list,
        'Email':email_list,
        'Phone':phone_list,
        'Title':title_list,
        'Location':location_list

        }
    df=pd.DataFrame(dic)
    df.fillna(value='N/A', inplace=True)
    df.to_csv(output_file,index=False)
#process_listing()


if flag=='1':
    logger.info("Fetcher started ...") 
    download_prof()
    end_time=datetime.now().strftime("%H:%M:%S")
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(end_time, FMT) - datetime.strptime(start_time, FMT)
    logger.info("\n\nFetcher finished with {} profiles in {} seconds \n".format(count,tdelta)) 
    logger.info("Parser started ...")
    process_listing()
    end_time=datetime.now().strftime("%H:%M:%S")
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(end_time, FMT) - datetime.strptime(start_time, FMT)
    logger.info("\n\n{} site finished {} listing in {} seconds\n".format(site,count,tdelta))
elif flag=='2':
    logger.info("Fetcher started ...")
    download_prof()
    end_time=datetime.now().strftime("%H:%M:%S")
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(end_time, FMT) - datetime.strptime(start_time, FMT)
    logger.info("\n\nFetcher finished with {} profiles in {} seconds\n".format(count,tdelta))
elif flag=='3':
    logger.info("Parser started ...")
    process_listing()
    end_time=datetime.now().strftime("%H:%M:%S")
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(end_time, FMT) - datetime.strptime(start_time, FMT)
    logger.info("\n\n{} site finished {} listing in {} seconds\n".format(site,count,tdelta))

