# To Do App
This is a simple To Do app that allows a user add items, check off items as done using a checkbox and prioritise items by clicking a star icon.

As a bonus, users can clear the list by clicking the `Clear List` button.

This app is built using Django. It uses Django Rest Framework to create a Restful API which allows fetching and deleting the list as well as updating and adding individual items.

The front end of the application is implemented using HTML, CSS, JavaScript and jQuery. 

The app uses the default SQLite database to store list items.

### API
```
To fetch a list, make a GET request to /api/todoitem/
To clear a list, make a DELETE request to /api/todoitem/
To add an item, make a POST request to /api/todoitem/
To update an item, make a PATCH request to /api/todoitem/<id>/
```

### How to Run the App
Change to the root folder of the app.

The first time you run it, install Python requirements by running the command: 
```
pip install -r requirements.txt
```

Next, run migrations using command: 
```
python manage.py migrate
```

Start the server using the command: 
```
python manage.py runserver 0.0.0.0:8002
```

Access the app by visiting http://localhost:8002 in a browser.



