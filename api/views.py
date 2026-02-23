from django.shortcuts import render
from django.http import JsonResponse
from http import HTTPStatus

from .forms import RegisterForm

from .models import Register



def HomePage(request):
    # form = SignUpForm()
    return render(request, 'index.html')


def Dynamic(request, title):
    print(title)
    return JsonResponse({'message': "end point is working"})


# def register_view(request):
#     form = RegisterForm()
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data.get('name')
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             confirm_password = form.cleaned_data.get('confirm_password')
#             Register.objects.create(
#                 name=name,
#                 email=email,
#                 password=password,
#                 confirm_password=confirm_password,
#             )
#             return JsonResponse({'message': 'User registered successfully'}, status=HTTPStatus.OK)
#         else:
#             return JsonResponse({'message': 'Invalid form data', 'errors': form.errors}, status=HTTPStatus.BAD_REQUEST)
#     return render(request, 'register.html', {'form': form})





def SignUp(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request,'signUp.html',{'f':form})
    elif request.method  == "POST":
        data = RegisterForm(request.POST)
        if data.is_valid():
            name = data.cleaned_data.get('name')
            email = data.cleaned_data.get('email')
            newuser =  Register.objects.create(name=name,email=email)
            newuser.save()
            return JsonResponse({'message':'User ceated success !!'})
        else:
            form = RegisterForm()
            return render(request,'signUp.html',{'form':form})
    else:
        return render(request,'signUp.html',{'form':form})
    

def AllUsers(request):
    users = Register.objects.all()
    context  = {
        'users':users
    }

    return render(request,'alluser.html',context)