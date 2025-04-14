# radiomics_features.py
from radiomics import featureextractor
import SimpleITK as sitk

# Initialize once
extractor = featureextractor.RadiomicsFeatureExtractor()

def extract_features(image_path, mask_path):
    """
    Extract radiomic features from PET image using mask.
    Returns a dict of feature names and values.
    """
    img = sitk.ReadImage(image_path)
    mask = sitk.ReadImage(mask_path)
    features = extractor.execute(img, mask)
    
    # Filter out metadata
    return {k: v for k, v in features.items() if "diagnostics" not in k}
