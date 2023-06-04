from .models import*

def feature(request):
    info = AppInfo.objects.get(pk=1)
    categ = Category.objects.all()

    context = {
        'info': info,
        'categ': categ
    }
    
    return context

def cartcount(request):
    cart = Cart.objects.filter(user__username = request.user.username, paid=False)
    itemcount = 0

    for item in cart:
        itemcount += item.quantity

    context = {
        'itemcount': itemcount
    }    

    return context