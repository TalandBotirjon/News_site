from django.urls import path

from .views import NewsListViews, NewCreateViews, NewDestroyViews, NewUpdateViews

urlpatterns = [
    path("upd/<int:pk>/", NewUpdateViews.as_view()),
    path("del/<int:pk>/", NewDestroyViews.as_view()),
    path('cre/', NewCreateViews.as_view() ),
    path('', NewsListViews.as_view()),
]
