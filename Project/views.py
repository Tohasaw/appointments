
from django.shortcuts import render, redirect
from Project.forms import RegisterForm

def register(request):
    data = {}
    if request.method == 'POST':
      form = RegisterForm(request.POST)
      if form.is_valid():
        new_user = form.save(commit = False)
        new_user.save()
        data['form'] = form

        return render(request, 'registration/signup_success.html', data)
    else:
        form = RegisterForm()
        data['form'] = form
    return render(request, 'registration/register.html', data)
def index_view(request):
  return render(request, 'home.html')
