# Projet de Scraping eBay avec Scrapy

Ce projet utilise le framework Scrapy pour extraire des informations à partir de la page des offres eBay.

## Structure du Projet

Le projet est organisé comme suit :


- **ScrapEbay/** : Répertoire racine du projet.
  - **ScrapEbay/** : Module principal du projet.
    - **items.py** : Définition des items pour stocker les données extraites.
    - **pipelines.py** : Implémentation des pipelines de traitement des données.
    - **settings.py** : Configuration du projet Scrapy.
    - **spiders/** : Répertoire contenant les spiders Scrapy.
      - **ebay_spider.py** : Spider principal pour extraire les données eBay.
- **scrapy.cfg** : Fichier de configuration Scrapy.
- **ebay.db** : Base de données SQLite pour stocker les données extraites.

## Fonctionnement

### Spider eBay

Le spider `ebay_spider` extrait les informations telles que l'image, le nom, le prix, le prix précédent et la réduction des produits à partir de la page des offres eBay.

### Items

Les items sont définis dans le fichier `items.py`. Chaque item correspond à un produit eBay et comprend les champs suivants :
- `image` : URL de l'image du produit.
- `name` : Nom du produit.
- `price` : Prix actuel du produit.
- `old_price` : Prix précédent du produit (s'il existe).
- `discount` : Montant de la réduction du produit (s'il existe).

### Pipeline

Les données extraites sont envoyées au pipeline `EbayPipeline` pour être traitées et stockées dans la base de données SQLite `ebay.db`.

## Configuration

Le pipeline `EbayPipeline` est activé dans le fichier `settings.py` avec la priorité 300.
