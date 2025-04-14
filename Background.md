### ✅ 1. **Understand the Domain (PET + Neuroendocrine Tumors)**  

### **What is PET? (Positron Emission Tomography)**
- A **nuclear medicine imaging technique**.
- Detects **metabolic or biochemical activity** in tissues.
- Inject a **radiotracer** → emits positrons → detects gamma rays when positrons annihilate with electrons.
- Visualizes **functional** processes, not just structure (unlike CT/MRI).

---

### **PET Imaging in Neuroendocrine Tumors (NETs)**
- NETs often overexpress **somatostatin receptors (SSTRs)**.
- **Specialized tracers** bind to these receptors to highlight tumors.

#### Common Tracers:
| Tracer | Use | Notes |
|--------|-----|-------|
| **FDG (Fluorodeoxyglucose)** | High-grade, aggressive NETs | Glucose metabolism |
| **Ga-68 DOTATATE / DOTATOC** | Well-differentiated NETs | Binds to somatostatin receptors (high SSTR affinity) |
| **F-18 DOPA** | Some NETs (esp. pancreatic) | Dopamine precursor |

---

### **PET Data Characteristics**
- 3D volume (voxel grid): `(x, y, z)` + sometimes time or tracer decay
- Low resolution, noisy, often needs:
  - **Denoising**
  - **Co-registration** with CT/MRI
  - **Standardized uptake value (SUV)** calculation for quantification

---

### **Clinical & Research Goals**
- **Tumor detection/localization**
- **Tumor grading (via SUV max, uptake patterns)**
- **Response to treatment (compare pre/post scans)**
- **Prognostic modeling**

---

### **PET + AI/ML Research Applications**
- Tumor **segmentation**
- **Classification** of tumor aggressiveness
- Predicting **treatment response**
- **Radiomics**: Extract quantitative features (texture, shape, intensity) from images

---


### ✅ 2. **Research Alignment**  
My  PhD work (evaluation metrics, optimization, explainable AI) to show that:
- We can design **custom pipelines** for imaging tasks
- We can **critically evaluate model performance**
- WE bring a **novel perspective** (NLP x imaging crossover can be an asset)


> My work on evaluation metrics in NLP taught me how to design task-specific, interpretable models — which I believe transfers well to the imaging domain, especially for diagnostics and clinical decision support.

---

### ✅  3. **Technical Fit**  

| JD Skill                      | Your Resume                        |
|------------------------------|------------------------------------|
| Statistical analysis tools   | Python, R, MATLAB, statistical ML  |
| Imaging data analysis        | NLP → similar data pipelines       |
| Research output              | Multiple papers, research profile  |
| Mentoring                    | Teaching assistant, leadership     |
| Communication                | Cross-functional roles, teaching   |


### ✅ 4. **Mock recent Project**  

**S**: Worked on counterfactual story rewriting models using custom training objectives.  
**T**: Improve interpretability and evaluation beyond BLEU or ROUGE.  
**A**: Designed new reward functions; integrated policy gradients; compared against baselines on real datasets.  
**R**: Achieved significant improvement in human evaluation; work submitted to ACM and Springler journals.


> I can apply similar rigorous evaluation and modeling methods to PET scan analysis — for example, defining a better interpretability metric for tumor segmentation.

---

### ✅  5. **Questions for the interviewers**
- What PET tracers are you using for neuroendocrine tumor detection?
- How are you currently preprocessing and labeling the imaging data?
- Is the goal classification, segmentation, or anomaly detection?
- Is there a plan to deploy these models into clinical workflows?


---

## 🧠 Some other concepts

### **How does PET links to NLP?**


> PET is a functional imaging modality that visualizes metabolic activity using radiotracers. In cancer, it's used to detect tumor metabolism, monitor therapy, and assess progression. In neuroendocrine tumors, PET tracers like Ga-68 DOTATATE target somatostatin receptors for high sensitivity and specificity.

> While my background is NLP, I’ve worked on high-dimensional data with explainability needs. PET has parallels — such as noise handling, dimensionality reduction, and building models that clinicians can trust.

---

### **What’s unique about PET scans in neuroendocrine tumors?**


> Neuroendocrine tumors overexpress somatostatin receptors — so radiotracers like Ga-68 DOTATATE bind specifically to these, offering precise tumor localization. Unlike FDG-PET used in many cancers, DOTATATE is preferred for well-differentiated NETs.


> The ability to tailor tracer selection based on tumor grade introduces interesting modeling challenges, e.g., tracer-specific feature extraction or hybrid models with CT co-registration.

---

### **How would you preprocess PET scan data for ML?**

- **Denoise** (e.g. Gaussian smoothing)
- **Normalize** intensities (e.g. z-score, SUV scaling)
- **Co-register** to anatomical images (CT/MRI)
- **Resample** to consistent resolution
- **Segment** regions of interest (manual/auto/weak labels)
- **Extract features** (e.g. radiomics, voxel intensities)

> “I’d use NiBabel or SimpleITK for preprocessing, PyRadiomics for feature extraction, and integrate pipelines in Python using PyTorch or Scikit-Learn.”

---

### **What’s radiomics?**

> Radiomics involves extracting quantitative features — such as texture, shape, and intensity — from medical images. These features can be used to build predictive models for tumor type, response to therapy, or prognosis. It’s analogous to feature engineering in NLP, but for 3D/4D image data.

### ✅  6. **Resources**

##  Mini Reading List – PET + Neuroendocrine Tumors

### 🔹 Basics of PET Imaging
- [Introduction to PET](https://radiopaedia.org/articles/positron-emission-tomography) – Radiopaedia  
- [NIH: What is a PET Scan?](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/pet-scan) – NIH Glossary  
- [PET Imaging Physics Primer (PDF)](https://humanhealth.iaea.org/HHW/MedicalPhysics/NuclearMedicine/NuclearMedicineImaging/PET/index.html) – IAEA

### 🔹 Neuroendocrine Tumors
- [NET Overview – American Cancer Society](https://www.cancer.org/cancer/neuroendocrine-tumor/about/what-is-net.html)  
- [Role of PET in NETs – PubMed](https://pubmed.ncbi.nlm.nih.gov/29494896/) (Good for evidence-based discussion)

### 🔹 AI in Medical Imaging
- [Radiomics: Extracting more information from medical images](https://www.nature.com/articles/nrclinonc.2015.141) – Lambin et al. (2015)  
- [Deep Learning in PET Imaging](https://pubmed.ncbi.nlm.nih.gov/32741878/) – Review paper  
- [Ga-68 DOTATATE PET/CT for NET](https://pubmed.ncbi.nlm.nih.gov/26101092/) – Useful tracer-specific example


