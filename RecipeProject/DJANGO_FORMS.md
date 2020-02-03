# Django Forms.
### forms.py
`from django import forms`  
This is where we 'make?' our forms.  

For the demo, we used models.py as a reference to build our form.  
**For the first part, we will do it the long way**  
  
Create a forms.py,  
Create our class:
```
class NewAddForm(forms.Form):
    title = forms. CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    # We will need to import Author from models
    # This is so we can 'spell check' author names with a dropdown.
    author = forms.ModelChoiceField(queryset=Author.objecs.all()) 

```
  
In urls.py  
we will want to hook up our rout to where the form will be.  
  
Make the view in views.py  
```
def my_new_view(request):
    html = 'my_new_form.html'
    if request.method == "POST":
     form = MyImportedForm(request.Post)
     # ALWAYS
     if form.is_valid():
        # This is an object - it can contain database objects
        # Thats a superpower
        data = form.cleaned_data
        MyCorrespondingModel.objects.create(
            title = data['title'],
            body = data['body'],
            author = data['author']
            # Or whatever
        ) 
        # Handle the re-route - path( ... name='REQUIRED_FOR_THIS_STEP')
        return HttpResponseRedirect(reverse("name"))
    form = MyImportedForm()
```
And a template in `/templates/project`
the `<form action="">` is intentional. Leave it as empty double quotes.



























