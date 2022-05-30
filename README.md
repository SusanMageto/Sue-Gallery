# Gallery

###  Author
Susan Nyabate

### Description
A personal gallery application that I display photos for others to see.

### User Stories :family:
1. View different photos that interest me.
1. Click on a single photo to expand it and also view the details of the photo. 
1. Search for different categories of photos. (ie. Travel, Food)


### How to use :rocket:
When the user opens the website, he/she will see the recent photos.
The user can also search for photos in a certian category e.g food.

### Tech used :computer: 
1. HTML and CSS
2. Python
3. Django
1. Postgres
1. Heroku for deployment

## Set up and Installation
### Prerequisites
The user will require git, django, postgres and python3.6+ installed in their machine.
To install these two, you can use the following commands
```
#git
$ sudo apt install git-all

#python3.6
$ sudo apt-get install python3.6.

#django
$ pip install django==1.11

#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
```
### Installation
1. To access this application on your command line, you need to clone it 
1. Create a requirements.txt in the root folder and copy the requirements above.
1. Install the required technologies with
`pip install -r requirements.txt`
1. Create a .env file and copy the .env code above
1. You can then run the server with:
`python3 manage.py runserver`
1. You can make changes to the db with
`python3 manage.py makemigrations photos`
`python3 manage.py migrate`
4. You can run tests:
`python3 manage.py test photos`

### Django Admin
Username: moringa
Password: Access

### Known Bugs :x:
Currently, there are no known bugs


Copyright (c) 2022 SusanNyabate