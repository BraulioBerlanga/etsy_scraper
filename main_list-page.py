from bs4 import BeautifulSoup
import doc_handler
import requests
import lxml
import re
import time
import bs4
from selenium import webdriver
import re
from main_detail_page import scraper_dpv
from datetime import date

# number of pages
start = 1
end = 10

for page in range(1,end+1):
    chromedriver_path= "/Users/.../chromedriver"
    driver = webdriver.Chrome()
    url = "https://www.etsy.com/de/search?q=bookmarks&ref=pagination&page="+str(page)
    driver.get(url)
    time.sleep(3) #if you want to wait 3 seconds for the page to load
    page_source = driver.page_source
    soup_list_page = bs4.BeautifulSoup(page_source, 'lxml')

    # follow the steps below to understand better the websites html nested structure  

    # 1. save all soup in flat file
    """ doc_handler.output(soup) """

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


    n = 0
    lis = soup_list_page.find_all('li')

    for li in lis:
        print(1)
        #reset values
        item_id = None
        page_num = None
        position_num = None
        shop_id = None
        item_link = None
        target = None
        title = None
        img_text = None
        video = None
        rating = None
        shop_reviews = None
        price_from = None
        price = None
        discount = None
        seller_batch = None
        free_delivery = None
        try:
            if li['class'][0] == 'wt-list-unstyled':
                print(2)
                divs = li.find_all('div')
                for div in divs:
                    try:
                        if div['class'][0] == 'js-merch-stash-check-listing':
                            print(3)
                            try:
                                shop_id = div['data-shop-id']
                                print('got:shop_id')
                            except:
                                pass
                            as_ = div.find_all('a')
                            print(4)
                            for a in as_:
                                try:
                                    if a['class'][0]=='listing-link':
                                        print(5)
                                        n = n+1 
                                        # get the sraper order, the order follows how the lists where display in the soup, not in the website interface
                                        order = n
                                        try:
                                        # itme_id
                                            item_id = a['data-listing-id']
                                            print('got:item_id')
                                            print(item_id)
                                        except:
                                            pass
                                        try:
                                        # page_num
                                            page_num = a['data-page-num']
                                            print('got:page_num')
                                        except:
                                            pass
                                        try:
                                        # position_num    
                                            position_num = a['data-position-num']
                                            print('got:position_num')
                                        except:
                                            pass
                                        try:
                                        # item_link
                                            item_link = a['href']
                                            print('got:item_link')
                                        except:
                                            pass 
                                        try:
                                        # target
                                            target = a['target']
                                            print('got:target_a')
                                        except:
                                            pass 
                                        try:
                                        # title
                                            title = re.sub(r"[^a-zA-Z0-9]+", " ", a['title']).strip()
                                            print('got:title')
                                        except:
                                            pass
                                        # img_text
                                        imgs = a.find_all('img')
                                        print('got:imgs')
                                        for img in imgs:
                                            img_text = img['alt']
                                            print('got:img_text')
                                        # vids
                                        vids = a.find_all('video')
                                        for vid in vids:
                                            try:
                                                video = vid['aria-label']
                                                print('got:video')
                                            except:
                                                pass
                                        # rating
                                        inputs = a.find_all('input')
                                        for input in inputs:
                                            try:
                                                if input['name'] == 'initial-rating':
                                                    rating=input['value']
                                                    print('got:ratings')
                                            except:
                                                pass
                                        # shop_reviews
                                        spans =a.find_all('span')
                                        for span in spans:
                                            try:
                                                if span['class'][0] == 'wt-text-caption':
                                                    shop_reviews = span.text.strip()
                                                    print('got:shop_reviews')
                                            except:
                                                pass
                                        #price
                                        price_list = []
                                        for span in spans:
                                            try:
                                                if span['aria-hidden'] == 'true':
                                                    price_from = span.text.strip()
                                                    print('got:price_from')
                                            except:
                                                pass
                                        ps = a.find_all('p')
                                        for p in ps:
                                            try:
                                                if p['class'][1] == 'lc-price':
                                                    spans_p = p.find_all('span')
                                                    for span_p in spans_p:
                                                        try:
                                                            price_list.append(str(span_p.text).strip())
                                                        except:
                                                            price_list.append(None)
                                            except:
                                                price_list.append(None)
                                        price = price_list[len(price_list)-1]
                                        print('got:price')
                                        #seller batch
                                        for p in ps:
                                            try:
                                                if p['class'][0] == 'wt-text-caption-title':
                                                    seller_batch = p.text 
                                            except:
                                                pass
                                        #discount
                                        for p in ps:
                                            try:
                                                if p['class'][1] == 'search-collage-promotion-price':
                                                    spans_p = p.find_all('span')
                                                    for span_p in spans_p:
                                                        try:
                                                            if span_p['class'][0]=='wt-text-grey':
                                                                discount = span_p.text.strip()
                                                        except:
                                                            pass
                                            except:
                                                pass
                                        #free delivery
                                        for p in ps:
                                            try:
                                                if p['class'][0] == 'wt-text-truncate':
                                                    spans_p = p.find_all('span')
                                                    for span_p in spans_p:
                                                        try:
                                                            if span_p['class'][1]=='wt-text-body-smallest' or span_p['class'][1]=='wt-text-body-smallest' or span_p['class'][1]=='wt-badge--small':
                                                                free_delivery = span_p.text.strip()
                                                        except:
                                                            pass
                                            except:
                                                pass
                                        try:
                                            # scrape detail page
                                            print('scraping_detail_page')
                                            detail_pg_lst = scraper_dpv(item_link)
                                            print(detail_pg_lst)
                                        except:
                                            detail_pg_lst = [None,None,None,None,None,None,None,None,None,None,None,None,None]
                                    

                                    #creat and store values in a diccitionary
                                    print('creating listing-dict')
                                    listing_dict =  {
                                                "date": str(date.today()),
                                                "order": order,
                                                "item_id": item_id,
                                                "page_num": page_num,
                                                "iteration": page,
                                                "position_num": position_num,
                                                "item_id": item_id,
                                                "shop_id": shop_id,
                                                "item_link": item_link,
                                                "target": target,
                                                "title": title,
                                                'img_text':img_text,
                                                'video':video,
                                                'rating':rating,
                                                'shop_reviews':shop_reviews,
                                                'price_from':price_from,
                                                'price':price,
                                                'seller_batch':seller_batch,
                                                'discount':discount,
                                                'free_delivery':free_delivery,
                                                #[description,rating_value,review_count,stock,offer_count,lowPrice,highPrice,price_dpv,num_imgs,list_tags]
                                                'description': detail_pg_lst[0],
                                                'rating_value': detail_pg_lst[1],
                                                'review_count': detail_pg_lst[2],
                                                'stock': detail_pg_lst[3],
                                                'offer_count': detail_pg_lst[4],
                                                'lowPrice': detail_pg_lst[5],
                                                'highPrice':detail_pg_lst[6],
                                                'date_listed': detail_pg_lst[7],
                                                'price_dpv': detail_pg_lst[8],
                                                'num_img': detail_pg_lst[9],
                                                'add_url':detail_pg_lst[10],
                                                'tags': detail_pg_lst[11],
                                                'num_fav':detail_pg_lst[12]
                                        }
                                    print('listing_dict created')
                                    # save values in a flat file
                                    print(listing_dict)
                                    doc_handler.Doc_handler(listing_dict)
                                    #doc_handler.Doc_handler(detail_pg_dict)
                                except:
                                    pass
                    except:
                        pass 
        except:
            pass

# store all soup in a flat file for debbuging
#doc_handler.list_page_soup(soup)
