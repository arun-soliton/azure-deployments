# azure-deployments

## Build and push to Azure Container Registry

1. Login to azure container registry

`az acr login --name <container registry name>`

2. Build the docker image

`docker build -t <app_name>:<tag> .`

3. Tag the docker image with the container name

`docker tag <app_name>:<tag> <acr_name>.azurecr.io/<app_name>:<tag>`

4. Push the docker image to registry

`docker push <acr_name>.azurecr.io/<app_name>:<tag>`
