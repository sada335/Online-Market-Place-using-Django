from django.shortcuts import render, redirect, get_object_or_404
from .models import MarketItem

# View all items
def item_list(request):
    items = MarketItem.objects.all()
    return render(request, 'marketplace/item_list.html', {'items': items})

# Create a new item
def create_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        rating = request.POST['rating']
        available = 'available' in request.POST
        MarketItem.objects.create(name=name, description=description, price=price, rating=rating, available=available)
        return redirect('item_list')
    return render(request, 'marketplace/item_form.html')

# Update an item
def update_item(request, item_id):
    item = get_object_or_404(MarketItem, id=item_id)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.price = request.POST['price']
        item.rating = request.POST['rating']
        item.available = 'available' in request.POST
        item.save()
        return redirect('item_list')
    return render(request, 'marketplace/item_form.html', {'item': item})

# Delete an item
def delete_item(request, item_id):
    item = get_object_or_404(MarketItem, id=item_id)
    item.delete()
    return redirect('item_list')
