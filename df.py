from diffusers import DiffusionPipeline
import torch

pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipeline.to("cuda")
task_str = input('Enter the phraze: ')
image = pipeline(task_str).images[0]
image.save("./output/df.png")
# "An image of a squirrel in Picasso style"