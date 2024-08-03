# Helm
-   Helm is a package manager for Kubernetes that simplifies the deployment of applications and services.
-   With Helm, you can create reusable packages (called Helm Charts) that describe even complex applications, making installation and updates straightforward.

# Helm Charts
-   Helm Charts are a collection of files that describe a related set of Kubernetes resources.
    -   **Chart.yaml:** Required metadata file containing info like name, version, and description.
    -   **values.yaml:** Default configuration values for the chart.
    -   **templates/:** Directory with templates for Kubernetes manifests.
    -   **charts/:** Optional directory for dependencies.
    -   **crds/:** Custom Resource Definitions (if needed).

# Creating Charts
-   `helm create <chart-name>`  --> Creats charts

# Install Helm Charts
-   `helm install <Release Name, User Defined> <Charts folder Name/path>`
-   `helm upgrade <Already Exist Release Name> <Charts folder Name/path>`
