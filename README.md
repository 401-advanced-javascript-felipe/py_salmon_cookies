# py_salmon_cookies

### Author: Felipe Delatorre

### Links and Resources
* [submission PR](https://github.com/401-advanced-javascript-felipe/py_salmon_cookies/pull/1)
* [front-end](https://py-salmoncookies.herokuapp.com/)

### Setup
* `MONGODB_URI` - URL to the running mongo instance/db

#### Running the app
* `FLASK_APP=main.py FLASK_DEBUG=1 python3 -m flask run`
* Endpoint: `/`
  * Home
* Endpoint: `/sales`
  * Page for sale predictions and to display data from database
* Endpoint: `/create`
  * Creates hard coded data into the Mongo DB
* Endpoint: `/destroy`
  * Deletes Mongo db data

