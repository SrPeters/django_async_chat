from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json


class ChatRoomConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'group_message',
                'data': {
                    'app': 'Websockets!'
                }
            }
        )

    
    async def group_message(self, event):
        data = event['data']
        await self.send(text_data=json.dumps(data))
    

    async def disconnect(self, code):
        
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
