import PyPDF2                            # First Install PyPDF2 (pip install PyPDF2)
import sys
import os

# First Define the folder containing PDF files
input_folder = "D:/vs code/pdf"  # Location of the folder or the file
output_path = "merged_output.pdf"  # Define the output merged PDF file name

# Now, Initialize the PdfMerger
merger = PyPDF2.PdfMerger()

# Now Loop through all PDF files in the folder and add all them to the merger
for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        file_path = os.path.join(input_folder, filename)
        merger.append(file_path)
        print(f"Added {filename} to the merge list.")

# Write the merged PDF to the output path
merger.write(output_path)
print("All PDF files are merged successfully!")