from django.urls import path
from .views import ItemListView, RustProcessView, TensorFlowProcessView

urlpatterns = [
    path('items/', ItemListView.as_view(), name='item-list'),
    path('rust-process/', RustProcessView.as_view(), name='rust-process'),
    path('tensorflow-process/', TensorFlowProcessView.as_view(), name='tensorflow-process'),
]