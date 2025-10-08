# Liver Cancer RNA-seq Analysis Pipeline

**Author:** Efe Can Orhan  
**Date:** 2025

---

## 🌟 Project Overview

This project presents a **comprehensive pipeline for liver cancer RNA-seq data analysis**. The pipeline integrates **data preprocessing, dimensionality reduction (PCA), differential gene expression analysis, visualization, and report generation** to provide reproducible insights into liver cancer transcriptomics. 

The workflow is designed for **bioinformatics research, educational purposes, and portfolio demonstration**, highlighting both computational and biological analysis skills.

---

## 🧬 Key Objectives

1. **Data Preprocessing**: Clean, normalize, and prepare liver RNA-seq data for analysis.
2. **Dimensionality Reduction (PCA)**: Perform both 2D and 3D PCA to explore sample clustering patterns.
3. **Differential Gene Expression (DGE)**: Identify top genes distinguishing cancerous vs normal samples using log2 fold-change and statistical testing.
4. **Visualization**:
   - Heatmaps for top differentially expressed genes.
   - Volcano plots to highlight significant gene changes.
   - Interactive 3D PCA visualization for sample exploration.
5. **Optional Clustering**: Group samples via k-means clustering to validate natural separation patterns.
6. **Automated Report Generation**: Produce a professional 1-page PDF summarizing the analysis and main results, with embedded figures.

---

## 🔹 Features

### 1. Data Loading & Cleaning
- Reads CSV files containing gene expression data.
- Checks for missing values and handles them by dropping or preprocessing.
- Prepares matrices of gene expression values and sample types for downstream analysis.

### 2. PCA Analysis
- **2D PCA**: Visualizes sample separation in two principal components.
- **3D PCA**: Interactive Plotly visualization allowing rotation, zooming, and color-coded sample types.
- Outputs both static PNGs and interactive HTML plots for presentations or portfolio use.

### 3. Differential Gene Expression
- Compares cancer vs normal samples using log2 fold change.
- Performs **t-tests** to assess statistical significance.
- Extracts **top 20 differentially expressed genes** and saves to CSV for further analysis.

### 4. Heatmaps & Volcano Plots
- **Heatmap**: Shows expression patterns of top 20 genes across all samples.
- **Volcano plot**: Visualizes log2 fold changes vs statistical significance (-log10 p-values) for all genes.

### 5. Clustering
- Optionally applies **k-means clustering** on scaled gene expression data.
- Validates sample separation and provides additional exploratory insight.

### 6. Automated PDF Report
- Generates a **professional 1-page summary** including:
  - Project overview and dataset summary
  - Analysis steps
  - Key results
  - Visualizations (PCA plot, heatmap, volcano plot)
  - Notes for portfolio or Devpost submission
- Uses `FPDF` and `Pillow` to embed images and format content.

---

## 📦 Dependencies

- Python ≥ 3.8
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- SciPy
- Plotly
- FPDF
- Pillow

Install dependencies via pip:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn scipy plotly fpdf pillow
