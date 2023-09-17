# etsy_scraper

Scraper based on a search url. The scraper takes listing page values information and detail page values.

## Description

The scraper runs on the following url: https://www.etsy.com/de/search?q=bookmarks&ref=pagination&page=. Extract values and save them in varaibles, after the scraper has fully scraped 
a item creates a dictionary and stores the value under a key. Example below.
Values in dictionary:

valued scraped| 
------------- |
date          |
order         |
item_id       |
page_num      |
iteration     |
position_num  |
item_id       |
shop_id       |
item_link     |
target        |
title         |
img_text      |
video         |
rating        |
shop_reviews  |
price_from    |
price         |
seller_batch  |
discount      |
free_delivery |
description   |
rating_value  |
review_count  |
stock         |
offer_count   |
lowPrice      |
highPrice     |
date_listed   |
price_dpv     |
num_img       |
add_url       |
tags          |
num_fav       |
num_img       |
add_url       |
tags          |
num_fav       |

### Dependencies
* BeautifulSoup [documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* requests
* lxml

## Authors

braulioberlanga@gmail.com




### etsy_scraper output example: 
Scraper based on a search url. The scraper takes listing page values information and detail page values.
Check results under item_attr***
{"date": "2023-08-26", "order": 1, "item_id": "1524417053", "page_num": "1", "iteration": 1, "position_num": "1", "shop_id": "45211838", "item_link": "https://www.etsy.com/de-en/listing/1524417053/4pcs-aesthetic-printable-bookmarks?click_key=b387dad4439e30f22f2bff243233a63ac1d77944%3A1524417053&click_sum=770f2457&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=bookmarks&ref=search_grid-670624-1-1&pro=1&dd=1", "target": "etsy.1524417053", "title": "4pcs Aesthetic Printable Bookmarks Inspired by Shatter Me", "img_text": "4pcs Aesthetic Printable Bookmarks Inspired by 'Shatter Me' By Tahereh Mafi | Print & Cut | Digital Dwn | PDF, PNG | Book-inspired | BookTok", "video": "Product video", "rating": null, "shop_reviews": null, "price_from": "\u20ac3.92", "price": "1.57", "seller_batch": null, "discount": "(60% off)", "free_delivery": null, "description": "Set of 4 bookmarks inspired by 39 SHATTER ME 39 by Tahreh Mafi Ready to print bookmark Digital download Print cut Size 2x6 inches Single side print Actual product colors might be slightly different from the pictures Add your personal touch with customized text tassels ribbon glitter and more to create unique gifts and crafts Easily personalize the pages before printing using apps like Canva or Photoshop Unleash your creativity and make unforgettable creations Effortlessly mark pages in books magazines and printed materials It is conveniently designed for on the go readers and adds a stylish flair to your reading experience Perfect for students bookworms and avid readers it helps you stay organized and effortlessly track multiple books Say goodbye to folding corners or losing your place with this handy tool PDF sheet of bookmarks ready to print CMYK 4 PNG files best for digital use customization Once your purchase is finalized you can access the files from the Purchases tab on Etsy or through the email receipt if you checked out as a Guest Certain files might be compressed in a zipped folder format requiring you to know how to open them on your computer These resources are available for commercial use exclusively for physical printed products Reselling of digital files or images in edited or unedited form is strictly prohibited Kindly refrain from sharing or redistributing the digital files or images", "rating_value": null, "review_count": null, "stock": 998, "offer_count": null, "lowPrice": null, "highPrice": null, "date_listed": "19 Aug, 2023", "price_dpv": "3.29", "num_img": 5, "add_url": "https://www.etsy.com/de-en/search?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=bookmarks&ref=return_to_search&pro=1&dd=1&plkey=b387dad4439e30f22f2bff243233a63ac1d77944%3A1524417053&explicit=1&q=bookmarks", "tags": ["custom bookmarks", "digital bookmarks", "bookmark", null, "book inspired", "quote bookmarks", "bookmarks set", "print and cut", "digital", "book lover gifts", "printable bookmarks", "book nerd", "ready to print", "book accessories"], "num_fav": "10"}

