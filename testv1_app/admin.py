from django.contrib import admin

from .models import Test, Question, Result

class QuestionInline(admin.TabularInline):
    model = Question

class TestAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]    

# Register your models here.
admin.site.register(Test, TestAdmin)
admin.site.register(Question)
admin.site.register(Result)
