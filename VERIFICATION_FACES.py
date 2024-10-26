from deepface import DeepFace
import cv2
from google.colab.patches import cv2_imshow
from datetime import datetime

# Known faces data
known_faces = {
    "22331A05D3": ["22331A05D3", "PATTEM SIVA NAGA HEMANTH"],
    "22331A05D4": ["22331A05D4", "PEDAPATI LASHYA SARANYA"],
    "22331A05F1": ["22331A05F1", "REVU ROHAN CHARAN DEEP"],
    "22331A05F2": ["22331A05F2", "RONGALI LALITHA"],
    "22331A05H2":["22331A05H2","TUTIKA BHASKAR SHASANK"],
    "22331A05H6": ["22331A05H6", "VADREVU SAI SANJANA"],
    "22331A05I8": ["22331A05I8", "KAYITHA HARSHINI"],
    "23335A0513": ["23335A0513", "PERAMBADURU PUJITHA"],
    "23335A0516": ["23335A0516", "TARINI RUPESWARI"],
    "23335A0518": ["23335A0518", "VANDRAPALLI ASWINI"],
}
# Load the unknown image
unknown_image = cv2.imread("captured_image.jpg")
if unknown_image is not None:
    cv2_imshow(unknown_image)
else:
    print("Error loading captured_image.jpg")

# Initialize lists for attendance
present_students = []
absent_students = []

# Iterate through known faces to find a match
match_found = False

for known_id, details in known_faces.items():
    known_image_path = f"{known_id}.jpg"
    known_image = cv2.imread(known_image_path)

    if known_image is None:
        print(f"Error loading {known_image_path}. Skipping...")
        continue

    try:
        result = DeepFace.verify(unknown_image, known_image)

        if result['verified']==True:
            current_date = datetime.now().date()
            present_students.append(details)
            print("Marked as present:", current_date)
            print(details)
            match_found = True
            break  # Stop checking after finding the first match
        else:
            absent_students.append(details)
    except Exception as e:
        print(f"Error verifying with {known_image_path}: {e}")

# If no match was found
if not match_found:
    print("No match found")
    print("Marked as absent:", absent_students)

# Optionally display the lists
print("\nSummary of Attendance:")
print("Present Students:", present_students)
print("Absent Students:", absent_students)
