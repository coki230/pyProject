import onnx
from torchvision.io import decode_image
from torchvision.models import  EfficientNet_B2_Weights
from torchvision import models
import torch
from PIL import Image
import onnxruntime
import numpy as np

def parse_img(img):
    img = decode_image(img).unsqueeze(0)
    weighets = EfficientNet_B2_Weights.DEFAULT
    process = weighets.transforms()
    img = process(img)
    model = models.efficientnet_b2(weights=weighets)
    model.eval()
    result = model(img).squeeze(0).softmax(0)
    id = result.squeeze(0).argmax().item()
    category_name = weighets.meta["categories"][id]
    return str(category_name)


def save_model():
    weighets = EfficientNet_B2_Weights.DEFAULT
    model = models.efficientnet_b2(weights=weighets)
    model.eval()
    torch.onnx.export(model,                                # model being run
                  torch.randn(1, 3, 288, 288).to("cpu"),    # model input (or a tuple for multiple inputs)
                  "EfficientNet_B2.onnx",           # where to save the model (can be a file or file-like object)
                  input_names = ['input'],              # the model's input names
                  output_names = ['output'])            # the model's output names

def check_model():
    # model = onnx.load("EfficientNet_B2.onnx")
    # onnx.checker.check_model(model)
    model = onnxruntime.InferenceSession("EfficientNet_B2.onnx")
    img = Image.open("hua2.jpg").convert("RGB")
    img = img.resize((288, 288))
    img = np.array(img)
    img = np.transpose(img, (2, 0, 1)) / 255
    img = np.expand_dims(img, 0).astype(np.float32)
    result = model.run(None, {"input": img})
    print(np.argmax(result))

check_model()