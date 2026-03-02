from django.contrib import admin
from .models import Note
from .models import Author

# Register your models here.

admin.site.register(Note)

admin.site.register(Author)
