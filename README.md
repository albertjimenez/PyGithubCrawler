# Python Test from Albert Sendrós Jiméenez

### REST Webserver 

There are two endpoints:
- `localhost:5000/` Targets the first exercise with a plain query
- `localhost:5000/extra` Targets the second exercise with the plain query plus the extra information composed by the owner
of the repository and the language + percentage usage used in the project.

### DISCLAIMER:

The testing for the Controller functionality of the webserver has been delegated to Postman App.

### USAGE:

Just run `pip install -r requirements` on the root folder and then run `python main.py`


### Input for the first endpoint 
`
{
  "keywords": [
    "openstack",
    "nova",
    "css"
  ],
  "proxies": [
    "194.126.37.94:8080",
    "13.78.125.167:8080"
  ],
  "type": "Repositories"
}`

### Input for the second endpoint
`
{
  "keywords": [
    "python",
    "django-rest-framework",
    "jwt"
  ],
  "proxies": [
    "194.126.37.94:8080",
    "13.78.125.167:8080"
  ],
  "type": "Repositories"
}` 


