from django.contrib import admin
from ticket.models import Categorie, Ticket, Message

admin.site.register(Categorie)
admin.site.register(Ticket)
admin.site.register(Message)
