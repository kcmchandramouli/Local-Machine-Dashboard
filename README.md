# Local-Machine-Dashboard

This repo is for setting up the K8s cluster & Grafana Dashboard for Local Machine

-   Starting this project with basic knowledge on K8s, Promethius & Grafana.
-   Using Minikube in the local machine for setting up the cluster in local machine.
-   Plan is to use python for gettig live metrics of system usage.

## Steps to setup Prometheus & Geafana
-   Reference
    -   [iam-veeramalla](https://github.com/iam-veeramalla/prometheus-Grafana-Zero-to-Hero) 
    -   [DinmaMerciBoi](https://www.youtube.com/watch?v=TyBsKMTDl1Q&t=820s)
-   Install Minikube, Kubectl, Helm in the local machine. (For windows use WSL as helm does't support in windows x86_64)
-   Install prometheus with the following commands using helm
    -   `helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
    -   `helm repo update`
    -   `helm install prometheus prometheus-community/prometheus`

## Process of setting up the dashboard with dataplain(kubectl) with yml files
-   Exposing Service using
    -   **Using NodePort:**
        -    exposes the service on a specific port on each Node in the cluster.
        -   The NodePort range is typically between 30000 and 32767.
        -   You can access the service using `<NodeIP>:<NodePort>`
        -   Limited Scalability: Less suitable for production environments with multiple nodes and high traffic.
    -   **Using LoadBalancer:**
        -   exposes the service externally using a cloud provider's load balancer
        -   Automatically provisions an external IP address that routes traffic to the service.
        -   Cloud Dependency: Requires a supported cloud provider, not suitable for local or on-premises setups without external load balancers.

-   Create a NameSpace(namespace.yml)
    -   Namespaces provide organization, security, and resource management in Kubernetes. 
    -   They allow you to create logical boundaries within a cluster b/w multiple users, teams & applications, making it easier to manage and scale your applications.

-   Create a ConfigMap(configmap.yml)
    -    For managing configuration data in Kubernetes, enhancing scalability, security, and maintainability.

-   Create a Deployment for prometheus(deployment.yml)
    -   For enabling declarative updated to the application.

-   Create a Service(service.yml)
    -   Provides a stable endpoint with IP address & port for access. (Simply used for exposing the service so that the user can access it from the browser.)

-   After creating the service we can access the application uding any node ip address & exposed service port number
    -   kubectl get services -n monitoring  --> Get the port number
    -   kubectl get nodes -o wide   --> Get node IP address

-   Create a Grafana Deployment(grafana-deployment.yaml)
-   Create a Grafana Service

-   Config Grafana Data Source with Promotheus(grafana-datasource.yaml)
-   Import Grafana Dashboard(grafana-dashboard-configmap.yaml)


# Note: 
-   At the moment we need to apply every yml file & then only we can setup the dashboard.