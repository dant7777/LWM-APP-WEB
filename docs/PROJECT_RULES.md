# PROJECT RULES – LWM-APP-WEB

## 🔒 Règles fondamentales (NON NÉGOCIABLES)

1. On ne supprime jamais une architecture existante sans validation.
2. On ne refactorise pas massivement pour corriger une erreur.
3. Toute modification doit être minimale et locale.
4. Aucun fichier ne doit dépasser 200 lignes.
5. Toute logique métier doit être séparée.
6. Chaque modification doit être commitée.
7. Toujours analyser avant de coder.
8. Tout contenu documentaire doit être généré automatiquement.
9. Éviter au maximum l’édition manuelle des fichiers.
10.Ne modifie jamais : PROJECT_RULES.md AI_SESSION_PROTOCOL.md Sans réflexion. Ce sont tes garde-fous.

---

## 🔁 Règles évolutives du projet

⚠ Cette section est mise à jour au fur et à mesure de l’avancement du projet.

### Principe :

- Toute erreur structurelle importante donne naissance à une nouvelle règle.
- Toute mauvaise pratique répétée devient une règle formelle.
- Toute décision architecturale forte devient une règle écrite.
- Toute dette technique constatée doit être encadrée par une règle.

### Format d’ajout obligatoire :

### Règle #X – [Titre court]

Date :
Contexte :
Problème rencontré :
Décision :
Impact :

---

## 🧠 Rappel automatique à chaque nouvelle session

Avant toute nouvelle implémentation, vérifier :

- Est-ce que cette modification viole une règle ?
- Est-ce qu’une nouvelle règle doit être créée ?
- Est-ce que CONTEXT.md doit être mis à jour ?

---

## 🧩 Discipline d’évolution

Si une discussion devient longue :
→ Résumer dans CONTEXT.md

Si un nouveau chat est ouvert :
→ Copier CONTEXT.md avant toute demande.

Si une erreur majeure survient :
→ Ajouter une règle dans la section “Règles évolutives”.

---

## ⚠ Interdictions

- Pas de suppression globale
- Pas de "réécriture complète"
- Pas de modification silencieuse de structure
- Pas d’ajout de dépendance sans justification
- Pas de code temporaire laissé en production

---

## 🧱 Principe directeur du projet

Stabilité > Rapidité  
Clarté > Complexité  
Structure > Improvisation  

---

## 🔔 Discipline Projet

À chaque milestone important :

1. Relire PROJECT_RULES.md
2. Vérifier si une nouvelle règle doit être ajoutée
3. Mettre à jour la section “Règles évolutives”
4. Commit immédiat
