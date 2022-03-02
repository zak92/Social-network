import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
      # get chat room name from the URL route
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # create a new  group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # Accepts the WebSocket connection
        await self.accept()

   # discard group
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # receive message
    async def receive(self, text_data):
      # get data from user
        text_data_json = json.loads(text_data)
        # extract message
        message = text_data_json['message']
        username = text_data_json['username']

        # send to group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']
    
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))

    pass