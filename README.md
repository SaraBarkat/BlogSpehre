# 📝 Blogify

Bienvenue sur **Blogify**, une plateforme de blogging moderne permettant aux auteurs de créer, gérer et publier leurs articles facilement, avec une interface claire et intuitive.

---

## 🚀 Fonctionnalités principales

- Publication d'articles avec éditeur simple
- Tableau de bord pour les auteurs
- Authentification sécurisée
- Interface responsive pour tous les appareils

---

## 📸 Aperçu de l'application

### 🏠 Landing Page

<div align="center">
  <img src="./screenshots/landing-page.png" alt="Landing Page" width="80%">
</div>

---

### 📊 Tableau de bord Auteur

<div align="center">
  <img src="./screenshots/dashboard-author.png" alt="Dashboard Auteur" width="80%">
</div>

---

### 🔐 Authentification

| Inscription | Connexion | Mot de passe oublié |
|-------------|-----------|----------------------|
| ![Sign Up](./screenshots/signup.png) | ![Sign In](./screenshots/signin.png) | ![Forgot Password](./screenshots/forgot-password.png) |

---

## 🛠️ Technologies utilisées

- **Frontend** : HTML, CSS, JavaScript  
- **Backend** : Django  
- **Base de données** : MySQL

---

## 📁 Structure du projet


---

## 🚀 Lancer l'application en local

### 1. Cloner le dépôt

```bash
git clone https://github.com/SaraBarkat/Blogify.git
cd blogify
cd backend
python -m venv env
source env/bin/activate  # ou env\Scripts\activate sous Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
