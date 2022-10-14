from django.contrib import admin

# Register your models here.
from .models import Book
from import_export.admin import ImportExportModelAdmin
from import_export import resources 

class BookAdmin(ImportExportModelAdmin):

    list_display = ['InvoiceID']

admin.site.register(Book,BookAdmin)