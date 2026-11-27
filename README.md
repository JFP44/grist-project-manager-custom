# Grist Project Manager

Outil de gestion et de pilotage de formulaires COILIBRIS intégré à Grist

## Présentation

Grist Project Manager est un widget personnalisé développé pour la plateforme [Grist](https://www.getgrist.com/).

Il permet de centraliser le suivi des formulaires, des tâches et des intervenants au sein d'une interface unique, directement intégrée dans un document Grist.

L'objectif est de proposer un outil collaboratif, simple d'utilisation et adaptable aux organisations administratives et aux équipes de travail.

## Fonctionnalités principales

### Gestion des formulaires COLIBRIS
- Création et modification des formulaires
- Affectation d'un service demandeur.
- Désignation des référents métier et des développeurs.
- Suivi des tickets et des références associées.
- Visualisation de l'avancement des formulaires.

### Gestion des tâches
- Création et modification des tâches.
- Affectation des tâches aux intervenants.
- Gestion des statuts.
- Suivi des échéances.
- Gestion des dépendances entre tâches.
- Commentaires et pièces jointes.
- Suivi du temps consacré aux tâches.

### Gestion des utilisateurs et des rôles

L'application distingue plusieurs profils :

| Profil | Principales autorisations |
|---|---|
| Administrateur | Accès complet à l'application et à sa configuration |
| Développeur | Gestion des formulaires, des tâches et des utilisateurs |
| Superviseur | Suivi des formulaires et gestion des tâches |
| Référent métier | Consultation des formulaires de son service et suivi des tâches associées |

Les autorisations sont adaptées au profil de chaque utilisateur et complétées par les règles de contrôle d'accès de Grist.

### Statistiques et pilotage
- Indicateurs de suivi des formulaires.
- Avancement des tâches.
- Suivi des échéances.
- Indicateurs de charge et d'activité selon les autorisations.

## Architecture technique

Le projet repose sur plusieurs composants :

- **Grist** : stockage des données, gestion des tables et contrôle des accès.
- **JavaScript** : logique applicative et interactions.
- **HTML / CSS** : interface utilisateur.
- **Grist Custom Widgets** : intégration dans les documents Grist.
- **Git** : gestion du code source et des versions.
- **Vercel** : hébergement et déploiement du widget.

## Structure des données

Les principales tables utilisées dans Grist sont :

| Table | Rôle |
|---|---|
| PM_Projects | formulaires |
| PM_Tasks | Tâches |
| PM_Users | Utilisateurs |
| PM_Services | Services |
| PM_Tags | Étiquettes |
| PM_Statuts | Référentiel des statuts |
| PM_UserInfo | Informations utilisateur |
| PM_Dependencies | Dépendances entre tâches |
| PM_Comments | Commentaires |
| PM_TimeEntries | Suivi du temps |

## Installation et déploiement

Le widget est conçu pour être hébergé indépendamment du document Grist.

Le déploiement s'effectue à partir du dépôt Git du projet, avec publication du widget sur un hébergement web compatible.

Le widget est ensuite déclaré dans Grist à l'aide de son URL de déploiement.

## Environnement du projet

- Dépôt source : `JFP44/grist-project-manager-custom`
- Plateforme de données : Grist
- Hébergement : Vercel
- Langages : JavaScript, HTML et CSS

## Évolutions

Le projet est conçu pour évoluer progressivement en fonction des besoins des utilisateurs et des retours d'expérience.

Les évolutions peuvent notamment porter sur :
- L'amélioration des outils de pilotage.
- L'enrichissement des statistiques.
- L'amélioration de l'ergonomie.
- L'adaptation des droits et des profils.
- L'ajout de nouvelles fonctionnalités.

## Licence

Licence à préciser.

