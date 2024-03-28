## Description du Code

Ce code est un web scraper utilisant le framework Scrapy pour extraire des informations à partir de la page des offres eBay. Les données extraites sont ensuite stockées dans une base de données SQLite.

## Structure du Code

Le code se compose d'une classe principale `EbaySpiderSpider` qui hérite de la classe `scrapy.Spider`. Voici une explication détaillée de chaque partie du code :

### Initialisation de la Base de Données

Dans la méthode `__init__`, une connexion à la base de données SQLite est établie. Si la table `products` n'existe pas encore, elle est créée avec les colonnes nécessaires pour stocker les informations des produits.

### Fermeture de la Connexion

La méthode `close` est appelée lorsque la connexion au spider est fermée. Avant de fermer la connexion, elle affiche les résultats de la base de données.

### Extraction des Données

La méthode `parse` est utilisée pour extraire les informations pertinentes à partir de la réponse HTML de la page des offres eBay. Les données extraites sont l'image du produit, le nom, le prix actuel, l'ancien prix (s'il y en a un), et la réduction (s'il y en a une). Ces informations sont ensuite insérées dans la base de données.

### Affichage des Résultats de la Base de Données

La méthode `print_database_results` interroge la base de données pour récupérer toutes les entrées de la table `products` et les affiche à l'écran.

## Utilisation du Code

Pour utiliser ce code, assurez-vous d'avoir Scrapy installé. Vous pouvez exécuter le spider en utilisant la commande `scrapy crawl ebay_spider` dans le terminal. Les données extraites seront stockées dans le fichier `ebay.db`.

Assurez-vous également d'avoir les permissions nécessaires pour créer et écrire dans des fichiers sur votre système de fichiers.