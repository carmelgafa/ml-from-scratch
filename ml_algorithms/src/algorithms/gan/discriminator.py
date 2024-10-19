

import torch
import torch.nn as nn


class Discriminator(nn.Module):
    
    def __init__(self):
        """
        Initialize the discriminator network.

        The network consists of three layers of fully connected (dense) layers.
        The output of the network is a probability that the input is real.
        """
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(784, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 1),
            nn.Sigmoid()  # Output a probability
        )

    def forward(self, img:torch.tensor) -> torch.tensor:
        """
        Forward pass of the discriminator network.

        Parameters
        ----------
        img : torch.tensor
            The input image to the discriminator network.

        Returns
        -------
        validity : torch.tensor
            The probability that the input image is real.
        """
        img_flat = img.view(img.size(0), -1)  # Flatten the image
        validity = self.model(img_flat)
        return validity
