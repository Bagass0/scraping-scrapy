# Utiliser une image de base avec Python
FROM python:3.9

# Mettre en place le répertoire de travail
WORKDIR /app

# Copier le fichier spider dans le conteneur
COPY ScrapEbay/spiders/ebay_spider.py .

# Installer Scrapy et ses dépendances
RUN pip install --no-cache-dir scrapy tqdm

# Commande à exécuter lorsque le conteneur démarre
CMD ["scrapy", "runspider", "ebay_spider.py"]