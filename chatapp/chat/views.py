from django.shortcuts import render
from django.shortcuts import render
from .models import Message

def chat_view(request):
    messages = Message.objects.all().order_by('timestamp')
    return render(request, 'chat/chat.html', {'messages': messages})

# Create your views here.
