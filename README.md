# VendreFacile - Plateforme de Petites Annonces

VendreFacile est une plateforme web inspirée de LeBonCoin, permettant de publier, consulter et rechercher des petites annonces gratuites, avec une messagerie interne pour faciliter les échanges.

## Fonctionnalités Clés (MVP)

*   **Gestion des Annonces :** Créer, lire, mettre à jour, supprimer des annonces.
*   **Comptes Utilisateurs :** Inscription, connexion, gestion de profil.
*   **Messagerie Intégrée :** Échanges directs entre acheteurs et vendeurs.
*   **Recherche Avancée :** Filtrage par catégorie, lieu, prix.
*   **Favoris :** Sauvegarder les annonces intéressantes.
*   **Géolocalisation :** Afficher les annonces sur une carte.
*   **Responsive Design :** Expérience utilisateur optimale sur mobile et desktop.

## Architecture en Bref

*   **Frontend :** React (Single Page Application)
*   **API Gateway :** Flask (Point d'entrée unique)
*   **Backend :** Microservices en Python (FastAPI)
*   **Base de Données :** MariaDB / MySQL
*   **Messagerie Asynchrone :** RabbitMQ
*   **Conteneurisation :** Docker

## Démarrage Rapide

Suivez ces étapes pour lancer VendreFacile sur votre machine locale.

### Prérequis

*   Git
*   Docker et Docker Compose
*   Node.js (v16+) et npm (ou Yarn)

### 1. Lancer le projet

```bash
git clone https://github.com/TheoPERSONNE/TpGroupeArchiLogi

cd TpGroupeArchiLogi

Lancer les services
docker-compose up --build -d

