from django.contrib import admin

from ecommerce.courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'partner', 'site',)
    search_fields = ('id', 'name', 'partner', 'site', )
    list_filter = ('site', 'partner', )


admin.site.register(Course, CourseAdmin)
