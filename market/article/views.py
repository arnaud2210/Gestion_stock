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
            return f'ERREUR DE CONNEXION'


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
            f"Votre ressource n'a pas été créée"


def list_of_product(request):

    all_products = Article.objects.all()
    numberOfProduct = Article.objects.count()
    return render(request, 'ListOfProduct.html', context={'all_products': all_products, 'numberOfProduct': numberOfProduct})


"""def resupply(request):
    render(request, 'Resupply.html')"""