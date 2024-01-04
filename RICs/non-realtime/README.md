# Non RealTime RIC

## Installation

### Docker and kubernetes (skip if already installed)

We installed the non rt ric using kubernetes and docker, to do so we used [minikube](https://minikube.sigs.k8s.io/docs/).

We've started with a machine running Ubuntu Desktop 22.04 LTS and installed docker following [their own documentation](https://docs.docker.com/engine/install/ubuntu/). 

Then we installed minikube using this:
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

Then we started our cluster using `sudo minikube start --driver=docker --force`. This will start our cluster.

Once the cluster is up we can install kubectl using `sudo minikube kubectl` and now to use kubectl commands all we have to do is type: `sudo minikube kubectl -- <command>`

<!--
missing details:
- clone it/dep repo
- run the chartsmuseum with `./dep/smo-install/scripts/layer-0/0-setup-charts-museum.sh`
- change all references of `kubectl` in `bin/deploy-nonrtric` for `minikube kubectl --`
- modify the recipe so it doesnt deploy the a1 simulator
- run `bin/deploy-nonrtric`
- profit
- undeploy by modifing `bin/undeploy-nonrtric` to use `minikube kubectl --` instead of `kubectl`
-->