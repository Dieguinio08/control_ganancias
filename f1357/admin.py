from django.contrib import admin

from f1357.models import F1357Field, Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "parent_id", "grandparent_id")
    list_filter = ("parent_id",)
    list_per_page = 30

    @admin.display(empty_value='No tiene')
    def grandparent_id(self, obj):
        if obj.parent_id:
            return obj.parent_id.parent_id
        return None


@admin.register(F1357Field)
class F1357FieldAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "group", "group_parent")
    list_filter = ("group", "group__parent_id", "group__parent_id__parent_id")
    list_per_page = 30

    @admin.display(empty_value='No tiene')
    def group_parent(self, obj):
        return obj.group.parent_id
