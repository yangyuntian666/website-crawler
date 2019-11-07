# The Website Crawler And Data Analysis About Digital product

This is my second project in my course named Open Sourse Tool for Data Science.
I write the website crawler about the price of digital product in Hong Kong. The original web is: https://www.price.com.hk/ .

There are three fuctions to realize my thoughts:
1. Get the names of all products.
2. Get the store information for each product.
3. Get daily changes in the price of the product.

The webpage of digital product: https://www.price.com.hk/category.php?c=100005&gp=10&page=1 . 

Document description:

-- product_req_show.py

   Get all the product names in the first sixty page and visualize the pie picture about product brand distribution.
   
-- store_data_request.py

   Get the store information for each product and store in Mysql database named yang_db.
   Store the data parameters as follows:
   product_id,
   store,
   address,
   order_30,
   all_order,
   evaluation,
   price.
   
-- store_data_show.py

   Read the content in my database from yang_db.
   Visualize the data and find potential law.
   
-- date_price_req_show.py

   Get daily changes in the price of the product and visualize it.
   
I try my best to do some meaningful thing and i wish you to give me some instructions. Contact me: 97317026@qq.com .

Think you for reading!

