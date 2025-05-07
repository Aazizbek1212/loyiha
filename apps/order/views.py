from django.contrib import messages 
from django.shortcuts import render, get_object_or_404, redirect
from telegram import Bot
from django.conf import settings
from django.contrib.auth.decorators import login_required
import telegram

from apps.order.forms import OrderForm
from .models import Order, Review, Tour

def review_create(request, pk):
    tour = get_object_or_404(Tour, id=pk)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        Review.objects.create(
            username=request.user.username,
            email=request.user.email,
            rating=rating,
            comment=comment,
            tour=tour
        )
        messages.success(request, 'Review submitted successfully!')
        return redirect('tour_detail', pk=pk)  # muvaffaqiyatli yozilgandan keyin qayerga yo‘naltirish kerak bo‘lsa o‘sha yerga
    return render(request, 'tour_detail.html', {'tour': tour})



bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
ADMIN_TELEGRAM_ID = 2095041544  # O'z admin IDingizni shu yerga yozing

@login_required(login_url='login')
def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            print('Buyurtma saqlandi')
            try:
                message = f"Yangi zakaz!\nTelefon: {form.cleaned_data.get('phone_number')}\nIsm: {order.name}\nTur: {order.tour.name}\nSana: {order.date}\nKattalar: {order.person}\nBolalar: {getattr(order, 'child', 0)}"
                bot.send_message(chat_id=ADMIN_TELEGRAM_ID, text=message)
            except Exception as e:
                print(f"Telegram xabarini yuborishda xatolik (admin): {e}")
            return redirect('tour_detail')  # Yoki buyurtma detal sahifasiga yo'naltiring
        else:
            print(form.errors)
    return redirect('home') # Agar POST bo'lmasa ham redirect qilish kerakmi?