import json
import jwt

from django.http  import JsonResponse
from django.views import View

from users.models          import User
from eightpercent.settings import SECRET_KEY, ALGORITHM

class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            user = User.objects.get(email = data['email'])
            
            if user.password != data['password']:
                return JsonResponse({"message": "INVALID_PASSWORD!"}, status=401)

            access_token = jwt.encode({'user_id' : user.id}, SECRET_KEY , algorithm=ALGORITHM)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_EMAIL!"}, status=401)
        
        return JsonResponse({"token": access_token}, status=201)