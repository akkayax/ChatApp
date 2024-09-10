from django.shortcuts import render
from .models import ChatRoom, Message
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(req):
    return render(req, 'home.html')

def chat_room(req):
    room_name = req.GET.get('room_name')
    user_name = req.GET.get('user_name')

    room, created = ChatRoom.objects.get_or_create(name=room_name)

    if req.method == 'POST':
        message_content = req.POST.get('message')
        if message_content:
            Message.objects.create(room=room, user=user_name, content=message_content)

    messages = Message.objects.filter(room=room).order_by('timestamp')

    context = {
        'room_name': room_name,
        'user_name': user_name,
        'messages': messages,
    }
    
    return render(req, 'chat_room.html', context)