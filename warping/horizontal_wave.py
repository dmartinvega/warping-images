import torch


def get_horizontal_wave(height, width, freq, amplitude):
    xx, yy = torch.linspace(-1, 1, width), torch.linspace(-1, 1, height)
    gridy, gridx = torch.meshgrid(yy, xx)  # create identity grid
    grid = torch.stack([gridx, gridy], dim=-1)
    dy = amplitude * torch.cos(freq * grid[:, :, 0])  # calculate dy
    grid[:, :, 1] += dy
    return grid.unsqueeze(0)  # unsqueeze(0) since the grid needs to be 4D.
