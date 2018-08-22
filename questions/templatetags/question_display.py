from django import template

register = template.Library()

@register.filter
def q_show(question, index):
    a = question.question_text.split("или")
    if index == 0:
        return a[index].lower()
    else:
        return a[index].replace("?", "")

