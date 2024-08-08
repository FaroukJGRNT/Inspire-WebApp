from django.shortcuts import render, redirect
from .forms import NewIdeaForm
from .models import Idea, Comment
import datetime


def home(response):
    ideas = Idea.objects.all()

    if response.method == 'POST':
        idea_id = response.POST.get('idea_id')
        user = response.user
        date = datetime.datetime.now()
        content = response.POST.get('comment_text')
        if content != None and len(content) != 0:
            new_comment = Comment(user=user, content=content, created_at=date, idea=Idea.objects.get(id=idea_id))
            new_comment.save()
        return redirect('/')
    else:
        return render(response, 'posts/home.html', {'ideas': ideas})

def create(response):
    user = response.user

    if response.method == 'POST':
        form = NewIdeaForm(response.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            new_idea = Idea(title=title, content=content, user=user)
            new_idea.save()
            return redirect('/')
    else:
        form = NewIdeaForm()
        return render(response, 'posts/create.html', {'form': form})

# Create your views here.
