from django.shortcuts import render
from .models import  Recommendation
from professions.models import Profession
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RecommendationForm,  StepForm, BulletFormset, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index1(request):
    recommendations = Recommendation.objects.all()
    return render(request, 'recommendations/index1.html',{'recommendations': recommendations})



def bubblesort(recommendations):
    arr = []
    for item in recommendations:
        arr.append(item)
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j].like_set.count() <  arr[j+1].like_set.count():
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def index(request):
    recommendations = Recommendation.objects.all()
    professions = Profession.objects.all()
    parameters = []
    if request.method == 'POST':
        profession_id = request.POST['rec_profession']
        if profession_id != 'None':
            recommendations = Recommendation.objects.filter( profession = profession_id )
            profession = Profession.objects.get(pk = profession_id)
            parameters.append(profession.name)
        search = request.POST['search']
        if search != '':
            parameters.append(search)
            tem = recommendations
            recommendations = []
            for item in tem:
                if search.lower() in item.title.lower():
                    recommendations.append(item)
    recommendations = bubblesort(recommendations) 
    return render(request, 'recommendations/index.html',{
        'recommendations': recommendations,
        'professions': professions,
        'parameters':parameters
    })






#for future add page not found handler
@login_required(login_url  = 'accounts:signin')
def detail(request, recommendation_id):
    recommendation = Recommendation.objects.get(pk = recommendation_id)
    comment_form = CommentForm()
    return render(request, 'recommendations/detail.html', {
                            'recommendation':recommendation,
                            'comment_form':comment_form
                        })

@login_required(login_url  = 'accounts:signin')
def comment(request):
    if request.method == 'POST':
        recommendation_id = request.POST['recommendation_id']
        rec = Recommendation.objects.get(pk = recommendation_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            request.user.comment_set.create(recommendation = rec, text = text)
        return HttpResponseRedirect(reverse('recommendations:detail', kwargs = { 'recommendation_id':recommendation_id } ))


@login_required(login_url  = 'accounts:signin')
def saver(request, recommendation_id):
    try:
        rec = Recommendation.objects.get(pk = recommendation_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('recommendations:detail', kwargs = { 'recommendation_id':recommendation_id } ))
    try:
        saver = rec.saver_set.get(user = request.user)
    except ObjectDoesNotExist:
        saver = None
    if saver:
        saver.delete()
    else:
        request.user.saver_set.create(recommendation = rec)
    return HttpResponseRedirect(reverse('recommendations:detail', kwargs = { 'recommendation_id':recommendation_id } ))

@login_required(login_url  = 'accounts:signin')
def like(request, recommendation_id):
    try:
        rec = Recommendation.objects.get(pk = recommendation_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('recommendations:detail', kwargs = { 'recommendation_id':recommendation_id } ))
    try:
        like = rec.like_set.get(user = request.user)
    except ObjectDoesNotExist:
        like = None
    if like:
        like.delete()
    else:
        request.user.like_set.create(recommendation = rec)
    return HttpResponseRedirect(reverse('recommendations:detail', kwargs = { 'recommendation_id':recommendation_id } ))
    
    print(rec)
    # if request.user.id == rec.like_set.
    


@login_required(login_url  = 'accounts:signin')
def add(request):
    professions = Profession.objects.all()
    rec_form = RecommendationForm()
    if request.method == 'POST':
        rec_form = RecommendationForm(request.POST)
        if rec_form.is_valid():
            #1 SAVE RECOMMENDATION
            rec_title = rec_form.cleaned_data['rec_title']
            rec_description = rec_form.cleaned_data['rec_description']
            rec_profession = request.POST['rec_profession']
            profession = Profession.objects.get(pk = rec_profession)
            rec = request.user.recommendation_set.create(
                title = rec_title, 
                description = rec_description, 
                profession = profession
            )
            rec.save()
            return HttpResponseRedirect(reverse('recommendations:addstep', 
                                                kwargs = { 'recommendation_id':rec.id } ))
        else:
            return render(request, 'recommendations/add.html', {
                            'professions': professions,
                            'rec_form': rec_form,
                        })
    return render(request, 'recommendations/add.html', {
                    'professions': professions,
                    'rec_form': rec_form,
                })

@login_required(login_url  = 'accounts:signin')
def add_step(request, recommendation_id):
    step_form = StepForm()
    bullet_formset = BulletFormset()
    rec = Recommendation.objects.get(pk = recommendation_id)
    if rec.user.id != request.user.id:
        return HttpResponseRedirect(reverse('accounts:profile'))
    if request.method == 'POST':
        step_form = StepForm(request.POST)
        bullet_formset = BulletFormset(request.POST)
        if step_form.is_valid() and bullet_formset.is_valid():
            step_title = step_form.cleaned_data['step_title']
            step = rec.step_set.create(title = step_title)
            step.save()
            step_form = StepForm()
            for bullet in bullet_formset:
                bullet_description = bullet.cleaned_data['description']
                bullet_link = bullet.cleaned_data['link']
                step.bullet_set.create(
                    description = bullet_description, 
                    link = bullet_link,
                    link_name = 'here',
                )
            if request.POST['submit_status'] == 'finish':
                return HttpResponseRedirect(reverse('recommendations:detail', 
                                                    kwargs = { 'recommendation_id':rec.id } ))
    return render(request, 'recommendations/addstep.html', {
                    'step_form': step_form,
                    'bullet_formset': BulletFormset,
                    'recommendation_id': recommendation_id,
                    'recommendation': rec,
                })


def add_step2(request):
    return render(request, 'recommendations/add2.html')