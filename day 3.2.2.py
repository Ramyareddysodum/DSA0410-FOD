import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PowerTransformer
from sklearn.cluster import KMeans
from scipy.stats import ttest_ind
import warnings

# Suppress future warnings related to scikit-learn changes
warnings.simplefilter(action='ignore', category=FutureWarning)

# Load the dataset
dataset_path = "C:/Users/ADMIN/Downloads/car.csv"
car_data = pd.read_csv(dataset_path)

# Identify non-numeric columns (assuming categorical columns)
non_numeric_cols = car_data.select_dtypes(include=['object']).columns.tolist()

# Exclude non-numeric columns from the dataset
numeric_car_data = car_data.drop(columns=non_numeric_cols)

# Split data into training and testing sets
X_train, X_test = train_test_split(numeric_car_data, test_size=0.2, random_state=42)

# Apply data transformation (e.g., PowerTransformer)
power_transformer = PowerTransformer(method='yeo-johnson', standardize=True)
X_train_transformed = power_transformer.fit_transform(X_train)
X_test_transformed = power_transformer.transform(X_test)

# Perform downstream analysis: Clustering
kmeans_original = KMeans(n_clusters=3, random_state=42, n_init=10)
labels_original = kmeans_original.fit_predict(X_train_transformed)

# Perform differential expression analysis (assuming you are comparing two columns)
t_stat_original, p_value_original = ttest_ind(X_train_transformed[:, 0], X_train_transformed[:, 1])

t_stat_transformed, p_value_transformed = ttest_ind(X_train_transformed[:, 0], X_train_transformed[:, 1])# Assess impact
# Evaluate clustering labels and differential expression results for original data
# Evaluate other relevant metrics based on your specific analysis objectives
print(labels_original)
print(car_data.head(5))
