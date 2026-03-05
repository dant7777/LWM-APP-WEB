# API CONTRACT – LWM-APP-WEB

## 🎯 Objectif

Définir les endpoints principaux de l'API.

L'API suit une architecture REST simple.

---

# Organisation

/api/continents/
/api/zones/
/api/pays/
/api/districts/
/api/assemblees/

---

# Membres

/api/members/

---

# Départements

/api/departments/

---

# Affectations

/api/assignments/

---

# Authentification

/api/auth/login/
/api/auth/logout/
/api/auth/me/

---

# Dashboard

/api/dashboard/

---

## Règles

- API REST
- JSON uniquement
- endpoints cohérents
- aucune logique métier dans les vues

# Authentification

Le projet utilise une authentification JWT.

Endpoints :

POST /api/auth/login/
POST /api/auth/refresh/
POST /api/auth/logout/
GET  /api/auth/me/

Les requêtes authentifiées doivent envoyer :

Authorization: Bearer <access_token>

## 🐳 Infrastructure

Le projet est déployé avec Docker.

Services :

- frontend : React
- backend : Django REST API
- database : PostgreSQL

Chaque service fonctionne dans un conteneur séparé.

La coordination des services est gérée par docker-compose.