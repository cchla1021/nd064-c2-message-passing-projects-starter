kubectl delete -f deployment/db-configmap.yaml
kubectl delete -f deployment/db-secret.yaml
kubectl delete -f deployment/postgres.yaml
kubectl delete -f deployment/api-connection.yaml
kubectl delete -f deployment/api-locations.yaml
kubectl delete -f deployment/api-persons.yaml
kubectl delete -f deployment/grpc-persons.yaml
kubectl delete -f deployment/udaconnect-app.yaml
kubectl delete -f deployment/kafka.yaml
