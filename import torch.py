import torch
print(torch.__version__)
print(torch.cuda.is_available())  # Should return True if GPU is set up, False for CPU