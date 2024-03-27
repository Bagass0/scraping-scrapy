# Utiliser une image de base avec Python
FROM python:3.9

# Mettre en place le répertoire de travail
WORKDIR /app

# Copier le fichier spider dans le conteneur
COPY spiders/ebay_spider.py .

# Installer Scrapy et ses dépendances
RUN pip install --no-cache-dir scrapy==2.6.0

# Commande à exécuter lorsque le conteneur démarre
CMD ["scrapy", "runspider", "spiders/ebay_spider.py"]
