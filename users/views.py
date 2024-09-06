from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Register a user."""
    if request.method != 'POST':
        # Display a blank creation form
        form = UserCreationForm()
    else:
        # Process the created form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user and redirect to the home page
            login(request, new_user)
            return redirect('blogs:index')
        
    # Dispay a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
