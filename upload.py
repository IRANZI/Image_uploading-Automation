import os
import time
import shutil
import subprocess

# Paths
source_folder = "C:/Users/user/Pictures/Camera Roll/Blender images"  
uploaded_folder = "C:/Users/user/Desktop/Images-uploaded"  
upload_url = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"


os.makedirs(uploaded_folder, exist_ok=True)


print("Monitoring folder for new images...")
while True:
    
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    for file in files:
        file_path = os.path.join(source_folder, file)

       
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            print(f"Found image: {file}")

            # Waiting  for 30 seconds before uploading
            time.sleep(30)

            # Uploading the file using curl command
            try:
                print(f"Uploading {file}...")
                result = subprocess.run(
                    ["curl", "-X", "POST", "-F", f"imageFile=@{file_path}", upload_url],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    print(f"Successfully uploaded {file}. Moving it to the 'uploaded' folder...")
                    shutil.move(file_path, os.path.join(uploaded_folder, file))
                else:
                    print(f"Failed to upload {file}. Error: {result.stderr}")

            except Exception as e:
                print(f"Error while uploading {file}: {e}")

    
    time.sleep(10)
