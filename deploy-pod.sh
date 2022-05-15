kubectl apply -f deployment/db-configmap.yaml
kubectl apply -f deployment/db-secret.yaml
kubectl apply -f deployment/postgres.yaml
kubectl apply -f deployment/api-connection.yaml
kubectl apply -f deployment/api-locations.yaml
kubectl apply -f deployment/api-persons.yaml
kubectl apply -f deployment/grpc-persons.yaml
kubectl apply -f deployment/udaconnect-app.yaml
kubectl apply -f deployment/kafka.yaml

#sh scripts/run_db_command.sh $(kubectl get pods | grep -i "postgres" | awk '{print $1}')
