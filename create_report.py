# create_report.py
# Author: Efe Can Orhan
# Date: 2025
# Description: Generates a professional 1-page PDF report for Liver RNA-seq analysis.

from fpdf import FPDF
from PIL import Image

# ------------------------------
# PDF setup
# ------------------------------
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=10)

# ------------------------------
# Title
# ------------------------------
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Liver Cancer RNA-seq Analysis", ln=True, align='C')

pdf.ln(5)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 6,
    "This report summarizes the analysis of a liver cancer RNA-seq dataset "
    "(TCGA). The analysis includes PCA, differential gene expression, "
    "heatmap, volcano plot, and 3D PCA visualization."
)

pdf.ln(3)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 6, "Dataset Overview:", ln=True)
pdf.set_font("Arial", '', 11)
pdf.multi_cell(0, 5,
    "- Genes: 20,531\n"
    "- Samples: Cancer and Normal\n"
    "- sample_type_id: 0 = Normal, 1 = Cancer"
)

pdf.ln(2)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 6, "Analysis Steps:", ln=True)
pdf.set_font("Arial", '', 11)
pdf.multi_cell(0, 5,
    "1. PCA (2D and 3D) for sample distribution.\n"
    "2. Differential gene expression analysis (Top 20 genes) using log2 fold change and t-test.\n"
    "3. Heatmap of Top 20 genes.\n"
    "4. Volcano plot of all genes.\n"
    "5. Clustering (optional) for sample grouping."
)

pdf.ln(2)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 6, "Key Results:", ln=True)
pdf.set_font("Arial", '', 11)
pdf.multi_cell(0, 5,
    "- Top 20 genes identified and saved in 'Top_20_Genes.csv'.\n"
    "- PCA shows clear separation of cancer and normal samples.\n"
    "- Heatmap visualizes expression patterns of Top 20 genes.\n"
    "- Volcano plot highlights significantly differentially expressed genes.\n"
    "- 3D PCA interactive plot saved as '3D_PCA.html'."
)

pdf.ln(2)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 6, "Visualizations:", ln=True)

# ------------------------------
# Add images
# ------------------------------
def add_image(path, w=90):
    try:
        img = Image.open(path)
        pdf.image(path, w=w)
    except Exception as e:
        pdf.set_font("Arial", '', 10)
        pdf.cell(0, 5, "Could not load image {}: {}".format(path, e), ln=True)

pdf.ln(2)
add_image(r"C:\Users\PC\Desktop\Cancers\PCA_plot.png", w=90)
pdf.ln(1)
add_image(r"C:\Users\PC\Desktop\Cancers\Top20_Heatmap.png", w=90)
pdf.ln(5)

# ------------------------------
# Footer / Notes
# ------------------------------
pdf.set_font("Arial", 'I', 10)
pdf.multi_cell(0, 5,
    "Note: For full interactive visualization, open '3D_PCA.html'. "
    "This report summarizes the main findings for CV or Devpost use."
)

# ------------------------------
# Save PDF
# ------------------------------
output_path = r"C:\Users\PC\Desktop\Cancers\Liver_RNA_Report.pdf"
pdf.output(output_path)
print("Report saved as {}".format(output_path))
