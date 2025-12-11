import time
import torch

print("Tensor:")
start = time.time()
tensor = torch.tensor([[1., 2.],
                       [3., 4.]])
stop = time.time()
print(f"Tensor: {tensor * 3} {stop-start} segundos.")

print("-"*20)

print("Autograd:")
x = torch.tensor(5.0, requires_grad=True)
print(f"x: {x}, type: {type(x)}")
y = x**2
print(f"y: {y}")
print(f"y.backward(): {y.backward()}")
grand = x.grad
print(f"grand: {grand}")