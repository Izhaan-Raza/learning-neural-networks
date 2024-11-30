import torch
from torch.utils.data import Dataset, DataLoader

class MyDataset(Dataset):
    def __init__(self):
        self.data = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
        self.labels = torch.tensor([0, 1, 0])
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__ (self, idx):
        return self.data[idx], self.labels[idx]

dataset = MyDataset()
dataloader =  DataLoader(dataset, batch_size=3, shuffle=True)

for batch in dataloader:
    print("Batch Data: ", batch[0])
    print("Batch Labels:", batch[0])