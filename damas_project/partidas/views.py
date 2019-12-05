from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def partida(request):
	return render(request, 'tabuleiro.html')

@csrf_exempt
def jogada(request):
	return HttpResponse(request.POST)
