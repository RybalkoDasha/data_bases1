from django.shortcuts import render
from books.models import Book
import datetime

def books_view(request):
    template = 'books/books_list.html'
    books_data = Book.objects.all()
    context = {'books': books_data}
    return render(request, template, context)
def books_pub(request, pub_date):

    date1 = datetime.datetime.strptime(pub_date, '%Y-%m-%d')
    book_pub = Book.objects.filter(pub_date = date1)
    '''
    получаем список дат из БД
    '''
    pages_list_full =['']+sorted(list(set([i.strftime('%Y-%m-%d') for i in Book.objects.values_list('pub_date', flat=True)])))+['']
    '''
    # получаем номера предыдущей и следующей страницы
    # '''
    page_cur = str(book_pub[0].pub_date)
    index_cur_page = pages_list_full.index(page_cur)
    pages_switch = list()
    pages_switch.append(pages_list_full[index_cur_page-1])
    pages_switch.append(pages_list_full[index_cur_page+1])

    context = {'books': book_pub, 'pages': pages_switch}
    template = 'books/books_pagi.html'
    return render(request, template, context)
