import json
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Portfolio
from .form import PortfolioForm
from django.db import models 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse

def home(request):
    portfolios = Portfolio.objects
    return render(request, 'home.html', {'portfolios': portfolios})

def detail(request, portfolio_id):
    portfolio_detail = get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request, 'detail.html', {'portfolio': portfolio_detail})

@login_required
def new(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.image = form.cleaned_data['image']
            post.idname = User.objects.get(username = request.user.get_username())
            post.save()
            return redirect('home')
    else:
        form = PortfolioForm()
        return render(request, 'new.html', {'form': form})

@login_required
def edit(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    if portfolio.idname == User.objects.get(username=request.user.get_username()):
        if request.method=="POST":
            portfolio.title = request.POST.get('title')
            # portfolio.image = portfolio.cleaned_data['image']
            # portfolio.image = request.POST.get('image')
            portfolio.description = request.POST.get('description')
            portfolio.save()
            return redirect('/portfolio/' + str(portfolio.id))
        return render(request, 'edit.html', {'portfolio': portfolio})
    else:
        messages.info(request, '권한이 없습니다')
        return redirect('home')

@login_required
def delete(request, portfolio_id):
    post = get_object_or_404(Portfolio, pk=portfolio_id)
    if post.idname == User.objects.get(username=request.user.get_username()):
        post.delete()
        return redirect('home')
    else:
        messages.info(request, '권한이 없습니다')
        return redirect('home')

@login_required
@require_POST
def post_like(request):
    pk = request.POST.get('pk', None) 
    portfolio = get_object_or_404(Portfolio, pk=pk)
    post_like, post_like_created = portfolio.like_set.get_or_create(user=request.user)

    if not post_like_created:
        post_like.delete()
        message = "좋아요 취소"
    else:
        message = "좋아요"

    context = {'like_count': portfolio.like_count,
               'message': message,
               'idname': request.user.get_username() }

    return HttpResponse(json.dumps(context), content_type="application/json")