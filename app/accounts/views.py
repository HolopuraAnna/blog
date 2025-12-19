from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render, redirect


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # додаємо нового юзера в групу "author"
            author_group, created = Group.objects.get_or_create(name='author')
            user.groups.add(author_group)

            return redirect('login')
        else:
            messages.error(request, "Дані не валідні!")
    else:
        form = UserCreationForm()

    return render(request, "accounts/registration.html", {'form': form})
