# segmentation.py
import os
from subprocess import run

def run_nnunet_inference(pet_path, ct_path, output_path, model_dir):
    """
    Run nnU-Net segmentation using pretrained model.
    Assumes nnUNet is installed and model weights are in model_dir.
    """
    os.makedirs(output_path, exist_ok=True)
    
    command = [
        "nnUNet_predict",
        "-i", os.path.dirname(pet_path),
        "-o", output_path,
        "-t", "511",  # Task number (change if needed)
        "-m", "3d_fullres",
        "-f", "0",    # Fold
        "-chk", "model_final_checkpoint",
        "-tr", "nnUNetTrainerV2",
        "-p", "nnUNetPlansv2.1"
    ]
    
    run(command, check=True)
