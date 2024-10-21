#from django.contrib import admin
#from demo.models import Book
#admin.site.register(Book)


# Register your models here.
# demo/admin.py

# demo/admin.py

from django.contrib import admin
from .models import Book  # Ensure this import is correct

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn')  # Columns to display in the admin list view
    search_fields = ('title', 'author')  # Fields that can be searched in the admin interface