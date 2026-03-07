# ARCHITECTURE – LWM-APP-WEB

## Orientation officielle du projet

LWM-APP-WEB est un outil interne destiné à une seule église locale.

Ce n'est pas une plateforme SaaS.
Il n'y a pas de multi-tenant.
Il n'y a pas de séparation par client.

L'architecture doit rester simple, maintenable et évolutive pour une seule organisation.

---

## Objectif

Projet évolutif, structuré, maintenable sur plusieurs années.

Architecture pensée pour :

- Scalabilité
- Lisibilité
- Séparation stricte des responsabilités
- Evolution contrôlée

---

# Backend

Technologie principale :

Django

Principes :

- Structure modulaire
- Séparation HTTP / logique métier
- Aucune logique métier dans les views
- Services dédiés pour la logique complexe
- Organisation par domaines

Structure actuelle :

backend/
¦
+-- organisation/
+-- members/
+-- departments/
+-- assignments/
+-- users/
+-- core/
+-- dashboard/
+-- config/

---

# Frontend

Technologie principale :

React

Structure cible :

frontend/
¦
+-- src/
¦   +-- components/
¦   +-- pages/
¦   +-- services/
¦   +-- hooks/
¦   +-- domains/

---

# Base de données

PostgreSQL via Docker

Principes :

- migrations versionnées
- sauvegardes automatisées
- accès contrôlé

---

# Principes structurants

- Un fichier = une responsabilité
- Dossiers par domaine métier
- Services séparés des views
- Aucune logique métier dans les routes
- Aucun fichier > 200 lignes

---

# Système d'affectation (Phase 1)

Un membre peut avoir plusieurs fonctions.

Une affectation contient :

- membre
- fonction
- département (optionnel)
- continent
- zone
- pays
- district
- assemblée

Règle :

Une affectation concerne un seul niveau territorial.

---

# Modèle Membre

Un membre représente une personne réelle dans l'église.

Champs :

Identité

- nom
- prenom
- sexe
- date_naissance

Contact

- telephone
- email
- adresse

Appartenance

- assemblee
- date_integration
- statut

Technique

- utilisateur (optionnel)

Statuts :

- Active
- Inactive
- Deceased
- Transferred

---

# Organisation API

Hiérarchie :

Continent  
+ Zone  
 + Country  
  + District  
   + Assembly  

Endpoints :

/api/continents/
/api/zones/
/api/countries/
/api/districts/
/api/assemblies/

---

# Architecture API

models ? serializers ? viewsets ? routers ? API

Stack :

- Django
- Django REST Framework
- SQLite (dev)
- PostgreSQL (Docker)
- Docker Compose
