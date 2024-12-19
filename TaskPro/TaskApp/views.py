from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Client, Project
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Project
from .forms import ProjectForm


# Register a client
@login_required
def register_client(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        Client.objects.create(name=name, email=email, phone=phone, address=address)
        return redirect('client_list')
    return render(request, 'register_client.html')

# Fetch client info
@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

# Edit/Delete client info
@login_required

# View to edit client information
def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)  # Ensure valid client ID
    if request.method == 'POST':
        client.name = request.POST.get('name')
        client.email = request.POST.get('email')
        client.phone = request.POST.get('phone')
        client.address = request.POST.get('address')
        client.save()
        return redirect('client_list')  # Redirect to client list after saving
    return render(request, 'edit_client.html', {'client': client})

@login_required
def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return redirect('client_list')

# Add new projects for a client and assign users
@login_required

def add_project(request, client_id):
    client = get_object_or_404(Client, id=client_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = client
            project.save()
            return redirect('client_detail', client_id=client.id)  # Fixed redirect
    else:
        form = ProjectForm()

    return render(request, 'add_project.html', {'form': form, 'client': client})

# Retrieve assigned projects for the logged-in user
@login_required
def user_projects(request):
    projects = request.user.projects.all()
    return render(request, 'user_projects.html', {'projects': projects})
def client_detail(request, client_id):
    print(f"Fetching client with ID: {client_id}")
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'client_detail.html', {'client': client})

def logout_confirmation(request):
    return render(request, 'logout.html')