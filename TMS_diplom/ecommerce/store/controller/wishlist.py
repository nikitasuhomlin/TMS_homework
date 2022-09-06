from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render, redirect

from store.models import Wishlist, Product


@login_required(login_url='loginpage')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist': wishlist}
    return render(request,'store/wishlist.html', context)


def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status':'Заданный продукт уже был добавлен в Лист Ожидания!'})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status':'Продукт добавлен в Лист Ожидания!'})
            else:
                return JsonResponse({'status':'Товар не найден!'})
        else:
            return JsonResponse({'status':'Войдите в систему, чтобы Продолжить!'})
    return redirect('/')


def deletewishlistitem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))

            if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                wishlistitem = Wishlist.objects.get(product_id=prod_id, user=request.user)
                wishlistitem.delete()
                return JsonResponse({'status': 'Заданный продукт удалён из Листа Ожидания!'})
            else:
                return JsonResponse({'status': 'Продукт не был найден в Листе Ожидания!'})
        else:
            return JsonResponse({'status': 'Войдите в систему, чтобы Продолжить!'})
    return redirect('/')