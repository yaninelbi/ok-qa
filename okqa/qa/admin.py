from django.contrib import admin
from okqa.qa.models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    pass
class AnswerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
