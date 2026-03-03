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