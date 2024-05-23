# pip install torchvision torch
from torchvision import models, transforms
from PIL import Image
import torch

# Load pre-trained ResNet model
resnet = models.resnet50(pretrained=True)
resnet.eval()

# Define transformation pipeline
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def generate_image_vector(image_path):
    image = Image.open(image_path)
    image = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        outputs = resnet(image)
    return outputs.numpy()

image_path = "path_to_image.jpg"
image_vector = generate_image_vector(image_path)
print(image_vector)
