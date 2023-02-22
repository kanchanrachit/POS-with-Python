import os
import time

file_path = '/path/to/locked/file'

while True:
    if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
        with open(file_path, 'r') as f:
            # Read file contents here
            data = f.read()
        # Process data here
        print(data)
    else:
        time.sleep(1)  # Wait for 1 second before checking again
