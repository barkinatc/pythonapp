#!/bin/bash

# Minikube'u başlat
echo "Minikube başlatiliyor..."
minikube start

# MongoDB Deployment dosyasını Kubernetes'e uygula
echo "MongoDB Deployment başlatiliyor..."
kubectl apply -f mongodb-deployment.yaml

# MongoDB Deployment durumunu kontrol et ve başarılı bir şekilde tamamlanıp tamamlanmadığını bekle
echo "MongoDB deployment'i kontrol ediliyor..."
kubectl rollout status deployment mongodb-deployment --timeout=1000s

# MongoDB Pod'larının durumunu kontrol et
kubectl get pods -l app=mongodb

# MongoDB Pod'larının "Ready" olduğunu kontrol et
echo "MongoDB Pod'lari hazir."
sleep 5 

echo "MongoDB Pod'lari hazir.App deployment hazirlaniyor"
kubectl apply -f python-app-deployment.yaml


kubectl rollout status deployment python-app-deployment --timeout=600s

echo "Proje başariyla ayağa kalkti!"

minikube service python-app-service