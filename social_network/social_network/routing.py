from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import websockets_chat.routing 


# routing once a websockets request is received
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websockets_chat.routing.websocket_urlpatterns
        )
    ),
})