from django.shortcuts import render
# from .forms import CustomUserCreationForm


# Create your views here.

def mainpage (request):
    page = 'bet'
    

    return render(request, "sports/base.html")
    
    

# def mainpage(request):
#     mainpage(request)
#     return redirect('livescore')

def Userbet(request):
    page = 'bet'
    return render(request, "sports/index.html")
    # form = CustomUserCreationForm()
