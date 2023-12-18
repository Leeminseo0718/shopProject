from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.

#다음과 같이 수정
from .models import Board
from django.views import generic
from django.urls import reverse_lazy


    

def list(request):
    board_list = Board.objects.order_by('category')
    context = {'board_list': board_list}
    return render(request, 'board/board_list.html', context)

def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board': board}
    return render(request, 'board/board_detail.html', context)

def bottom(request):
    board = Board.objects.order_by('category')
    context = {'board': board}
    return render(request, 'board/bottom.html', context)

def top(request):
    board = Board.objects.order_by('category')
    context = {'board': board}
    return render(request, 'board/top.html', context)

def outer(request):
    board = Board.objects.order_by('category')
    context = {'board': board}
    return render(request, 'board/outer.html', context)

class create(generic.CreateView):
    model = Board
    fields = ['subject', 'price', 'photo', 'category']
    success_url = reverse_lazy('board:list')
    template_name_suffix  ='_create'

