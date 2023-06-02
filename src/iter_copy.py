import os
import glob
import shutil

# Get the source directory
source_directory = "./"

# Get the destination directory
destination_directory = "/tmp/dog"

# Get all files in the source directory
files = glob.glob(os.path.join(source_directory, "**/*"))

# Iterate over all files
for file in files:

    # Check if the file is a regular file
    if os.path.isfile(file):

        # Copy the file to the destination directory
        shutil.copyfile(file, os.path.join(destination_directory, os.path.basename(file)))


