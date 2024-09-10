from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req, 'home.html')

def chat_room(req):
    room_name = req.GET.get('room_name')
    user_name = req.GET.get('user_name')

    context = {
        'room_name': room_name,
        'user_name': user_name,
    }
    return render(req, 'chat_room.html', context)