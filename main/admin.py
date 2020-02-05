from django.contrib import admin

# Register your models here.
from .models import Person,ListSource,Author,Article,RecommendArticle,Query

admin.site.register(Person)
admin.site.register(ListSource)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(RecommendArticle)
admin.site.register(Query)
