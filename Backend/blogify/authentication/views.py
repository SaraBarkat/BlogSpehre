import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from crud_article.models import Auteur
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import  get_object_or_404



@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
            except:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)
        else:
            data = request.POST

        first_name = data.get('first_name')
        family_name = data.get('family_name')
        email = data.get('email')
        password = data.get('password')

        if not all([first_name, family_name, email, password]):
            error_msg = 'All fields are required'
            if request.content_type == 'application/json':
                return JsonResponse({'error': error_msg}, status=400)
            return render(request, 'register.html', {'error': error_msg})

        if Auteur.objects.filter(email=email).exists():
            error_msg = 'Email already exists'
            if request.content_type == 'application/json':
                return JsonResponse({'error': error_msg}, status=409)
            return render(request, 'register.html', {'error': error_msg})

        username = f"{first_name} {family_name}"
        auteur = Auteur.objects.create(
            username=username,
            first_name=first_name,
            family_name=family_name,
            email=email,
            password=make_password(password),
        )

        if request.content_type != 'application/json':
            return redirect('author_dashboard', author_id=auteur.id)

        return JsonResponse({'message': 'Account created'}, status=201)

    return JsonResponse({'error': 'Invalid method'}, status=405)


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
            except:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)
        else:
            data = request.POST

        email = data.get('email')
        password = data.get('password')

        try:
            user = Auteur.objects.get(email=email)
        except Auteur.DoesNotExist:
            error_msg = 'Invalid email or password'
            if request.content_type == 'application/json':
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
            return render(request, 'login.html', {'error': error_msg})

        if check_password(password, user.password):
            if request.content_type != 'application/json':
                return redirect('author_dashboard', author_id=user.id)
            return JsonResponse({'message': 'Login successful', 'user_id': user.id})
        else:
            if request.content_type == 'application/json':
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
            return render(request, 'login.html', {'error': 'Invalid email or password'})

    return JsonResponse({'error': 'Invalid method'}, status=405)


def logout_view(request):
    logout(request)
    return redirect('home')


@csrf_exempt
def update_profil(request, user_id):
    if request.method == 'POST':
        try:
            user = Auteur.objects.get(id=user_id)
        except Auteur.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

        bio = request.POST.get('bio')
        image = request.FILES.get('image')
        profession = request.POST.get('profession')

        if bio:
            user.bio = bio
        if profession:
            user.profession = profession
        if image:
            user.image = image

        user.save()
        return JsonResponse({'message': 'Profile updated successfully'})

    return JsonResponse({'error': 'Invalid method'}, status=405)


@csrf_exempt
def get_profil(request, user_id):
    if request.method == 'GET':
        try:
            user = Auteur.objects.get(id=user_id)
            data = {
                'id': user.id,
                'first_name': user.first_name,
                'family_name': user.family_name,
                'username': user.username,
                'email': user.email,
                'image_url': user.image.url if user.image else None,
                'bio': user.bio,
                'profession': user.profession,
            }
            return JsonResponse(data)
        except Auteur.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

    return JsonResponse({'error': 'Invalid method'}, status=405)
@csrf_exempt
def author_settings(request, author_id):
    author = get_object_or_404(Auteur, id=author_id)

    if request.method == 'POST':
        # Récupération des champs du formulaire
        author.first_name = request.POST.get('first_name')
        author.family_name = request.POST.get('family_name')
        author.email = request.POST.get('email')
        author.profession = request.POST.get('profession')  
        author.bio = request.POST.get('bio')  

        # Traitement de l'image (champ "photo" côté form, mais "image" dans le modèle)
        if 'photo' in request.FILES:
            uploaded_file = request.FILES['photo']
            if uploaded_file.content_type in ['image/jpeg', 'image/png', 'image/webp']:
                author.image = uploaded_file  # image = champ du modèle Auteur

        # Changement de mot de passe
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password and new_password == confirm_password:
            author.set_password(new_password)

        author.save()

        # Redirection après la mise à jour
        return redirect('author_dashboard', author_id=author.id)

    return render(request, 'auteurDashboard.html', {'author': author})