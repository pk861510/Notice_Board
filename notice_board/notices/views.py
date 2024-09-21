from django.shortcuts import render, redirect
from .models import * #[Notice,]
from .forms import NoticeForm


# List all notice
def notice_list(request):
    notices = Notice.objects.all().order_by('-date_posted')
    return render(request,'notices/notice_list.html', {'notices': notices})

def create_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notice_list')  # Ensure this matches the name in urls.py
    else:
        form = NoticeForm()

    return render(request, 'notices/create_notice.html', {'form': form})