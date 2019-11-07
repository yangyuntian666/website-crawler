# -*- coding:utf-8 -*-
# Author: Yang

import pymysql
import numpy
import pandas as pd
import matplotlib.pyplot as plt

#plt.rcParams['font.sans-serif'] = ['SimHei']

def read_data():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', db='yang_db')
    cursor = conn.cursor()
    cursor.execute('USE yang_db')
    cursor.execute('select * from store_data_HUAWEIp30pro')
    all_data = cursor.fetchall()
    return all_data


def store_price(all_data):
    store = []
    price = []
    for data in all_data:
        #print(data[6])
        store.append(data[1])
        price.append(data[6])
#    print(Series(price))  #+序号    series()一维数组型对象
    data = {
        'store' : store,
        'price' : price
    }
    d = pd.DataFrame(data)    # dataframe()二维矩阵型数据表对象<class 'pandas.core.frame.DataFrame'>
    print("HUAWEI P30 Pro (8+256GB)")
    print("--------1. store and price--------")
    print(d)   #store+price
    print("--------  2. data sort    ---------")
    k = d['price']
    print(k.sort_values())

    data_int = []
    for p in price:
        each = p.replace(',', '')
        data_int.append(each)
    prices = list(map(int, data_int))      #list里的string转成int
    print("Minimum price is HK$%s"%(numpy.min(prices)))
    print("Maximal price is HK$%s"%(numpy.max(prices)))
    print("Average price is HK$%s"%(numpy.mean(prices)))
    print("Median price is HK$%s" %(numpy.median(prices)))

    print("--------3. unique data price-------")
    print(k.sort_values().unique())
    print("--------4. unique data price counts-------")
    print(k.value_counts())
    print(k.describe())
    return store,prices

def sort_values(store,price):
    dict1 = dict(zip(store,price))
 #   print(dict1)    #{'store' : values}
    tuple1 = sorted(dict1.items(), key= lambda k:k[1])
    d = dict(tuple1)
    return d

def store_order_price(all_data):
    store = []
    order_30 = []
    order_all = []
    evaluation = []
    price = []
    for data in all_data:
        data = list(data)
        store.append(data[1])
        if data[3]  == '':
            data[3] = '0'
        order_30.append(data[3])
        if data[4] == '':
            data[4] = '0'
        if "萬" in data[4]:
            data[4] = data[4].replace('萬','0000').replace('.','')
        order_all.append(data[4])
        if data[5] == '':
            data[5] = '0'
        evaluation.append(data[5])
        price.append(data[6])
    order_30_int = list(map(int,order_30))
    print(order_30_int)
    order_all_int = list(map(int,order_all))
    print(order_all_int)
    evaluation_int = list(map(float,evaluation))
    print(evaluation_int)
    return store,order_30_int,order_all_int,evaluation_int

def order_eval(o_30,o_all,eval):
    o_all_1 = [num // 100 for num in o_all]
    dict1 = dict(zip(eval,o_30))
    tuple1 = sorted(dict1.items(), key=lambda item:item[0])
    dict2 = dict(tuple1)
    print(dict2)
    dict3 = dict(zip(eval,o_all_1))
    tuple2 = sorted(dict3.items(), key=lambda item: item[0])
    dict4 = dict(tuple2)
    print(dict4)
    return dict2,dict4


def show_columnr_pic(d):
    plt.figure(figsize=(20, 5))  # 长宽
    plt.bar(d.keys(), d.values(),color = 'green', label='price')
    plt.title("HUAWEI P30 Pro (8+256GB)")
    plt.xlabel("store")
    plt.ylabel("price(HK$)")
    plt.ylim((4900,5500))
    for a,b in zip(d.keys(),d.values()):
        plt.text(a,b,b,ha = 'center',fontsize = 9)
    plt.gcf().autofmt_xdate()  # 日期倾斜
    plt.legend()  # 图例
    plt.grid()  # 网格
    plt.show()

def show_order_eval_pic(s,o_30,o_all,e):
    plt.figure(figsize=(20,5))    #长宽
    o_all_1 = [num//100 for num in o_all]    #除100
    plt.plot(s,o_30,color = 'red',label = 'order-30days',linewidth = 1)
    plt.plot(s,o_all_1,color='blue',label='order-all(*100)',linewidth=1)
    plt.title("Store information(HUAWEI P30 Pro (8+256GB))")
    plt.xlabel("store")
    plt.ylabel("number")
    for a,b in zip(s,o_30):    #标数字
        plt.text(a,b,b,ha = 'center',fontsize = 8,color = 'red')
    for a,b in zip(s,o_all_1):
        plt.text(a,b,b,ha = 'center',fontsize = 8,color = 'blue')
    plt.gcf().autofmt_xdate()  #日期倾斜
    plt.legend()    #图例
    plt.grid()    #网格
    plt.show()


def show_scatter_pic(d1,d2):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)    #1*1网格，第一个子图
    ax1.scatter(d1.keys(),d1.values(),s = 20,color='red',label = 'store-30days',marker='*')
 #   ax1.scatter(d2.keys(),d2.values(),s = 20,color='blue',label='store-all(*100)', marker='+')
    ax1.set_title("Store orders and evaluations(HUAWEI P30 Pro (8+256GB))")
    plt.xlabel('evaluations')
    plt.ylabel('orders')
    plt.legend()
    plt.show()

def main():
    all_data = read_data()
    data_store_and_price = store_price(all_data)
    d = sort_values(data_store_and_price[0],data_store_and_price[1])
    show_columnr_pic(d)

    k = store_order_price(all_data)
    show_order_eval_pic(k[0],k[1],k[2],k[3])

    o_e = order_eval(k[1],k[2],k[3])
    show_scatter_pic(o_e[0],o_e[1])



if __name__ == '__main__':
    main()
