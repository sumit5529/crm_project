"""
ASGI config for crm project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')

# application = get_asgi_application()
import os
from channels.http import AsgiHandler
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import chatapp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = ProtocolTypeRouter({
        'http':get_asgi_application(),
        'websocket':AuthMiddlewareStack(
            URLRouter(
                chatapp.routing.websocket_urlpatterns
            )
        )  
})
