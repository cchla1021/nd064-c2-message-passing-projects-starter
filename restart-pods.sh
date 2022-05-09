kubectl delete -f deployment/db-configmap.yaml
kubectl delete -f deployment/db-secret.yaml
kubectl delete -f deployment/postgres.yaml
kubectl delete -f deployment/udaconnect-api.yaml
kubectl delete -f deployment/udaconnect-app.yaml
sleep 1
kubectl apply -f deployment/db-configmap.yaml
kubectl apply -f deployment/db-secret.yaml
kubectl apply -f deployment/postgres.yaml
kubectl apply -f deployment/udaconnect-api.yaml
kubectl apply -f deployment/udaconnect-app.yaml

sh scripts/run_db_command.sh $(kubectl get pods | grep -i "postgres" | awk '{print $1}')
