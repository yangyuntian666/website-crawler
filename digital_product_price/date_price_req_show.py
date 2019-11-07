# -*- coding:utf-8 -*-
# Author: Yang


import requests
import re
import matplotlib.pyplot as plt

def get_dateprice_source(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def parse_price(html):
    parrent = re.compile('{"x":(.*?),"y":(.*?)}')
    items = re.findall(parrent,html)
    items_2 = []
    [items_2.append(i) for i in items if not i in items_2]   #列表去重
    print(items_2)
    v1 = []
    k1 = []
    for items_2_list in items_2:
        k = items_2_list[0].strip('"')   #字符串去引号
        k1.append(k)     #全部日期list
        v = items_2_list[1].strip('"')
        v = float(v)
        v1.append(v)     #全部价格list
    k2 = k1[:int(len(k1)/2)]
    k3 = k1[:int(len(k1)/2)]
    v2 = v1[:int(len(v1)/2)]
    v3 = v1[int(len(v1)/2):]
    d1 = dict(zip(k2,v2))
    print(d1)
    """
    for key, value in d1.items():
        print('{key}:{value}'.format(key = key, value = value))
    """
    d2 = dict(zip(k3,v3))
    print(d2)
    return d1,d2

def show_pic(d1,d2):
    plt.figure(figsize=(20,5))    #长宽
    plt.plot(list(d1.keys()),list(d1.values()),color = 'red',label = 'goods',linewidth = 2)
    plt.plot(list(d2.keys()),list(d2.values()),color = 'blue',label = 'smuggled goods',linewidth = 2)
    plt.title("HUAWEI P30 Pro (8+256GB)")
    #plt.title("Samsung Galaxy S10 (8+128GB)")
    plt.xlabel("date")
    plt.ylabel("price(HK$)")
    for a,b in zip(d1.keys(),d1.values()):    #标数字
        plt.text(a,b,b,ha = 'center',fontsize = 5)
    for a,b in zip(d2.keys(),d2.values()):
        plt.text(a,b,b,ha = 'center',fontsize = 5)
    plt.gcf().autofmt_xdate()  #日期倾斜
    plt.legend()    #图例
    plt.grid()    #网格
    plt.show()

def main():
    url = 'https://www.price.com.hk/product.php?p=396047&ct=history'  #p30 pro
    #url = 'https://www.price.com.hk/product.php?p=388164&ct=history'   #S10
    html = get_dateprice_source(url)
    data_list = parse_price(html)
    show_pic(data_list[0],data_list[1])

if __name__ == '__main__':
    main()