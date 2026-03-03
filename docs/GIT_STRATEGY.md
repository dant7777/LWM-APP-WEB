# GIT STRATEGY – LWM-APP-WEB

## 🌿 Branches

main → stable  
dev → développement  

Règle :
- main ne doit jamais casser
- Tout développement passe par dev

---

## 📝 Commits

WIP autorisé.

Toujours commit avant :
- Modification risquée
- Refactor
- Migration
- Suppression

Format recommandé :

type(scope): description courte

Exemple :
fix(auth): correction validation token

---

## 💾 Sauvegarde rapide

git add .
git commit -m "WIP"
git push

Même si le code n'est pas parfait.

---

## 🔒 Discipline Git

- Pas de modification massive non commitée
- Pas de code non versionné
- Pas de travail local > 24h sans push
- Toujours pouvoir revenir en arrière

