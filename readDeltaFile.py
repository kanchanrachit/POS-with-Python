from google.cloud import pubsub_v1

import shutil
import time
import os

# Create a Pub/Sub client
client = pubsub_v1.PublisherClient()

# Get a reference to the topic you want to publish to
topic = client.topic('projects/pos-dev-288217/topics/TLOGTopic')

# Set the paths of the two files
file1_path = 'file1.txt'
file2_path = 'file2.txt'

# Copy file 1 into file 2 initially
shutil.copy(file1_path, file2_path)

while True:
    # Wait for 1 minute
    time.sleep(10)

    # Get the size of file 2 before copying
    file2_size_before_copy = os.path.getsize(file2_path)

    # Copy file 1 into file 2
    shutil.copy(file1_path, file2_path)

    # Get the size of file 2 after copying
    file2_size_after_copy = os.path.getsize(file2_path)

    # Read the delta from file 2
    with open(file2_path, 'rb') as file2:
        file2.seek(file2_size_before_copy)
        delta = file2.read(file2_size_after_copy - file2_size_before_copy)

    # Process the delta
    # ...
    # Publish a message to the topic
    data = delta
    topic.publish(data=data)
