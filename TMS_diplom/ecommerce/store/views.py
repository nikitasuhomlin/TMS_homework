from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Category, Product, ProductReview
from .forms import ReviewForm


def home(request):
    trending_products = Product.objects.filter(trending=1)
    context = {'trending_products': trending_products}
    return render(request, 'store/index.html', context)



def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request, 'store/collections.html', context)



def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category': category}
        return render(request, 'store/products/index.html', context)
    else:
        messages.warning(request, 'Категория не найдена!')
        return redirect('collections')


def productview(request, cate_slug, prod_slug):

    if(Category.objects.filter(slug=cate_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products': products}
        else:
            messages.error(request, 'Отзыв успешно добавлен!')
            return redirect('collections')
    else:
        messages.error(request, 'Категория не найдена!')
        return redirect('collections')
    return render(request, 'store/products/view.html', context)


def productlistajax(request):
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    productlist = list(products)

    return JsonResponse(productlist, safe=False)


def searchproduct(request):
    if request.method == 'POST':
        searcheditem = request.POST.get('productsearch')
        if searcheditem == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name__contains=searcheditem).first()

            if product:
                return redirect('collections/'+product.category.slug+'/'+product.slug)
            else:
                messages.info(request, 'По вашему запросу ничего не найдено!')
                return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))


def submit_review(request, product_id, cate_slug, prod_slug):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        products = Product.objects.get(slug=cate_slug, slug1=prod_slug)
        if products:
            reviews = ProductReview.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Ваш отзыв опубликован!Спасибо за ваш отзыв!')
            return redirect(url)
        # except ObjectDoesNotExist:
        #     form = ReviewForm(request.POST)
        #     if form.is_valid():
        #         data = ProductReview()
        #         data.content = form.cleaned_data['content']
        #         data.stars = form.cleaned_data['stars']
        #         data.user_id = request.user.id
        #         data.product_id = product_id
        #         data.save()
        #         messages.success(request, 'Спасибо!')
        #         return redirect(url)
