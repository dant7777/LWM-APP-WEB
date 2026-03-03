# WORKFLOW – LWM-APP-WEB

## 🛠 Méthode de correction

Quand un bug apparaît :

1. Décrire précisément l’erreur
2. Définir un objectif clair
3. Interdire tout refactor global
4. Appliquer une correction minimale et locale
5. Tester
6. Commit immédiat

---

## 🧠 Règle anti-oubli

Avant toute modification, toujours écrire :

Objectif :
Contraintes :
Impact attendu :

Aucune exception.

---

## 📏 Règle des fichiers

Maximum 200 lignes par fichier.

Si dépassement :
→ Division obligatoire
→ Création de module/service dédié

---

## 🔄 Processus standard de développement

1. Analyse
2. Définition objectif
3. Vérification des règles PROJECT_RULES.md
4. Implémentation minimale
5. Test
6. Commit
7. Mise à jour CONTEXT.md si nécessaire

---

## 🚫 Interdictions workflow

- Pas de correction dans la précipitation
- Pas de modification multiple non liée
- Pas de code temporaire laissé actif
- Pas de modification sans commit

---

## 🔁 Discipline continue

Si une erreur revient plusieurs fois :
→ Ajouter une règle dans PROJECT_RULES.md

Si une discussion devient longue :
→ Résumer dans CONTEXT.md

