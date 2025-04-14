# download_mskcc_model.py

import os
import requests
import zipfile
from tqdm import tqdm

def download_file(url, dest_path):
    """Download a file from a URL with a progress bar."""
    response = requests.get(url, stream=True)
    total = int(response.headers.get('content-length', 0))
    with open(dest_path, 'wb') as file, tqdm(
        desc=dest_path,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

def extract_zip(zip_path, extract_to):
    """Extract a zip file to a specified directory."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

if __name__ == "__main__":
    # Define the URL and destination paths
    url = "https://zenodo.org/record/7843469/files/Task511_PETCT_pretrained.zip"
    zip_path = "/data/agirard/Projects/Multi-Modal-Neuroendocrine-Tumor-Analysis-Pipeline/models/Task511_PETCT_pretrained.zip"
    extract_to = "/data/agirard/Projects/Multi-Modal-Neuroendocrine-Tumor-Analysis-Pipeline/models/Task511_PETCT"

    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(zip_path), exist_ok=True)

    # Download the zip file
    print("Downloading the pretrained model...")
    download_file(url, zip_path)

    # Extract the zip file
    print("Extracting the model files...")
    extract_zip(zip_path, extract_to)

    print(f"✅ Model downloaded and extracted to: {extract_to}")
