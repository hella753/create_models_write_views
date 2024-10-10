# Create Models Write Views

## Description
This project stores Musical instruments store data in json.
Project uses Django and sqlite3 database.

Project Structure:
```
create_models_write_views/
├── create_models_write_views
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media
├── order
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
├── store
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md

```

Database name: `db` <br>
Tables created: `store_category`, `store_product`, `store_product_product_category`(association table) and `order_order`<br>

`store_product` uses many-to-many relationship and is connected to `store_category` on **product_category**
`store_category` uses recursive (many-to-one relationship to itself) for **parent_category**<br>
`order_order` uses many-to-one relationships and is connected to `store_product` and `User` on **product_id** 
and **order_customer**

Table Structures:

**store_category:**

| id | category_name | category_description | parent_category_id |
|----|---------------|----------------------|--------------------|
| 1  | _name_        | _description_        | _id_               |


**store_product:**

| id | product_name | product_description | product_image | product_price |
|----|--------------|---------------------|---------------|---------------|
| 1  | _name_       | _description_       | _image_       | _price_       |


**store_product_product_category:**

| id | product_id   | category_id   |
|----|--------------|---------------|
| 1  | _product_id_ | _category_id_ |


**order_order:**

| id | order_date | order_status | product_quantity | order_total | order_customer | order_address | order_customer_id | product_id_id |
|----|------------|--------------|------------------|-------------|----------------|---------------|-------------------|---------------|
| 1  | _date_     | _status_     |   _quantity_     | _total_     | _customer_     | _address_     | _id_              | _id_          |


For testing purposes there are 8 products, 9 categories and 2 orders records in the database <3


## **Components** ##
* **store** - This app contains the models(Product and Category) and 4 views for the store.
* **order** - This app contains the model(Order) and 2 views for the orders.
* **media** - All user uploaded images go to the media folder.
* **db.sqlite3** - Database file.

## **Features** ##
* **Category** - Can be accessed at `/` or `/store/` Displays the categories data in json.
* **Category Detail Page** - Can be accessed at `/store/{category_id}/` or `/{category_id}/` Displays the category information in json.
* **Product** - Can be accessed at `/product` Displays all products data in json.
* **Product Detail Page** - Can be accessed `/product/{product_id}` and Displays the information about the individual Product in json.
* **Order Page** - Can be accessed at `/order/` Displays short info of the orders in json.
* **Order Detail Page** - Can be accessed at `/order/{order_id}/` Displays the details of individual order in json.
* **Admin Panel** - Can be accessed at `/admin/`. Default username: `admin`, password: `admin`.
* **Database** - sqlite3 database is used.

## Dependencies
* **Python 3.X**
* **Django 5.1.1**
* **Pillow 10.4.0**

## Usage
Clone the repository:
```bash
git clone https://github.com/hella753/create_models_write_views.git
cd create_models_write_views
```
To install the dependencies, use the following command in your terminal:
```bash
pip install -r requirements.txt
```
To run the development server, use the following command in your terminal:
```bash
python manage.py runserver
```
To access the application, open your browser and go to http://127.0.0.1:8000/

