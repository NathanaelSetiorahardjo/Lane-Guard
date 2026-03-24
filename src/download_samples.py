import os
import urllib.request

def download_sandbox_images():
    # Ensure the data directory exists
    save_dir = os.path.join("..", "data", "train")
    os.makedirs(save_dir, exist_ok=True)

    # A set of classic highway test images for classical CV pipelines
    base_url = "https://raw.githubusercontent.com/udacity/CarND-Advanced-Lane-Lines/master/test_images/"
    images = [
        "test1.jpg", "test2.jpg", "test3.jpg", 
        "test4.jpg", "test5.jpg", "test6.jpg"
    ]

    print(f"Downloading 6 test images into {save_dir}...")

    for img_name in images:
        url = base_url + img_name
        save_path = os.path.join(save_dir, img_name)
        
        try:
            urllib.request.urlretrieve(url, save_path)
            print(f"✅ Successfully downloaded: {img_name}")
        except Exception as e:
            print(f"❌ Failed to download {img_name}: {e}")

    print("\nSandbox dataset is ready!")

if __name__ == "__main__":
    # Note: Run this script from INSIDE the src/ folder
    download_sandbox_images()