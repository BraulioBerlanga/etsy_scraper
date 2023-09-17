from bs4 import BeautifulSoup
import doc_handler
import requests
import lxml
import re
import time
import bs4
from selenium import webdriver
import re
import json

def scraper_dpv(url):
#url = 'https://www.etsy.com/de-en/listing/1261909727/sterling-silver-bookmark-with-wooden-box?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=bookmarks&ref=sc_gallery-2-1&frs=1&sts=1&plkey=ba5990b0c82a81421f242d7d8dd136d1a1514715%3A1261909727'
#print(url)
    chromedriver_path= "/Users/.../chromedriver"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3) #if you want to wait 3 seconds for the page to load
    page_source = driver.page_source
    soup_detail_page = bs4.BeautifulSoup(page_source, 'lxml')
    #soup_detail_page = str(soup_detail_page)
    #doc_handler.all_soup(soup_detail_page)


    # follow the steps below to understand better the websites html nested structure  

    # 1. save all soup in flat file
    #doc_handler.detail_page_soup(soup_detail_page)

    # 2. save in flata file the corresponding tag that contains all listings 
    """ lis = soup.find_all('li')
    for li in lis:
        try:
            doc_handler.listing(str(li))
        except:
            pass """

    # 3. save all values of the class property from the tag from above in a flat file
    """ lis = soup.find_all('li')
    for li in lis:
        try:
            doc_handler.listing(str(li.attrs['class']))
        except:
            pass """

    scripts = soup_detail_page.find_all('script')

    description = None
    rating_value = None
    review_count = None
    stock = None
    offer_count = None
    date_listed = None
    lowPrice = None
    highPrice = None
    price_dpv = None
    num_imgs = None
    add_url = None
    num_fav = None



    # url to check if lisitng is an add
    try:
        as_ = soup_detail_page.find_all('a',alt= 'Back to search results')
        for a in as_:
            try:
                add_url = a['href']
            except:
                add_url = None
    except:
        add_url = None

    # number of times the listing was favorited
    metas = soup_detail_page.find_all('meta')
    list_fav =[]
    list_date_listed =[]
    for meta in metas:
        try:
            if meta['content'].find('from Etsy shoppers') > 0:
                list_fav.append(re.search(r'(?<=has)[0-9]*',meta['content'].replace(' ','')).group())
                list_date_listed.append(meta['content'][-12:])
        except:
            pass

    num_fav = [x for x in set(list_fav)][0]
    date_listed = [x for x in set(list_date_listed)][0]



    for script in scripts:
        try:
            if script['type'] == 'application/ld+json':
                dict_text = script.text.replace('\n',' ').replace('\/','/').replace('@','').strip()
                dict = json.loads(dict_text)
                #print(dict)
                try:
                    description = re.sub(r"[^a-zA-Z0-9]+", " ",dict['description']).strip()
                    print('got:description')
                except:
                    pass
                try:
                    rating_value = dict['aggregateRating']['ratingValue']
                    print('got:rating_value')
                except:
                    pass
                try:
                    review_count = dict['aggregateRating']['reviewCount']
                    print('got:review_count')
                except:
                    pass
                try:
                    stock = dict['offers']['eligibleQuantity']
                    print('got:stock')
                except:
                    pass
                try:
                    offer_count = dict['offers']['offerCount']
                    print('got:offer_count')
                except:
                    pass
                try:
                    lowPrice = dict['offers']['lowPrice']
                    print('got:lowPrice')
                except:
                    pass
                try:
                    highPrice = dict['offers']['highPrice']
                    print('got:highPreice')
                except:
                    pass
                try:
                    price_dpv = dict['offers']['price']
                    print('got:price_dpv')
                except:
                    pass
                try:
                    num_imgs = len(dict['image'])
                    print('got:num_img')
                except:
                    pass
                #print(description,rating_value,review_count,stock,price_desc,num_imgs)

        except:
            pass



    # tags        
    divs = soup_detail_page.find_all('div')
    list_tags = []
    for div in divs:
        try:
            if div['class'][0] == 'tags-section-container':
                lis = div.find_all('li')
                for li in lis:
                    val = li.text.strip()
                    list_tags.append(val)
                    print('got:one_list_tags')
        except:
            list_tags.append(None)
        list_tags = list(set(list_tags))
    print('creating detail page list')
    detail_pg_lst = [description,rating_value,review_count,stock,offer_count,lowPrice,highPrice,date_listed,price_dpv,num_imgs,add_url,list_tags,num_fav]
    print(detail_pg_lst)

    return detail_pg_lst

#url = 'https://www.etsy.com/de-en/listing/1026276988/kashmiri-cushion-covers-suzani-wool?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=pillow+covers&ref=sr_gallery-2-15&bes=1&sts=1&organic_search_click=1'
#print(scraper_dpv(url))