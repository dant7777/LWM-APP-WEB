# BACKUP POLICY – LWM-APP-WEB

## 🔐 Triple sauvegarde obligatoire

1. PC local
2. GitHub / GitLab
3. VPS

Aucune exception.

---

## ⏳ Règle temporelle

Jamais plus de 24h sans push.

Si travail important :
→ Push immédiat

---

## 🚨 En cas d'erreur

Voir historique :

git log

Restaurer un fichier :

git checkout ID_COMMIT -- fichier

Revenir à un commit :

git reset --hard ID_COMMIT

---

## 🛡 Principe

Si ce n'est pas pushé :
→ Ce n'est pas sauvegardé.

