from django.urls    import path
from products.views import *

urlpatterns = [
    path('', ProductsView.as_view()),
    path('/menu', MenuView.as_view()),
    path('/category', CategoryView.as_view()),
    path('/all_drink', Allergy_Drink.as_view())
]
#여기 안에 뷰에 있는 클래스가 와야한다.
#  as_view()를 써줘야함. as_view()가 해당 요청이 get인지 post인지 구분해준다.
# 클래스형에는 무조건 붙고, 함수형은 안붙는다.