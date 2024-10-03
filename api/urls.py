from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

#create instance of DefaultRouter
router=DefaultRouter()

#invoke register

router.register("v1/books",views.BookViewSetView,basename="books")

router.register("v1/reviews",views.ReviewUpdateDestroyViewSetView,basename="reviews")

for url in router.urls:
    print("===============",url,"================")

#router.urls
#lh:8000/api/v1/books/

urlpatterns=[

    path("books/",views.BookListCreateView.as_view()),

    path("books/<int:pk>/",views.BookRetrieveUpdateDestroyView.as_view()),

    path("books/genres/",views.GenreListView.as_view()),

    path("books/author/",views.AuthorListView.as_view()),

    path("v2/books/",views.BookListView.as_view()),

    path("v2/books/<int:pk>/",views.BookRetriUpDestroyView.as_view()),

    



]+router.urls