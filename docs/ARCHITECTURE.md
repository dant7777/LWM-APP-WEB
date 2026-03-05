# ARCHITECTURE – LWM-APP-WEB

## 🎯 Orientation officielle du projet

LWM-APP-WEB est un outil interne destiné à une seule église locale.

Il ne s'agit pas d'une plateforme SaaS.
Il n'y a pas de multi-tenant.
Il n'y a pas de séparation par client.

L'architecture doit rester simple, maintenable et évolutive uniquement dans le cadre d'une seule organisation.
## 🎯 Objectif

Projet évolutif, structuré, maintenable sur plusieurs années.

Architecture pensée pour :
- Scalabilité
- Lisibilité
- Séparation stricte des responsabilités
- Évolution contrôlée

---

## 🖥 Backend

Technologie principale :
- Django

Principes :

- Structure modulaire
- Séparation stricte HTTP / logique métier
- Aucune logique métier dans les views
- Services dédiés pour la logique complexe
- Dossiers organisés par domaine métier

Structure cible :

backend/
│
├── apps/
│   ├── domain_1/
│   ├── domain_2/
│
├── core/
├── services/
└── config/

---

## 🎨 Frontend

Technologie principale :
- React

Principes :

- Séparation composants / logique
- Hooks dédiés pour la logique
- Composants purs (UI)
- Structure par domaine fonctionnel

Structure cible :

frontend/
│
├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── hooks/
│   └── domains/

---

## 🗄 Base de données

- PostgreSQL via Docker
- Pas d'accès direct non contrôlé
- Migrations versionnées
- Sauvegardes automatisées

---

## 🧱 Principes structurants

- Un fichier = une responsabilité
- Dossiers par domaine métier
- Services séparés des views
- Aucune logique métier dans les routes
- Aucun fichier > 200 lignes

---

## 🔐 Discipline architecturale

Toute modification structurelle doit :

1. Être justifiée
2. Être validée
3. Être documentée dans PROJECT_RULES.md si nécessaire
4. Être commitée immédiatement

## 🧩 Système d’affectation (Phase 1)

Le projet utilise un système d’affectation générique.

Un membre peut avoir plusieurs fonctions.

Une affectation contient :

- Le membre concerné
- Le niveau territorial concerné
- Le département (optionnel)
- La fonction

Ce système évite la multiplication de champs spécifiques
(pasteur_zone, responsable_finance_district, etc.).

Il garantit flexibilité et évolutivité.

## 🧩 Modèle d'affectation – Phase 1

Le système utilise une entité Affectation simple et explicite.

Champs conceptuels :

- membre
- fonction
- département (optionnel)
- continent (nullable)
- zone (nullable)
- pays (nullable)
- district (nullable)
- assemblee (nullable)

Règle métier :

Une affectation concerne un seul niveau territorial à la fois.

Ce choix privilégie :
- la lisibilité
- la simplicité
- la maintenabilité
- l'absence de sur-ingénierie

## 👤 Modèle Membre – Phase 1

Un Membre représente une personne réelle dans l'église.

Un membre peut exister sans avoir de compte utilisateur.

Un membre peut avoir plusieurs affectations.

Champs conceptuels :

Identité :
- nom
- prenom
- sexe
- date_naissance

Contact :
- telephone
- email
- adresse

Appartenance :
- assemblee (obligatoire)
- date_integration
- statut

Technique :
- utilisateur (optionnel)

Statut possible :

- Actif
- Inactif
- Décédé
- Transféré

Le statut influence :
- l'affichage dans le dashboard
- l'éligibilité aux affectations
- les statistiques futures

## 🔐 Système de permissions – Phase 1

Le projet utilise un système mixte.

Deux niveaux existent :

### Rôles techniques

Contrôlent l'accès au système.

Exemples :
- SuperAdmin
- Admin
- Gestionnaire
- Utilisateur

### Fonctions métier

Les responsabilités dans l'église sont gérées via le système d'Affectation.

Une fonction est liée :
- à un membre
- à un niveau territorial
- éventuellement à un département

## 🏗 Organisation du backend

Le backend Django est organisé par domaines métier.

Applications principales :

- core
- users
- members
- organisation
- departments
- assignments
- dashboard

Chaque application doit respecter :

- responsabilité claire
- séparation logique métier / HTTP
- fichiers < 200 lignes

## 🌐 Architecture applicative

Le projet utilise une architecture séparée :

Frontend : React  
Backend : Django REST API  
Database : PostgreSQL

Communication :

React consomme les endpoints exposés par l’API Django.

Cela permet :

- séparation claire frontend / backend
- évolution indépendante des couches
- intégration facile avec Docker