## Django Recipes
As an ntroduction, we want to get familiar with creating a new Django application.  
Create a new application that serves recipes from different authors, much like our demo application does for news. Intended layout:  

An index page that lists all titles of the loaded recipes.  
Each title is a link that takes you to a single page with the content of that recipe.  
Each detail view for a recipe has the author name, along with all the information for the recipe arranged in a reasonable format.  
Clicking on the author's name should take you to an Author Detail page, where you can see a list of all the recipes that Author has contributed to.  
Make editing all of the models accessible through the admin panel only.  

We have three types of pages:  
a simple list view, a recipe detail view, and an author detail view.

## Getting Started

Python 3.8, latest version of Django (3.0.2 as of this writing)  

Start a project with `django-admin startproject {project name} .` -- note the period at the end! (for example, `django-admin startproject recipebox .`)  

Start the server with `python manage.py runserver`  

After you create your models, run `python manage.py makemigrations {foldername}` (where foldername is the top level folder for your project) to create them, then `python manage.py migrate` to push them to the db. If you get stuck, delete the db and run the command again  

If you change your models after running the migrations, run makemigrations and migrate again. If the migrations require the creation of a new table, django will automatically handle it  

Create an admin user by running `python manage.py createsuperuser`  

REITERATING: There are no extra points for pretty HTML! Don't spend time making everything on the front end look gorgeous; we just want to make sure we're serving the right information.  

Author model:  
- Name (CharField)  
- Bio (TextField)  

Recipe Model:  
- Title (CharField)
- Author (ForeignKey)
- Description (TextField)
- Time Required (Charfield) (for example, "One hour")
- Instructions (TextField)