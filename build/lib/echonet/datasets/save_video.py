import os
import numpy as np
import echonet

def read_bounding_boxes(self, filename):
    bounding_boxes = {}
    with open(filename, 'r') as file:
        # Skip header line
        next(file)
        for line in file:
            parts = line.strip().split(',')
            file_name = parts[0]
            x1, y1, x2, y2, frame = map(int, parts[1:])
            if file_name not in bounding_boxes:
                bounding_boxes[file_name] = {}
            if frame not in bounding_boxes[file_name]:
                bounding_boxes[file_name][frame] = []
            bounding_boxes[file_name][frame].append((x1, y1, x2, y2))
    return bounding_boxes

def perform_segmentation(video, bounding_boxes):
   # Code for segmentation (as provided earlier)
   pass

def save_segmented_video(segmented_frame, file_name):
   echonet.utils.savevideo(f'segmented_{file_name}.avi', segmented_frame)

if __name__ == "__main__":
    # Assuming you call this script from the command line
    # Load video file (you'll need to replace 'video_file_path' with the actual path)
    video = echonet.utils.loadvideo('video_file_path').astype(np.float32)

    # Read bounding box coordinates
    bounding_boxes = read_bounding_boxes('volumetracing.csv')

    # Perform segmentation
    for frame in bounding_boxes:
        x1, y1, x2, y2 = bounding_boxes[frame][0]  # Assuming one bounding box per frame
        segmented_frame = video[:, frame, y1:y2, x1:x2]  # Perform segmentation

        # Save segmented video
        save_segmented_video(segmented_frame, os.path.basename('video_file_path'))
