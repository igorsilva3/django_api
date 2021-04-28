<!-- Header -->
<h1 align="center">DJANGO API</h1>

<!-- Description  -->
> *This is a Django project. A API of product manager, where it has the register of product, updates of data product, the exclusion of product and th listing of all products added. :stars:*

<!-- Table of contents -->
## :pushpin: Table of Contents
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [How to run](#how-to-run)
- [License](#license)

<!-- Technologies -->
## Technologies
* [Python](https://www.python.org/) 
* [Django Framework](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)

<!-- Prerequisites -->
## Prerequisites
* Python 3.5+ installed in your machine

- #### Creation of virtual environment
	```bash
	# Installing virtualenv for Python
	$ python3 -m pip install virtualenv

	# Creating your virtual environment
	$ python3 -m virtualenv name-of-your-virtual-environment

	# Activating virtual environment
	$ source name-of-your-virtual-environment/bin/activate 
	```


- #### Installing dependencies
	```bash
	# Enter in folder of project
	$ cd django_api/
	``` 
  	Make sure what the virtual environment this activated.
	```bash
	# Installing requirements
	(name-of-your-virtual-environment) $ pip install -r requirements.txt
	``` 

- #### Migrating database
	```bash
	# Migrating tables for database
	(name-of-your-virtual-environment) $ python manage.py migrate
	``` 

## How to run

With your virtual environment enabled
```bash
# Running the application
(name-of-your-virtual-environment) $ python manage.py runserver
```

<!-- License -->
## License

Released in 2020 :closed_book: License.

Made with :heart: by [Igor Silva](https://github.com/igorsilva3).
This project is under the [MIT license](./LICENSE).

Give a :star: if this project helped you!
