# Kubernetes Setup
So after you are on your cluster and have kubectl in the proper context you can update the `k8s_secret_example.yml` to be your own `k8s_secrets.yml` with the info you want and ensure this doesn't go into version control.

You can then apply these secrets to the cluster via:

`kubectl apply -f k8s_secrets.yml`

Then you can deploy the pod setup via:

`kubectl apply -f k8s_manifest.yml`