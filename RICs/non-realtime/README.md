# Non RealTime RIC

## Installation

### Docker and kubernetes (skip if already installed)

We installed the non rt ric using kubernetes and containers, to do so we used [kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/) and [containerd](https://containerd.io/).

We've started with a machine running Ubuntu Desktop 22.04 LTS and installed docker following [their own documentation](https://docs.docker.com/engine/install/ubuntu/). 

For our cgroup driver we chose systemd. Our configuration file can be found [here](./config.yaml). Make sure to install kubectl as well. As our pod network add-on, we picked [flannel](https://github.com/flannel-io/flannel). Finally we removed the `node-role.kubernetes.io/control-plane:NoSchedule` taint from all nodes.

Now we should have a healthy kubernetes cluster running so its time to deploy the NearRTRIC itself.


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