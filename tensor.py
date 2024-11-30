import torch
import numpy as np

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

print(device)

tensor_size = (10000,10000)
a = torch.randn(tensor_size, device=device)
b = torch.randn(tensor_size, device=device)

c = torch.matmul(a,b.T)

print("Result shape (moved to CPU for printing):", c.cpu().shape)


print("Current GPU memory usage:")
print(f"Allocated: {torch.cuda.memory_allocated(device) / (1024 ** 2):.2f} MB")
print(f"Cached: {torch.cuda.memory_reserved(device) / (1024 ** 2):.2f} MB")
# print(f"cpu: {torch.cpu.memory_allocated(device)/(1024**2):.2f} MB")
print(c)