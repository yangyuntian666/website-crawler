# -*- coding:utf-8 -*-
# Author: Yang

import requests
import re
import time
import pymysql

def get_one_page(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }
    response = requests.get(url,headers = headers)
    if response.status_code == 200 :
        return response.text
    return None

def get_strips(html):
    strip = re.compile('<li id="(\d+)".*?quotation-merchant-name"><a.*?>(.*?)</a></p>.*?'
                       'address.*?<a.*?>(.*?)</a>.*?'
                       '近30日訂購.*?<p>(\d+)次</p>.*?累積訂購.*?<p>(.*?)次</p>.*?評分.*?<b>(.*?)</b>.*?'
                       'text-price-number.*?>(.*?)</span>',re.S)
    items = re.findall(strip,html)
 #   print(items)
    return items


def conn_mysql(text):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', db='yang_db')
    cursor = conn.cursor()
    cursor.execute('USE yang_db')
    sql1 = '''create table store_data_HUAWEIp30pro(
            product_id varchar(64) not null,
            store varchar(255) not null,
            address varchar(255),
            order_30 varchar(64),
            all_order varchar(64),
            evaluation varchar(64),
            price varchar(64) not null);'''
    cursor.execute(sql1)
    try:
        sql2 = "insert into store_data_HUAWEIp30pro(product_id," \
               "store,address,order_30,all_order,evaluation,price) " \
               "values(%s,%s,%s,%s,%s,%s,%s)"
        cursor.executemany(sql2,text)
        conn.commit()
    except:
        conn.rollback()


def main(list_items,page):
    #url = 'https://www.price.com.hk/product.php?p=419717&gp=10&page=' + str(page)  #Samsung Note 10+
    #url = 'https://www.price.com.hk/product.php?p=388164&gp=10&page=' + str(page)  #Samsung S10
    url = 'https://www.price.com.hk/product.php?p=396047&gp=10&page=' + str(page)  #HUAWEI P30 Pro
    html = get_one_page(url)
    strips = get_strips(html)
    for strip in strips:
        print(strip)
        list_items.append(strip)
    print("page %d is done."%(page))
    return list_items


if __name__ == '__main__':
    list_items = []
    for i in range(3):
        fins = main(list_items,page=i + 1)
        time.sleep(1)
    print(fins)
    conn_mysql(fins)

