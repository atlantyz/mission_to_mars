#!/usr/bin/env python
# coding: utf-8

# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://redplanetscience.com/'
browser.visit(url)

browser.is_element_present_by_css('div.list_text', wait_time=1)


html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


slide_elem.find('div', class_='content_title')


news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p



url = 'https://spaceimages-mars.com'
browser.visit(url)


full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


df.to_html()


url = 'https://marshemispheres.com/'

browser.visit(url)


hemisphere_image_urls = []

for i in range(4):
    hemispheres = {}
    browser.find_by_css('a.product-item h3')[i].click()
    element = browser.find_link_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()

url = 'https://marshemispheres.com/'
browser.visit(url)

html = browser.html
img_soup = soup(html, 'html.parser')


hemisphere_image_urls = []

links = browser.find_by_css('a.product-item img')

for i in range(len(links)):
    hemispheres = {}

    browser.find_by_css('.description > a.product-item h3')[i].click()

    element = browser.find_link_by_text('Sample').first

    img_url = element['href']

    title = browser.find_by_css("h2.title").text
    hemispheres["title"] = title
   
    hemispheres["img_url"] = img_url
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()


# 5. Quit the browser
#browser.quit()

