import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password  

from crud_article.models import Auteur
@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')

        if not all([name, email, password, role]):
            return JsonResponse({'error': 'Missing fields'}, status=400)

        # ✅ Valider le rôle
        if role not in ['auteur', 'user']:
            return JsonResponse({'error': "Role must be either 'auteur' or 'user'"}, status=400)

        if Auteur.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=409)

        auteur = Auteur.objects.create(
            username=name,
            email=email,
            password=make_password(password),
            role=role
        )

        return JsonResponse({'message': 'Account created'}, status=201)
    return JsonResponse({'error': 'Invalid method'}, status=405)


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        email = data.get('email')
        password = data.get('password')

        try:
            user = Auteur.objects.get(email=email)
        except Auteur.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)

        if check_password(password, user.password):
            return JsonResponse({'message': 'Login successful', 'user_id': user.id})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    return JsonResponse({'error': 'Invalid method'}, status=405)
