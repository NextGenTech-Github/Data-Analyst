# Approach
# 1. Import Libraries
# 2. Create Data
# 3. Define the Neural Network
# 4. Initialize the Model, Loss Function, and Optimizer
# 5. Training the Model
# 6. Prediction
# 

# 1 First, import the necessary PyTorch libraries.
import torch
import torch.nn as nn
import torch.optim as optim

# 2. Create Data
# For simplicity, let's create some synthetic data using torch.rand for features and torch.randint for labels.
# Features
x = torch.rand(100, 10)
# Labels (0 or 1)
y = torch.randint(0, 2, (100,))


# 3. Define the Neural Network
class BinaryClassifier(nn.Module):
    def __init__(self):
        super(BinaryClassifier, self).__init__()
        self.layer1 = nn.Linear(10, 5)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(5, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.sigmoid(x)
        return x


# 4. Initialize the Model, Loss Function, and Optimizer

model = BinaryClassifier()
criterion = nn.BCELoss()
optimizer = optim.SGD(model.parameters(), lr=0.09)

# 5. Training the Model
for epoch in range(150):  # number of epochs
    model.train()
    optimizer.zero_grad()  # zero the parameter gradients
    outputs = model(x)
    loss = criterion(outputs.squeeze(), y.float())
    loss.backward()
    optimizer.step()

    print(f'Epoch {epoch+1}, Loss: {loss.item()}')


# 6. Prediction

model.eval()  # set the model to evaluation mode
with torch.no_grad():
    predictions = model(x)
    predicted_classes = predictions.round()  # Threshold the predictions
    accuracy = (predicted_classes.squeeze() == y).float().mean()
    print(f'Accuracy: {accuracy.item()}')

