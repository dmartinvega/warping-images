import torch


def get_fisheye(height, width, center, magnitude):
    xx, yy = torch.linspace(-1, 1, width), torch.linspace(-1, 1, height)
    gridy, gridx = torch.meshgrid(yy, xx)  # create identity grid
    grid = torch.stack([gridx, gridy], dim=-1)
    d = center - grid  # calculate the distance(cx - x, cy - y)
    d_sum = torch.sqrt((d ** 2).sum(axis=-1))  # sqrt((cx-x)**2 + (cy-y)**2)
    grid += d * d_sum.unsqueeze(-1) * magnitude  # calculate dx & dy and add to original values
    return grid.unsqueeze(0)  # unsqueeze(0) since the grid needs to be 4D.