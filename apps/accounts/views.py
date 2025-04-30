from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.http import JsonResponse
from .models import UserProfile


def login_user(request):
    if request.method == 'POST':
        print('post')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username, password)
        if user:
            login(request, user)
            return redirect(reverse_lazy('home'))
        else:
            messages.add_message(request, messages.WARNING, "Parol yoki username noto'g'ri")
            return render(request, 'login.html')  # Mana shu qator qo'shildi
    elif request.method == 'GET':
        return render(request, 'login.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # Boshqa maydonlar

        # Ma'lumotlarni validatsiya qilish (tekshirish)
        if not username or not email or not password or password != confirm_password:
            # Xatolik xabarlarini ko'rsatish
            return render(request, 'register.html', {'error': 'Noto\'g\'ri ma\'lumotlar'})

        # Foydalanuvchini yaratish (misol uchun)
        try:
            from django.contrib.auth.models import User
            user = User.objects.create_user(username=username, email=email, password=password)
            # Ro'yxatdan o'tish muvaffaqiyatli bo'lganda yo'naltirish
            return HttpResponseRedirect(reverse_lazy('home'))
        except Exception as e:
            # Xatolik xabarini ko'rsatish
            return render(request, 'register.html', {'error': f'Ro\'yxatdan o\'tishda xatolik: {e}'})
    else:
        return render(request, 'register.html')


def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('home'))


@login_required
def profile_update(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Noto\'g\'ri so\'rov'}, status=400)