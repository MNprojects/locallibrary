
from django.conf.urls import url

from . import views


urlpatterns = [
    
    url(r'^$', views.index, name='index'),

    # /catalog/books
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    

    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]
#/catalog/mybooks
urlpatterns += [url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),]

#/catalog/allbooksborrowed/
urlpatterns += [url(r'allbooksborrowed/$', views.AllLoanedBooksListView.as_view(),name='all-borrowed'),]

#/catalog/book/*bookID*/renew/
urlpatterns += [url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),]

#/catalog/author/*make changes to authors, min access Librarians *
urlpatterns += [  
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]