from django.contrib import admin
from .models import CreditCard

class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('series', 'number', 'date_issue', 'date_end_activity',
                    'date_use', 'amount', 'status')

admin.site.register(CreditCard, CreditCardAdmin)