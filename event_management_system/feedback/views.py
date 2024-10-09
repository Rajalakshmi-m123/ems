from django.shortcuts import render,redirect


from .models import Feedback
from django.contrib import messages

def feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user_class = request.POST.get('user_class')
        semester = request.POST.get('semester')
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')

        Feedback.objects.create(
            name=name,
            user_class=user_class,
            semester=semester,
            rating=rating,
            comments=comments
        )
        messages.success(request, 'Feedback submitted successfully!')
        return redirect('feedback')

    return render(request, 'feedback/feedback_form.html')

