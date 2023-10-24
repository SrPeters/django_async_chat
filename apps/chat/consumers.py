from channels.generic.websocket import WebsocketConsumer
import json


class ChatRoomConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        # self.room_group_name = f'chat_{self.room_name}'

        # self.channel_layer.group_add(
        #     self.room_group_name,
        #     self.channel_name
        # )

        
        # self.channel_layer.send('event', {
        #     'type': 'message',
        #     'channel': self.room_group_name,
        #     'text': 'Websockets!'
        # })

        # self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'group_message',
        #         'data': {
        #             'app': 'Websockets!'
        #         }
        #     }
        # )

    
    # async def group_message(self, event):
    #     data = event['data']
    #     await self.send(text_data=json.dumps(data))
    

    def disconnect(self, code):
        pass


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({'message': message}))
        
        # self.channel_layer.group_discard(
        #     self.room_group_name,
        #     self.channel_name
        # )
