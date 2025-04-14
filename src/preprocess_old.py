# preprocess.py
import nibabel as nib
import numpy as np
from scipy.ndimage import gaussian_filter

def load_nifti(path):
    """Load a NIfTI file and return image data and affine."""
    img = nib.load(path)
    return img.get_fdata(), img.affine

def save_nifti(data, affine, path):
    """Save a NumPy array as a NIfTI file."""
    img = nib.Nifti1Image(data, affine)
    nib.save(img, path)

def normalize(data):
    """Z-score normalization."""
    return (data - np.mean(data)) / np.std(data)

def denoise(data, sigma=1):
    """Apply Gaussian smoothing to reduce noise."""
    return gaussian_filter(data, sigma=sigma)

def preprocess_volume(path):
    """Complete load → normalize → denoise pipeline."""
    data, affine = load_nifti(path)
    norm = normalize(data)
    clean = denoise(norm)
    return clean, affine
