from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method== 'POST':
        form=RegistrationForm(request.POST)

        if form.is_valid():
            User=form.save(commit=False)
            User.set_password(form.cleaned_data['password'])
            User.save()
            return redirect('login')
    else:  
         form=RegistrationForm()
    return render(request,'register.html',{'form':form})


# Create your views here.
