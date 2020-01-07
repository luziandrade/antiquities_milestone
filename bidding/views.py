from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Bid
from .forms import BidForm


@login_required
def all_items(request):
    items = Bid.objects.all()
    return render(request, "items_bid.html", {"items": items})


def item(request, id):
    bids = Bid.objects.get(id=id)
    if request.method == "POST":
        form = BidForm(request.POST, request.FILES, instance=bids)
        if form.is_valid():
            bid = form.save()
            return redirect(item, bid.id)
    else:
        form = BidForm(instance=bids)
    return render(request, 'auction.html', {'form': form, 'author': User, "bids": bids})


def edit_bid(request, id=id):
    bid = get_object_or_404(Bid, id=id)
    if request.method == "POST":
        form = BidForm(request.POST, request.FILES, instance=bid)
        if form.is_valid():
            bid = form.save()
            return redirect(item, bid.id)
    else:
        form = BidForm(instance=bid)
    return render(request, 'auction.html', {'form': form, 'author': User})
