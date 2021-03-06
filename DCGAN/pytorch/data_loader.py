# -*- coding: utf-8 -*-
"""data_loader.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xWF026DGmTJpq5z8DzDzOZEhmvB3DQij
"""

from torch.utils.data import DataLoader
from torchvision import datasets, transforms

class MnistDataLoader(DataLoader):
  def __init__(self, data_dir, batch_size, shuffle=True,num_workers=1):
    self.transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,),(0.5,)),
        transforms.Resize(64)
    ])
    self.data_dir = data_dir
    self.dataset = datasets.MNIST(self.data_dir, download=True, transform=self.transform)
    super().__init__(self.dataset, batch_size=batch_size, shuffle=shuffle,num_workers=num_workers)