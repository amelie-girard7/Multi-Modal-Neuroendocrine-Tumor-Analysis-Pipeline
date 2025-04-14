# utils.py
import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
import os

def overlay_mask_on_pet(pet_path, mask_path, output_img="overlay.png", slice_idx=None):
    pet = nib.load(pet_path).get_fdata()
    mask = nib.load(mask_path).get_fdata()

    if slice_idx is None:
        slice_idx = pet.shape[2] // 2

    plt.figure(figsize=(6, 6))
    plt.imshow(pet[:, :, slice_idx], cmap='gray')
    plt.contour(mask[:, :, slice_idx], colors='red', linewidths=1)
    plt.title(f"Slice {slice_idx}: PET with Tumor Mask")
    plt.axis('off')
    plt.savefig(output_img)
    plt.close()

def print_summary_report(report_text, summary_text):
    print("\n--- Original Report ---\n", report_text[:1000])
    print("\n--- Summary ---\n", summary_text)
