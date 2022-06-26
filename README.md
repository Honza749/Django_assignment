# Django_assignment

## Local Setup

Install required package:

```
pip install -r requirements.txt
```



Run development server locally:

```
python manage.py runserver
```

Then navigate to http://localhost:8000

## Requests
Get all objects:
```
curl -X GET http://localhost:8000
```
Get all objects with name Product:
```
curl -X GET http://localhost:8000/detail/Product/ 
```
Get data from object with name Attribute and ID 9:
```
curl -X GET http://localhost:8000/detail/Attribute/9  
```
Import object NewProduct with id: 4, price: 1254, color: blue:
```
curl -X POST \
  http://localhost:8000/import \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 8fda4f96-2de4-c955-a55b-06a8a159783a' \
  -d '{
	"NewProduct": {
		
            "id": 4,
            "price": "1254",
            "color": "blue"
    }
}'
```