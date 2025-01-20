#!/bin/bash


echo "Minikube başlatiliyor..."
minikube start


echo "MongoDB Deployment başlatiliyor..."
kubectl apply -f mongodb-deployment.yaml


echo "MongoDB deployment'i kontrol ediliyor..."
kubectl rollout status deployment mongodb-deployment --timeout=1000s


kubectl get pods -l app=mongodb


echo "MongoDB Pod'lari hazir."
sleep 5 

echo "MongoDB Pod'lari hazir.App deployment hazirlaniyor"
kubectl apply -f python-app-deployment.yaml


kubectl rollout status deployment python-app-deployment --timeout=600s

echo "Proje başariyla ayağa kalkti!"

minikube service python-app-service