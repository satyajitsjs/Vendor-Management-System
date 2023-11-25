# Vendor-Management-System

# 1st Step:-
pip install virtualenv
virtualenv envsmart
.\envsmart\Scripts\activate
pip install -r .\requierment.txt
cd .\vendor_project\
python.exe .\manage.py runserver


# Test in Postman

# Register Api 
http://127.0.0.1:8000/api/register

"username":"aaaaaaa",
"email":"aaaaaa@gmail.com",
"password":"aaaa",
"phone_number": 0000000000

register through this field 

# Login Api For generate Token

"email" : "aaaa@gmail.com",
"password":"aaaa"


# Use Token for authentication in header 
Token yourtoken


# Create the Vendor
Api :- http://127.0.0.1:8000/api/vendors 
POST

{
    "name":"satyajit",
    "contact_details":"7787998637",
    "address":"bajapur,kaktapur,puri",
    "vendor_code":"satya143",
    "on_time_delivery_rate":4.8,
    "quality_rating_avg":4.8,
    "average_response_time":4.7,
    "fulfillment_rate":5.0

}

# Get the Vendos 
Api :- http://127.0.0.1:8000/api/vendors
GET

# Get the perticular Vendoor 
Api :- http://127.0.0.1:8000/api/vendors/2
GET

# Update the perticual Vendor 
Api :- http://127.0.0.1:8000/api/vendors/2
PUT

# Delete The Perticualr vendor 
Api :- http://127.0.0.1:8000/api/vendors/2
DELETE


# Create the purchase_orders
Api:- http://127.0.0.1:8000/api/purchase_orders
POST

{
    "po_number": 123,
    "vendor" : 1,
    "delivery_date": "2023-11-29",
    "items" : "Laptop,Keyboards",
    "quantity": 7,
    "quality_rating" :"5.0"
}

# Get the purchase_orders
Api:- http://127.0.0.1:8000/api/purchase_orders
GET


# Get the perticular purchase_orders
Api:- http://127.0.0.1:8000/api/purchase_orders/1
GET

# Update the perticular purchase_orders
Api:- http://127.0.0.1:8000/api/purchase_orders/1
PUT

# Delete the perticular purchase_orders
Api:- http://127.0.0.1:8000/api/purchase_orders/1
DELETE


# Get the Vendor Whole ratings and review
Api :- http://127.0.0.1:8000/api/vendors/1/performance
GET
