from django.shortcuts import render

# Create your views here.
#https://www.youtube.com/watch?v=F4nwRQPXD8w
#https://github.com/veryacademy/YT-Django-Project-Chatroom-Getting-Started/blob/master/chat/views.py
# https://channels.readthedocs.io/en/latest/tutorial/part_1.html

def index(request):
  context = {}
  return render(request, 'websockets_chat/index.html', context)


def room(request, room_name):
  context = {'room_name': room_name}
  return render(request, 'websockets_chat/chat_room.html', context)







