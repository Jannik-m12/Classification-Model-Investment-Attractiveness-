
import pandas as pd
import hashlib
import os
import requests # Import requests for downloading

def download_data(url, output_path):
    """
    Downloads data from a given URL to a specified output path.
    """
    print(f"Attempting to download data from {url} to {output_path}")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status() # Raise an exception for bad status codes
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded data successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading data: {e}")
        # Handle specific errors like connection issues, timeouts, etc.
    except Exception as e:
        print(f"An unexpected error occurred during download: {e}")


def generate_checksum(file_path):
    """Generates an MD5 checksum for a given file."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

if __name__ == "__main__":
    # Define the URL for the dataset
    dataset_url = "https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy/download?datasetVersionNumber=1" # Example download URL format (may need adjustment based on Kaggle API/direct link)
    # Note: Direct download links from Kaggle often require authentication or specific API usage.
    # This URL is illustrative and might need to be replaced with a method using the Kaggle API
    # or assuming the dataset is manually placed in the Colab environment.

    # Define the path where the dataset should be saved
    dataset_path = 'data/global-data-on-sustainable-energy.csv'
    checksum_output_path = 'data/global-data-on-sustainable-energy.csv.md5' # Define checksum file path

    # Ensure the data directory exists
    os.makedirs(os.path.dirname(dataset_path) or '.', exist_ok=True)


    # Attempt to download the data (this part might need adjustment for actual Kaggle download)
    # For this notebook's context, the file is likely already in /content/
    # We'll update the script to reflect a potential real-world download location
    # and assume the file might need to be copied or accessed from /content if download fails.

    # In a real script, you would call download_data here first
    # download_data(dataset_url, dataset_path)

    # For this notebook, let's check if the file exists at the expected /content path
    # and generate checksum from there, or provide a placeholder message.
    colab_dataset_path = '/content/global-data-on-sustainable-energy.csv'

    if os.path.exists(colab_dataset_path):
        print(f"Dataset found at {colab_dataset_path}. Generating checksum.")
        file_to_checksum = colab_dataset_path
    elif os.path.exists(dataset_path):
         print(f"Dataset found at {dataset_path}. Generating checksum.")
         file_to_checksum = dataset_path
    else:
        print(f"Dataset not found at {colab_dataset_path} or {dataset_path}. Cannot generate checksum.")
        file_to_checksum = None


    if file_to_checksum:
        # Generate checksum
        checksum = generate_checksum(file_to_checksum)

        if checksum:
            print(f"Generated MD5 checksum: {checksum}")

            # Ensure the output directory for checksum exists
            os.makedirs(os.path.dirname(checksum_output_path) or '.', exist_ok=True)

            # Save checksum to a file
            with open(checksum_output_path, 'w') as f:
                f.write(checksum)
            print(f"Checksum saved to {checksum_output_path}")
    else:
        print("Checksum generation skipped due to missing dataset.")

