from django.contrib import admin
from myblog.models import Post, Category, Categorization



class CategoriesInline(admin.TabularInline):
    model = Categorization
    extra =1

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_date','modified_date','published_date']
    inlines = (CategoriesInline,)

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)