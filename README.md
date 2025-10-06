# Liver Cancer RNA-seq Analysis

## Description
This project analyzes TCGA liver cancer RNA-seq data to identify differentially expressed genes and visualize results using PCA, heatmap, volcano plot, and 3D PCA.

## Folder Structure
- `data/`: Raw RNA-seq CSV file
- `scripts/`: Analysis and report scripts
- `results/`: Output figures, CSVs, and interactive 3D plot
- `README.md`: Project description
- `.gitignore`: Ignore unnecessary files

## Key Results
- Top 20 differentially expressed genes saved in `Top_20_Genes.csv`
- PCA plots show sample separation
- Heatmap visualizes gene expression patterns
- Volcano plot highlights significant genes
- 3D PCA interactive plot in `3D_PCA.html`

## Usage
1. Run `analysis.py` to generate plots and Top 20 genes CSV.
2. Run `create_report.py` to create a 1-page PDF report summarizing the findings.
