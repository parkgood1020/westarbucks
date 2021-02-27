import json
from os     import O_APPEND, name
from typing import MutableSequence

from django          import views
from django.http     import JsonResponse, request

from django.views    import View
from products.models import Menu, Category, Product
from products.models import Drink, Nutrition, Image, Allergy, Allergy_drink

# Create your views here.
#장고에서는 post와 get에 따라 알아서 나눠 처리하게 해준다.

#post 방식
#1. 요청을 받는다. body -> JSON
#2. JSON -> Python
#3. 데이터베이스에 쿼리를 날린다(create)
#4. 응답을 반환한다.

#get 방식
# 1.요청을 받는다.
# 2. 데이터베이스에서 알맞는 쿼리를 날린다.
# 3.결과를 가공한다.
# 4.json형태의 바디에 담아 리턴 해준다.

#상품 관련
class ProductsView(View):

    def get(self, request):
        products = Product.objects.all()
        results = []
        for product in products:
            results.append(
                {
                    'menu':product.menu.menu.name,
                    'category': product.menu.name,
                    'product': product.name
                }
            )
        return JsonResponse({'results':results}, status=200)

    def post(self, request):
        data = json.load(request.body)
        menu = Menu.objects.create(name=data['menu'])
        category = Category.objects.create(
            name = data['category'],
            menu = menu
        )
        product = Product.objects.create(
            name = data['product']['name'],
            category = category
        )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

# 메뉴 관련.
class MenuView(View):
    def get(self, request):
        menus   = Menu.objects.all()
        results = []

        for menu in menus:
            results.append(
                {
                    'name' : menu.name
                }
            )
        
        return JsonResponse({'results':results}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        menu = Menu.objects.create(name=data['menu'])

        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)


# 카테고리 관련.
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        results    = []

        for category in categories:
            results.append(
                {
                    'category' : category.name,
                    'menu'     : category.menu.name
                }
            )
        
        return JsonResponse({'results':results}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        
        menu = Menu.objects.create(name=data['menu'])
        category = Category.objects.create(
            name = data['category'],
            menu = menu
        )

        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)


#  음료-알러지 유발요인
class Allergy_Drink(View):
    def get(self, request):
        all_drinks = Allergy_drink.objects.all()
        results = []

        for all_drink in all_drinks:
            results.append(
                {
                    'menu'         : all_drink.drink.category.menu.name,
                    'category'     : all_drink.drink.category.name,
                    'korean_name'  : all_drink.drink.korean_name,
                    'english_name' : all_drink.drink.english_name,
                    'description'  : all_drink.drink.description,
                    'allergy_name' : all_drink.allergy.name,

                }
            )
        
        return JsonResponse({'results':results}, status=200)

    def post(self, request):
        data = json.loads(request.bodoy)

        menu = Menu.objects.create(name=data['menu'])
        category = Category.products.create(
            name = data['categoroy'],
            menu = menu
        )
        drink = Drink.objects.create(
            korean_name  = data['korean_name'],
            english_name = data['english_name'],
            description  = data['description'],
            category     = category
        )
        allergy = Allergy.objects.create(name=data['allergy'])
        allergy_drink = Allergy_Drink.objects.create(
            allergy = allergy,
            drink   = drink
        )

        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

