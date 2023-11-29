# Photo generator #
Ubuntu-22.04 nvidia/cuda-12.1.0
[Diffusers](https://huggingface.co/diffusers) [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
## Dockerhub ##
```bash
docker run -it --gpus all -v=./output:/output --rm tyurina0410/dreamfusion
```
You'll be asked for a phrase upon which the image will be generated.
Generated image will appear in the __./output__ folder with name __df.png__.


## Local machine ##
Repo cloning
```bash
git clone https://github.com/Gerasim0410/DLS.git DLS
cd DLS
```
For proper work of GPU
```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) && \
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - && \
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update
sudo apt-get install -y nvidia-docker2
sudo systemctl restart docker
```
Building and running of the project 
```bash
docker build --tag=tyurina0410/dreamfusion .
docker run -it --gpus all -v=./output:/output --rm tyurina0410/dreamfusion
```
