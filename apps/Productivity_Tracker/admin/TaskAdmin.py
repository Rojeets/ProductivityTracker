from .admin import *


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_project_title', 'priority', 'get_category_title', 'get_deadline_range', 'status')
    inlines = [DeadlinesInline]  # Add the inline here

    def get_project_title(self, obj):
        return obj.project_id.title
    get_project_title.short_description = 'Project'
    get_project_title.admin_order_field = 'project_id__title'
    
    def get_category_title(self, obj):
        return obj.category_id.title
    get_category_title.short_description = 'Category'
    get_category_title.admin_order_field = 'category_id__title'

    def get_deadline_range(self, obj):
        deadlines = obj.deadlines_set.all()  # all deadlines for this task
        if deadlines.exists():
            start = min(d.start_date for d in deadlines)
            end = max(d.end_date for d in deadlines if d.end_date)
            return f"{start} - {end if end else 'N/A'}"
        return 'No deadlines'
    get_deadline_range.short_description = 'Deadlines'
