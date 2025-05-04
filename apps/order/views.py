from django.contrib import messages 
from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Tour

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
