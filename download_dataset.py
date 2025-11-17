import kagglehub

# Download latest version of the dataset
path = kagglehub.dataset_download("vivek603/vehicle-detection-sample-and-output-videos")

print("✅ Dataset downloaded successfully!")
print("📂 Path to dataset files:", path)
