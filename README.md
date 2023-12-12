# Welcome to my Supreme Django Project



Let's check the requirements :

- ```Python 3.10 or newer```
- ```Pip installed``` 

Installation steps :
- 
 
 Lest begin by creating our working enviroment.

  1. create a folder and name it Django.
  2. cd into that folder using CMD or your prefered terminal.
  3. you need to create your virtual enviroment:
  
  - run this command : ```python -m venv my_env``` ( or any prefered name)
  - activate your venv by running the command : ```source env/bin/activate```

   4. now that we have our venv activated lets install Django by running the command :
   
        ```pip install -r requirements.txt```

Project Beggining :
 -

Let's create our Project File :
 
  - cd into your new project folder 
  - run the command : ```python manage.py runserver```
  
  If everything is set up correctly by clicking on this Ip you should be redirected at your own project (check this link http://127.0.0.1:8000/)

  Let's create our first Application 

   - run the command : ```python manage.py startapp polls``` 
   - also run the following command in order to check all the migrations / changes that have taken place inside your folders directory : ```
   python manage.py migrate``` .

After those steps you can start typing your on code in order to create your own custom API or clone my code and start experiment with it.


   


