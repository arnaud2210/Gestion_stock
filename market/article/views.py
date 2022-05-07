from os import abort
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Article, Category


@login_required
def home(request):
    return render(request, 'ListOfCategory.html')


def add_to_category(request, method="/category/add/"):
    if request.method == 'POST':
        try:
            response = request.POST.get('category')
            category = Category(category=response)
            category.save()
            return redirect('categories')
        except:
            abort(404)


def list_of_category(request):

    all_categories = Category.objects.all()
    return render(request, 'ListOfCategory.html', context={'all_categories': all_categories})


def add_to_article(request, method="/product/add/"):
    if request.method == "POST":
        try:
            label = request.POST.get('label')
            price = request.POST.get('price')
            quantity = request.POST.get('quantity')
            category = request.POST.get('categorie')
            creation = request.POST.get('creation')

            article = Article(category_id=category, label=label,
                              price=price, quantity=quantity, creation=creation)
            article.save()
            return redirect('products')

        except:
            abort(404)


def list_of_product(request):

    all_products = Article.objects.all()
    all_categories = Category.objects.all()
    numberOfProduct = Article.objects.count()
    return render(request, 'ListOfProduct.html', context={'all_products': all_products, 'all_categories': all_categories, 'numberOfProduct': numberOfProduct})


def get_one_product(request, id, method='/product/<int:id>/'):

    product = Article.objects.get(id=id)
    all_categories = Category.objects.all()

    if request.method == 'POST':
        product.label = request.POST.get('label')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.creation = request.POST.get('creation')

        product.save()
        return redirect('products')
    return render(request, 'GetOneProduct.html', context={'product': product, 'all_categories': all_categories})


def delete_one_product(request, id, method="/delete/<int:id>/"):
    
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('products')

