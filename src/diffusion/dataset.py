from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
import os

class PairedGrayscaleDataset(Dataset):
    def __init__(self, root_dir, transforms=None):
        self.root = root_dir
        self.transforms = transforms or transforms.Compose([
            transforms.Resize(512),
            transforms.CenterCrop(512),
            transforms.ToTensor(),              # [0,1]
            transforms.Normalize(0.5, 0.5),     # [–1,1]
        ])
        # assume structure root/noisy/*.png and root/cond/*.png
        self.noisy_paths = sorted(os.listdir(os.path.join(root_dir, "noisy")))
        self.cond_paths  = sorted(os.listdir(os.path.join(root_dir, "cond")))

    def __len__(self):
        return len(self.noisy_paths)

    def __getitem__(self, idx):
        noisy = Image.open(os.path.join(self.root, "noisy", self.noisy_paths[idx])).convert("L")
        cond  = Image.open(os.path.join(self.root, "cond",  self.cond_paths[idx])).convert("L")
        noisy = self.transforms(noisy)
        cond  = self.transforms(cond)
        return noisy, cond
