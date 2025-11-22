from .admin import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'no_of_tasks')
    
    def no_of_tasks(self, obj):
        return obj.tasks_set.count()  # count() is more efficient than len()
    no_of_tasks.short_description = 'Number of Tasks'