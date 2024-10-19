import torch
import torch.nn as nn


class Generator(nn.Module):
    def __init__(self, latent_dim):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 128),
            nn.LeakyReLU(0.2),
            nn.Linear(128, 256),
            nn.BatchNorm1d(256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 784),  # 28x28=784
            nn.Tanh()  # Normalize the output to [-1, 1]
        )

    def forward(self, z:torch.tensor) -> torch.tensor:
        """
        Forward pass of the generator network.

        Parameters
        ----------
        z : torch.tensor
            The input latent vector to the generator network.

        Returns
        -------
        img : torch.tensor
            The generated image, reshaped to 28x28 for MNIST.
        """
        img = self.model(z)
        img = img.view(img.size(0), 1, 28, 28)  # Reshape to 28x28 for MNIST
        return img
