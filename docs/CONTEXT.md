# CONTEXT – LWM-APP-WEB

⚠ Ce fichier doit être mis à jour régulièrement.

---

## 🏗 Architecture actuelle

Backend : Django (structure modulaire)
Frontend : React (séparation composants / logique)
Base de données : PostgreSQL via Docker

---

## 📌 Décisions importantes

- Structure modulaire par domaine
- Fichier maximum 200 lignes
- Correction minimale uniquement
- Documentation générée automatiquement

---

## 🐞 Problèmes connus

(Aucun pour le moment)

---

## ⚠ Points sensibles

- Respect strict des règles PROJECT_RULES.md
- Pas de refactor global
- Pas de suppression sans validation

---

## 🔁 Rappels permanents

Ne jamais supprimer sans validation.  
Correction minimale uniquement.  
Toujours commit avant modification risquée.  

## Orientation officielle

Projet interne pour une seule église locale.
Développement progressif par phases.
Complexité contrôlée.


---

## Progress Update

Backend foundation implemented:

✔ Django project structure  
✔ Organisation hierarchy models  
✔ Migrations applied  
✔ Django REST Framework API  
✔ Router endpoints for organisation  
✔ API tested (200 OK)

Next milestone:

Member / Department / Assignment domain models.
