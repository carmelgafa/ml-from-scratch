import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.datasets as datasets
from torch.utils.data import DataLoader
from torchvision import transforms
import torchvision
import matplotlib.pyplot as plt

from generator import Generator
from discriminator import Discriminator

# Hyperparameters
latent_dim = 100
lr = 0.0002
batch_size = 64
epochs = 200

# Device configuration (GPU if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])  # Normalize images to [-1, 1]
])

train_data = datasets.MNIST(root="./data", train=True, transform=transform, download=True)
train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)


generator = Generator(latent_dim).to(device)
discriminator = Discriminator().to(device)

optimizer_G = optim.Adam(generator.parameters(), lr=lr)
optimizer_D = optim.Adam(discriminator.parameters(), lr=lr)

criterion = nn.BCELoss()  # Binary Cross Entropy Loss

generator = Generator(latent_dim).to(device)
discriminator = Discriminator().to(device)

optimizer_G = optim.Adam(generator.parameters(), lr=lr)
optimizer_D = optim.Adam(discriminator.parameters(), lr=lr)

criterion = nn.BCELoss()  # Binary Cross Entropy Loss

for epoch in range(epochs):
    for i, (imgs, _) in enumerate(train_loader):
        
        # Ground truths
        real = torch.ones(imgs.size(0), 1).to(device)
        fake = torch.zeros(imgs.size(0), 1).to(device)

        # ---------------------
        #  Train Discriminator
        # ---------------------

        optimizer_D.zero_grad()

        # Real images
        real_imgs = imgs.to(device)
        real_loss = criterion(discriminator(real_imgs), real)

        # Fake images
        z = torch.randn(imgs.size(0), latent_dim).to(device)
        fake_imgs = generator(z)
        fake_loss = criterion(discriminator(fake_imgs), fake)

        # Total loss for discriminator
        d_loss = real_loss + fake_loss
        d_loss.backward()
        optimizer_D.step()

        # -----------------
        #  Train Generator
        # -----------------

        optimizer_G.zero_grad()

        # Generate fake images
        z = torch.randn(imgs.size(0), latent_dim).to(device)
        fake_imgs = generator(z)

        # The generator wants the discriminator to think these images are real
        g_loss = criterion(discriminator(fake_imgs), real)

        g_loss.backward()
        optimizer_G.step()

        # Print progress
        if i % 200 == 0:
            print(f"Epoch [{epoch}/{epochs}] Batch {i}/{len(train_loader)} \
                  Loss D: {d_loss.item():.4f}, loss G: {g_loss.item():.4f}")

    # Save generated samples for visualization every few epochs
    if epoch % 10 == 0:
        with torch.no_grad():
            z = torch.randn(16, latent_dim).to(device)
            generated_imgs = generator(z).cpu().view(-1, 1, 28, 28)
            grid_img = torchvision.utils.make_grid(generated_imgs, nrow=4, normalize=True)
            plt.imshow(grid_img.permute(1, 2, 0))
            plt.show()
