# -*- coding:utf-8 -*-
# Author: Yang

import requests
import re
import pandas as pd
import matplotlib.pyplot as plt
import time

def get_one_page(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }
    response = requests.get(url,headers = headers)
    if response.status_code == 200 :
        return response.text
    return None

def get_strips(html):
    strip = re.compile('data-add-compare-name="(.*?)"',re.S)
    items = re.findall(strip,html)
    return items

def product_count(product_brand):
    result = pd.value_counts(product_brand)
    print(result)
    return result

def show_pie(result):
    dict1 = dict(result)
    labels = list(dict1.keys())
    sizes = list(dict1.values())
    plt.figure()
    plt.pie(sizes,labels=labels, autopct='%1.2f%%',
            shadow = True,pctdistance = 0.6)
    plt.title("Phone Pie chart")
    plt.axis('equal')
 #   plt.legend(loc='upper left', bbox_to_anchor=(-0.3, 1))
    plt.show()


def action(num,page):
    url = 'https://www.price.com.hk/category.php?c=100005&gp=10&page=' + str(page)
    html = get_one_page(url)
    strips = get_strips(html)
    for strip in strips:
        num = num + 1
        print(strip)
        product_all.append(strip)
        product_all_split.append(strip.split()[0])
    print("already got {} phones information".format(num))
    return num

if __name__ == '__main__':
    num_product = 0
    product_all = []
    product_all_split = []
    for i in range(40):
        num_product = action(num_product,page=i + 1)
    #    time.sleep(1)
    print(product_all)
    print(product_all_split)
    result = product_count(product_all_split)
    show_pie(result)
