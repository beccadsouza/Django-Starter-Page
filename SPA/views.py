from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required
def main(request):
	return render(request, 'main.html')


def logout_view(request):
	logout(request)
	return render(request, 'registration/logout.html')
