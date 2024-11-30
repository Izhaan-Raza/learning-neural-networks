import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(2,4)
        self.fc2 = nn.Linear(4,1)
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

x_train = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]) # inputs
y_train = torch.tensor([[0.0], [1.0], [1.0], [0.0]]) # corresponding ooutput XOR

model = SimpleNN()
criterion = nn.MSELoss() # Mean Squared Error for regression
optimizer = optim.SGD(model.parameters(), lr =0.1)

for epoch in range(100):
    model.train()

    outputs = model(x_train)
    loss = criterion(outputs, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch + 1}/100], Loss: {loss.item():.4f}')

model.eval()
with torch.no_grad():
    test_data = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
    predictions = model(test_data)
    print(f'Predictions:\n{predictions}')