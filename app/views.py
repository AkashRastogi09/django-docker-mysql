from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ItemForm()
    items = Item.objects.all()
    return render(request, 'form.html', {'form': form, 'items': items})

