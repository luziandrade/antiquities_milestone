from django.shortcuts import render, redirect, reverse
from .models import Bid


def all_items(request):
    items = Bid.objects.all()
    return render(request, "items_bid.html", {"items": items})


def item(request, id):
    bids = Bid.objects.get(id=id)
    return render(request, "auction.html", {"bids": bids})

