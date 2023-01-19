Robin Wagner

# TP Devops: Docker/Kubernetes

Introduction: 

Le but de ce TP est de réaliser une application puis de la dockeriser dans deux containers. Faire la même chose sur Kubernetes.

Application:

Docker :

dans le terminal : 
    $ docker-compose up

(l'image de l'application est créé directement dans un build de docker-compose)


=> L'application est accessible avec localhost:3380

Consigne:

(entre quote les variables)

Faites dans votre chemin :
    / pour connaitre vos produits
    /insert/'nom'/'prix' pour ajouter un nouveau produit avec le nom et le prix voulu
    /'numéro' pour afficher le produit à tel numéro


Kubernetes:

dans le terminal : 
    $ minikube start
    $ eval $(minikube -p minikube docker-env)
    $ docker build -t devops .
    $ kubectl apply -f config-map.yaml
    $ kubectl apply -f deploy-sql.yaml
    $ kubectl apply -f deploy-python.yaml
    $ minikube service myapp-service


Faites dans votre chemin :
    /pour connaitre vos produits
    /insert/'nom'/'prix' pour ajouter un nouveau produit avec le nom et le prix voulu
    /'numéro' pour afficher le produit à tel numéro

