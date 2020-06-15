import re
import os
from os.path import expanduser  # it is used to give the home directory
home = expanduser("~")
import logging 
import sys  


#Create and configure logger 
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s INF p = %(process)d %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def create_files():
    '''
    permission denied
    if not os.path.exists('/mnt'):os.mkdir('/mnt1')
    if not os.path.exists('/mnt/xml_dir'):os.mkdir('/mnt/xml_dir')
    if not os.path.exists('/mnt/xml_dir'):os.mkdir('/mnt/xml_dir')
    '''
    if not os.path.exists(''+home+'/service/'):os.mkdir(''+home+'/service/')
    if not os.path.exists(''+home+'/service/data'):os.mkdir(''+home+'/service/data')
    if not os.path.exists(''+home+'/service/data/feed'):os.mkdir(''+home+'/service/data/feed')
    if not os.path.exists(''+home+'/service/data/feed/premierip'):os.mkdir(''+home+'/service/data/feed/premierip')
    if not os.path.exists(''+home+'/service/data/feed/premierip/new'):os.mkdir(''+home+'/service/data/feed/premierip/new')
    if not os.path.exists(''+home+'/service/data/feed/premierip/item'):os.mkdir(''+home+'/service/data/feed/premierip/item')
    if not os.path.exists(''+home+'/service/data/feed/premierip/xls'):os.mkdir(''+home+'/service/data/feed/premierip/xls')
    if not os.path.exists(''+home+'/service/data/feed/premierip/xls/PremierIP'):os.mkdir(''+home+'/service/data/feed/premierip/xls/PremierIP')
    if not os.path.exists(''+home+'/service/data/feed/premierip/logs'):os.mkdir(''+home+'/service/data/feed/premierip/logs')

def strip_html(var):
    var=' '.join(var.split()).strip()
    var=re.sub('\s*<style.*</style.*?>\s*',' ',var,re.S)
    var=re.sub('(\s*<.*?>\s*)+',' ',var,re.S)
    return var

