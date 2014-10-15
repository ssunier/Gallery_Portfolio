from django.contrib import admin
from portfolio.models import Collection, Gallery, Music

# Register your models here.
admin.site.register(Collection)
#class CollectionsInline(admin.StackedInline):
  #model = Collection

admin.site.register(Gallery)
admin.site.register(Music)
