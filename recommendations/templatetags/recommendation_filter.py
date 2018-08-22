from django.template import Library

register = Library()

def like_unlike(recommendation, user):
    if len(recommendation.like_set.filter(user = user)) == 0:
        return 'LIKE'
    return 'UNLIKE' 

def save_unsave(recommendation, user):
    if len(recommendation.saver_set.filter(user = user)) == 0:
        return 'SAVE'
    return 'UNSAVE' 

register.filter(like_unlike)
register.filter(save_unsave)
