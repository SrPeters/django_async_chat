import os
from django.core.asgi import get_asgi_application
from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from apps.chat import consumers

django_asgi_app = get_asgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'async_chat.settings')

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # "websocket": AllowedHostsOriginValidator(
    #     AuthMiddlewareStack(
    #         URLRouter([
    #             re_path(r"^front(end)/$", consumers.ChatRoomConsumer.as_asgi()),
    #         ])
    #     )
    # ),
})