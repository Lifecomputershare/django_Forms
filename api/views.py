from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse


from http import HTTPStatus
from django.views.generic import DeleteView, CreateView,UpdateView,DetailView

from .forms import RegisterForm

from .models import Register

from django.contrib.auth.decorators import login_required



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
    
@login_required(login_url='accounts/login')
def AllUsers(request):
    users = Register.objects.all()
    context  = {
        'users':users
    }
    return render(request,'alluser.html',context)



def update_user(request,id):
    register_user = get_object_or_404(Register,id=id)

    if request.method == "POST":
        form = RegisterForm(request.POST, instance=register_user)
        if form.is_valid():
            form.save()
            return redirect('users')
        
    else:
        form = RegisterForm(instance = register_user)
    return render(request,'update.html',{'form':form})



def delete_user(request,id):
    user = Register.objects.get(id = id)
    if request.method == "POST":
        user.delete()
        return redirect('users')
    return render(request, 'delete.html', {'form': user})







def Update_Register_User(request, name):
    user = get_object_or_404(Register,id=name)
    if request.method == "POST":
        data = RegisterForm(request.POST, instance=user)
        if data.is_valid():
            data.save()
            return redirect('users')
    else:
        form = RegisterForm(instance=user)
    return render(request,'update_register_user.html',{'form':form})




# For Delete User

def Delete_User(request, id):
    user = get_object_or_404(Register, id = id)
    if request.method == "POST":
        user.delete()
        return redirect('users')
    return render(request, 'delete_user.html',{'user':user})
    
    