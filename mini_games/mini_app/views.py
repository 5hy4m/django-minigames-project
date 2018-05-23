from django.shortcuts import render
from mini_app.forms import archery_boards_form
from mini_app.models import archery_boards
# Create your views here.
def home(request):
    return render(request,'mini_app/home.html')


def tictactoe(request):
    return render(request,'mini_app/tictactoe/tictactoe.html')

def fingercut(request):
    return render(request,'fingercut/fingercut.html')

def snakeattack(request):
    return render(request,'snakeattack/snakeattack.html')

def light_game(request):
    return render(request,'light_game/light_game.html')

def orbitshooter(request):
    return render(request,'orbitshooter/orbitshooter.html')


def archery_game(request):
    obj = archery_boards.objects.create()

    bestScore = request.POST.get('bestScore')
    print(bestScore,"THIS IS THE SCORE*****************************************************")
    return render(request,'archery/archery.html',{'bestScore':bestScore})


def retry(request):
    return render(request,'archery/archery_login.html')


def archery_form(request):
    form = archery_boards_form()

    if request.method == "POST":
        form = archery_boards_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return archery_game(request)
        else:
            print('ERROR FORM INVALID')
            return retry(request)

    return render(request,'archery/archery_login.html',{'form':form})
