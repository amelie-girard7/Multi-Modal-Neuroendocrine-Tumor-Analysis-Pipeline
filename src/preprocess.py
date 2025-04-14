# preprocess.py

import nibabel as nib
import numpy as np
from scipy.ndimage import gaussian_filter
import os

def load_nifti(path):
    """Load a NIfTI file and return the image data and affine matrix."""
    img = nib.load(path)
    return img.get_fdata(), img.affine

def save_nifti(data, affine, path):
    """Save a NumPy array as a NIfTI file."""
    img = nib.Nifti1Image(data, affine)
    nib.save(img, path)

def normalize(data):
    """Z-score normalization: (x - mean) / std."""
    return (data - np.mean(data)) / np.std(data)

def denoise(data, sigma=1):
    """Apply Gaussian smoothing to reduce noise."""
    return gaussian_filter(data, sigma=sigma)

def preprocess_volume(path):
    """
    Complete pipeline: load → normalize → denoise.
    Returns processed data and affine.
    """
    print(f"Loading image: {path}")
    data, affine = load_nifti(path)

    print("Normalizing image...")
    norm_data = normalize(data)

    print("Denoising image with Gaussian filter...")
    clean_data = denoise(norm_data, sigma=1)

    return clean_data, affine


# This allows the script to be run standalone
if __name__ == "__main__":
    # Define input and output paths
    input_path = "/data/agirard/Projects/Multi-Modal-Neuroendocrine-Tumor-Analysis-Pipeline/data/dummy_pet.nii.gz"
    output_path = "/data/agirard/Projects/Multi-Modal-Neuroendocrine-Tumor-Analysis-Pipeline/data/dummy_pet_preprocessed.nii.gz"

    print("=== Starting PET preprocessing ===")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    processed_data, affine = preprocess_volume(input_path)

    print(f"Saving preprocessed image to: {output_path}")
    save_nifti(processed_data, affine, output_path)

    print("✅ Done. Preprocessed PET saved.")
