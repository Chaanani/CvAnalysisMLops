SERVICE_NAME="my-python-app-service"
NODE_PORT=$(kubectl get svc $SERVICE_NAME -o=jsonpath='{.spec.ports[0].nodePort}')
echo "Service $SERVICE_NAME exposé via ngrok sur le port $NODE_PORT"