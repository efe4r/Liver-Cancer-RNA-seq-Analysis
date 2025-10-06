# Liver RNA-seq Enhanced Analysis
# Author: Efe Can Orhan
# Date: 2025
# Description: Full pipeline for liver cancer RNA-seq dataset analysis,
# including PCA, differential gene expression, heatmap, volcano plot, and 3D PCA visualization.

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
import plotly.express as px

# ------------------------------
# 1. Load the dataset
# ------------------------------
file_path = r"C:\Users\PC\Desktop\Cancers\Liver RNA Data.csv"
data = pd.read_csv(file_path)

# View first rows and check missing values
print("First 5 rows:")
print(data.head())
print("\nMissing values:")
print(data.isnull().sum())

# ------------------------------
# 2. Data preprocessing
# ------------------------------
data_clean = data.dropna()
gene_names = data_clean.iloc[:, 0]
expression_data = data_clean.iloc[:, 1:-1]  # last column sample_type_id
sample_type = data_clean.iloc[:, -1]

# ------------------------------
# 3. PCA (2D)
# ------------------------------
x_scaled = StandardScaler().fit_transform(expression_data)
pca = PCA(n_components=2)
pca_result = pca.fit_transform(x_scaled)
pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'])
pca_df['sample_type'] = sample_type

# 2D PCA plot
plt.figure(figsize=(8,6))
sns.scatterplot(x='PC1', y='PC2', hue='sample_type', data=pca_df)
plt.title("2D PCA of Liver RNA-seq Samples")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.tight_layout()
plt.savefig(r"C:\Users\PC\Desktop\Cancers\PCA_plot.png")
plt.show()

# ------------------------------
# 4. Differential Gene Expression (Top 20 Genes)
# ------------------------------
# Assume first half samples are cancer, second half normal
num_samples = expression_data.shape[1]
half = num_samples // 2
cancer_samples = expression_data.iloc[:, :half]
normal_samples = expression_data.iloc[:, half:]

# log2 Fold Change
data_clean['mean_cancer'] = cancer_samples.mean(axis=1)
data_clean['mean_normal'] = normal_samples.mean(axis=1)
data_clean['log2FC'] = np.log2(data_clean['mean_cancer'] + 1) - np.log2(data_clean['mean_normal'] + 1)

# t-test for p-value
p_values = []
for i in range(expression_data.shape[0]):
    t_stat, p_val = ttest_ind(cancer_samples.iloc[i, :], normal_samples.iloc[i, :])
    p_values.append(p_val)
data_clean['p_value'] = p_values

# Top 20 genes by absolute log2FC
top_genes = data_clean.assign(abs_log2FC = data_clean['log2FC'].abs())
top_genes_sorted = top_genes.sort_values('abs_log2FC', ascending=False).head(20)
top_genes_sorted.to_csv(r"C:\Users\PC\Desktop\Cancers\Top_20_Genes.csv", index=False)
print("Top 20 genes saved as 'Top_20_Genes.csv'")

# ------------------------------
# 5. Heatmap of Top 20 Genes
# ------------------------------
top20_genes_df = expression_data.loc[top_genes_sorted.index, :]
plt.figure(figsize=(10,8))
sns.heatmap(top20_genes_df, cmap='viridis', annot=False)
plt.title("Heatmap of Top 20 Differentially Expressed Genes")
plt.xlabel("Samples")
plt.ylabel("Top Genes")
plt.tight_layout()
plt.savefig(r"C:\Users\PC\Desktop\Cancers\Top20_Heatmap.png")
plt.show()

# ------------------------------
# 6. Volcano Plot
# ------------------------------
plt.figure(figsize=(8,6))
plt.scatter(data_clean['log2FC'], -np.log10(data_clean['p_value']), alpha=0.5)
plt.xlabel("log2 Fold Change")
plt.ylabel("-log10(p-value)")
plt.title("Volcano Plot of Gene Expression")
plt.axvline(0, color='grey', linestyle='--')
plt.tight_layout()
plt.savefig(r"C:\Users\PC\Desktop\Cancers\Volcano_plot.png")
plt.show()

# ------------------------------
# 7. 3D PCA Plot (Interactive)
# ------------------------------
pca_3 = PCA(n_components=3)
pca_result_3 = pca_3.fit_transform(x_scaled)
pca_df_3 = pd.DataFrame(data=pca_result_3, columns=['PC1', 'PC2', 'PC3'])
pca_df_3['sample_type'] = sample_type

fig = px.scatter_3d(pca_df_3, x='PC1', y='PC2', z='PC3',
                    color='sample_type',
                    title="3D PCA of Liver RNA-seq Samples")
fig.write_html(r"C:\Users\PC\Desktop\Cancers\3D_PCA.html")
fig.show()

# ------------------------------
# 8. Clustering (Optional)
# ------------------------------
kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(x_scaled)
pca_df['cluster'] = clusters
