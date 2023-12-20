# my_app/authentication.py
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.response import Response
from Users.models import *
import jwt
from django.conf import settings
from rest_framework.views import exception_handler


SECRET = getattr(settings,'SECRET','secret')
ALGO = getattr(settings,'ALGO','HS256')

class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1] 

            if not token:
                raise exceptions.AuthenticationFailed('Unauthenticated')
            else:
                try:
                    payload = jwt.decode(token, SECRET, algorithms=ALGO)
                except jwt.InvalidSignatureError:    
                    raise exceptions.AuthenticationFailed('Token Invalid')
                except jwt.ExpiredTokenError:
                    raise exceptions.AuthenticationFailed('Token Expired')
                except IndexError:
                    raise exceptions.AuthenticationFailed('Token prefix missing')
                except Exception as e:
                    raise exceptions.AuthenticationFailed(str(e))
            user = User.objects.filter(id=int(payload['id'])).first()
            if user is None:
                raise exceptions.AuthenticationFailed('Invalid token')
            elif user.is_active == False:
                raise exceptions.AuthenticationFailed('Your account has been deactivated')
            else:
                try:
                    return (user, None)
                except Exception as e:
                    raise exceptions.AuthenticationFailed(str(e))
            
            return (user, None)
        except Exception as e:
            raise exceptions.AuthenticationFailed(str(e))

