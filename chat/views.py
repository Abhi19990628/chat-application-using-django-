from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Room,Message

@login_required
def home(request):
    rooms = Room.objects.all()
    return render(request, 'chat/home.html', {'rooms': rooms})

@login_required
def room(request, room_id):
    room = Room.objects.get(id=room_id)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    return render(request, 'chat/room.html', {'room': room, 'messages': messages})

@login_required
def send_message(request, room_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        room = Room.objects.get(id=room_id)
        user = request.user
        Message.objects.create(room=room, user=user, content=content)
    return redirect('room', room_id=room_id)

