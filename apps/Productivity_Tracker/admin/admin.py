from django.contrib import admin
from apps.Productivity_Tracker.models import *
# from apps.Productivity_Tracker.models.tasks import Tasks


class DeadlinesInline(admin.TabularInline):
    model = Deadlines
    # extra = 1  # number of empty forms to show
    max_num = 1  # optional: require at least one deadline

# Register your models here.
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description')
    
#     def get_urls(self):
#         return super().get_urls()
    




# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'no_of_tasks')
    
#     def no_of_tasks(self, obj):
#         tasks = obj.tasks_set.all()
#         if tasks:
#             return tasks.length()
        # return 0