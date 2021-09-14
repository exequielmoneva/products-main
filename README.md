# Proof of concept implementation of a microservice

Main module implementation for the Products microservice.

##About
This proof of concept of a microservice is based on the Event-Driven Architecture,
connecting the main module working on Flask 
with the [admin module made on Django](https://github.com/exequielmoneva/products-admin-and-DB) using RabbitMQ queues hosted on CloudAMQP.
You can use the available endpoints to retrieve all products at the DB and to create, update or delete a product and give a like to it.


Both modules run within Docker containers using MySQL as the database.

# Stack of this module:
- Python, Flask framework
- SQLAlchemy
- RabbitMQ
- Docker-compose
- MySQL

# Requirements
- Docker
- Python
- [The admin module already running](https://github.com/exequielmoneva/products-admin-and-DB)
- Your own [CloudAMQP RabbitMQ instance](https://www.cloudamqp.com/)
# Installation 
First, paste your RabbitMQ url at [consumer.py](consumer.py) and [producer.py](producer.py).

After that, simply run the following command inside the root folder:

```
docker-compose up
```

# API specification

| Task | URL | Method | Response code | Response |
|:----:|:---:|:------:|:-------------:|:--------:|
| Create an Object | localhost:8000/api/products | POST | 201 | Object created|
| Like an Object | localhost:8001/api/products/product_id/like | POST | 201 | Like applied|
| Read all entries | localhost:8000/api/products | GET | 200 | All entries |
| Read Product by id | localhost:8000/api/products/product_id | GET | 200 | Product belonging to that id |
| Update Product | localhost:8000/api/products/product_id | UPDATE | 200 | Updated product | 
| Delete Product | localhost:8000/api/products/product_id | DELETE | 200 | Status |

## Body example for the POST endpoint
```json
{
    "title":"Product name example",
    "image":"image url example"
}
```




# TO-DO
- Unit and integration tests