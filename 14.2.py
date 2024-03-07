import numpy as np
from sklearn.preprocessing import PowerTransformer
from sklearn.cluster import KMeans
import warnings

# Suppress future warnings related to scikit-learn changes
warnings.simplefilter(action='ignore', category=FutureWarning)

# Generate example gene expression data
gene_expression_data = np.random.exponential(scale=1, size=(1000, 10))

# Perform data transformation
power_transformer = PowerTransformer(method='yeo-johnson', standardize=True)
gene_expression_transformed = power_transformer.fit_transform(gene_expression_data)

# Cluster original data
kmeans_original = KMeans(n_clusters=3, random_state=42, n_init=10)
labels_original = kmeans_original.fit_predict(gene_expression_data)

# Cluster transformed data
kmeans_transformed = KMeans(n_clusters=3, random_state=42, n_init=10)
labels_transformed = kmeans_transformed.fit_predict(gene_expression_transformed)

# Assess impact
print("Cluster Labels (Original):", labels_original)
print("Cluster Labels (Transformed):", labels_transformed)
