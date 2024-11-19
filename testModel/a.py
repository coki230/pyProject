# from diffusers import StableDiffusionPipeline
# import torch
#
# model_id = "runwayml/stable-diffusion-v1-5"
# pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
# pipe = pipe.to("cuda")
#
# prompt = "a photo of an astronaut riding a horse on mars"
# image = pipe(prompt).images[0]
#
# image.save("astronaut_rides_horse.png")



import requests

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": "god like a duck",
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
image.show()