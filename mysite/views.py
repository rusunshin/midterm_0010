from django.shortcuts import render
from django.http import HttpResponse
from mysite import models, forms


# Create your views here.
def index(request):
    # posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    posts = models.Post.objects.all().order_by('-pub_time')
    moods = models.Mood.objects.all()
    try:
        user_id = request.GET['user_id']
        user_title = request.GET['user_title']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
    except:
        user_id = None
        message = '如果要張貼訊息，則每一個欄位都要填寫'

    if user_id is not None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post, smalltitle=user_title)
        post.save()
        message = '成功儲存! 請記得你的編輯密碼[{}]!'.format(user_pass)

    return render(request, 'index.html', locals())


def listing(request):
    posts = models.Post.objects.all().order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()
    return render(request, 'listing.html', locals())


def posting(request):
    moods = models.Mood.objects.all()
    try:
        user_title = request.POST['user_title']
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_post = request.POST['user_post']
        user_mood = request.POST['mood']
    except:
        user_id = None
        message = '如果要張貼訊息，則每一個欄位都要填寫'
    if user_id is not None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post, smalltitle=user_title)
        post.save()
        message = '成功儲存! 請記得你的編輯密碼[{}]!'.format(user_pass)

    return render(request, 'posting.html', locals())

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = "感謝您的來信"
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email  = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
        else:
            message = "請檢查您輸入的資訊是否正確"
    else:
        form = forms.ContactForm()
    return render(request, 'contact.html', locals())


def post2db(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            message = "您的訊息已儲存，要等管理者啟用後才看得到喔。"
            post_form.save()
        else:
            message = '如要張貼訊息，則每一個欄位都要填...'
    else:
        post_form = forms.PostForm()
        message = '如要張貼訊息，則每一個欄位都要填...'

    return render(request, 'post2db.html', locals())