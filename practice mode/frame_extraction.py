import cv2
import os
def extract_frames_from_video(video_path, output_directory):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Check if video file was successfully opened
    if not video.isOpened():
        print("Error opening video file")
        return

    # Get some video properties
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)

    # Create the output directory if it doesn't exist
    #os.makedirs(output_directory, exist_ok=True)

    # Extract frames from the video
    for frame_index in range(frame_count):
        # Read the current frame
        ret, frame = video.read()

        # Check if frame was successfully read
        if not ret:
            print("Error reading frame {}".format(frame_index))
            continue

        # Construct the output image path
        image_path = os.path.join(output_directory, "frame_{}.jpg".format(frame_index))

        # Save the frame as an image
        cv2.imwrite(image_path, frame)

    # Release the video file
    video.release()

    print("Frames extracted successfully")

# Specify the video file path and output directory
video_path = "dataset_video.mp4"
output_directory = r"C:\Users\Dhruv\Desktop\capestone\dataset\frames"

# Call the function to extract frames
extract_frames_from_video(video_path, output_directory)
