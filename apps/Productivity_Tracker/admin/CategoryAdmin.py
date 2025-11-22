from .admin import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    
    def get_urls(self):
        return super().get_urls()