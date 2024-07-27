from django.urls import path
from .views import ExpenseAddView

urlpatterns = [
    path("api/expense/", ExpenseAddView.as_view(), name="expanse")

    ]
