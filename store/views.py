

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Book, Order

@csrf_exempt
def order_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, id=book_id)
        Order.objects.create(book=book)
        return JsonResponse({'status': 'success', 'message': f'You ordered {book.title} for Rs. {book.price}'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
