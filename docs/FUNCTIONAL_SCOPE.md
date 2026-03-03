# FUNCTIONAL SCOPE – LWM-APP-WEB

## 🎯 Vision

Système simple de gestion interne pour une église locale.

Le projet évoluera progressivement par phases.

Pas de SaaS.
Pas de multi-tenant.
Pas de complexité inutile.

---

# 🥇 PHASE 1 – Fondation (Obligatoire)

Objectif : Base stable et propre.

Modules :

- Organisation (Zone → Pays → District → Assemblée)
- Membres
- Rôles
- Permissions
- Dashboard simple

## Structure organisationnelle officielle

Structure territoriale :

Continent
 └── Zone
      └── Pays
           └── District
                └── Assemblée
                     └── Membres

Départements :

- Créables dynamiquement
- Présents à tous les niveaux
- Transversaux

Fonctions :

- Un membre peut avoir plusieurs fonctions
- Une fonction est toujours liée :
  - à un niveau territorial
  - et éventuellement à un département

---

Critères de validation :

- Architecture respectée
- Séparation logique métier / HTTP
- Aucun fichier > 200 lignes
- Tests fonctionnels basiques validés
- Commit propre et documenté

---

# 🥈 PHASE 2 – Activité

Modules :

- Événements
- Présences
- Planning ministériel

Condition d'ouverture :

- Phase 1 stable
- Aucun bug critique
- Structure validée

---

# 🥉 PHASE 3 – Administration avancée

Modules :

- Finances
- Documents internes
- Communication interne
- Statistiques avancées

Condition d'ouverture :

- Phase 2 stable
- Architecture maintenue propre
- Aucune dette technique majeure

---

## 🔒 Règle importante

On ne passe à la phase suivante que lorsque la phase actuelle est stable.

Toute tentative d'accélération non contrôlée est interdite.

---

## 🧱 Discipline fonctionnelle

- Toujours développer par module isolé
- Toujours valider avant d’étendre
- Toujours respecter PROJECT_RULES.md
- Toujours mettre à jour CONTEXT.md en cas de décision majeure

