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
curl -X GET \
  http://localhost:8000/ \
  -H 'cache-control: no-cache' \
  -H 'postman-token: 579ba179-dd23-38d3-ea28-6ca915916b0d'
```
Get all objects with name Attribute:
```
curl -X GET \
  http://localhost:8000/detail/Attribute \
  -H 'cache-control: no-cache' \
  -H 'postman-token: 00da0493-db3d-229d-dc9b-5657ac081421'
```
Get data from object with name Attribute and ID 9:
```
curl -X GET \
  http://localhost:8000/detail/Attribute/9 \
  -H 'cache-control: no-cache' \
  -H 'postman-token: 54d2dafa-1dec-c2ae-009d-3c86a7d471ba'
```
Import object NewProduct with id: 4, cena: 1254, barva: modra:
```
curl -X POST \
  http://localhost:8000/import \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: ac5acc08-9a48-cd1e-3095-e2e64ab9eca4' \
  -d '{
	"NewProduct": {
		
            "id": 4,
            "cena": "1254",
            "barva": "modra"
    }
}'
```