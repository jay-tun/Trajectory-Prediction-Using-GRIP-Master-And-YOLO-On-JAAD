import numpy as np
import cv2
from PIL import Image
import os

def load_predictions(prediction_file):
    predictions = {}
    with open(prediction_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            frame_id = int(parts[0])
            object_id = int(parts[1])
            object_type = int(parts[2])
            x = float(parts[3])
            y = float(parts[4])
            if object_id not in predictions:
                predictions[object_id] = []
            predictions[object_id].append((frame_id, object_type, x, y))
    return predictions

def load_image_frames(image_folder):
    frames = []
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')])
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = Image.open(image_path)
        frame = np.array(image)
        frames.append(frame)
    print(f"Loaded {len(frames)} frames from {image_folder}")
    return frames


def load_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return []
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    print(f"Loaded {len(frames)} frames from {video_path}")
    return frames

def overlay_predictions(frames, predictions):
    colors = {
        1: (0, 0, 255),  # Red for small vehicles
        2: (0, 255, 0),  # Green for big vehicles
        3: (255, 0, 0),  # Blue for pedestrians
        4: (0, 255, 255), # Yellow for bicycles
        5: (255, 0, 255)  # Magenta for others
    }
    
    for frame_id in range(len(frames)):
        for object_id, trajectory in predictions.items():
            # Filter trajectory points for this frame and future frames
            future_trajectory = [point for point in trajectory if point[0] >= frame_id]
            
            if future_trajectory:
                color = colors.get(future_trajectory[0][1], (255, 255, 255))  # Get color based on object type
                
                # Draw the entire future trajectory
                for i in range(1, len(future_trajectory)):
                    prev_point = future_trajectory[i-1]
                    curr_point = future_trajectory[i]
                    cv2.line(frames[frame_id], 
                             (int(prev_point[2]), int(prev_point[3])), 
                             (int(curr_point[2]), int(curr_point[3])), 
                             color, 2)
                
                # Draw a circle for the current position
                current_point = future_trajectory[0]
                cv2.circle(frames[frame_id], (int(current_point[2]), int(current_point[3])), 3, color, -1)
                
                # Add label
                label = f'ID: {object_id}'
                cv2.putText(frames[frame_id], label, 
                            (int(current_point[2])+5, int(current_point[3])-5), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    
    return frames


def save_video(frames, output_path, fps=20):
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
    if not frames:
        print("Error: No frames to write to video.")
        return
    height, width, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    for frame in frames:
        out.write(frame)
    out.release()
    print(f"Saved video to {output_path}")

def save_processed_frames(frames, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for i, frame in enumerate(frames):
        output_path = os.path.join(output_folder, f"processed_frame_{i:04d}.jpg")
        cv2.imwrite(output_path, frame)
    print(f"Saved {len(frames)} processed frames to {output_folder}")

# Load predictions
predictions = load_predictions('first/prediction_result.txt')

# Load image
#image_folder = '/home/jnomad/Documents/Semester 6/Thesis/GRIP-master/video_0269'
#frames = load_image_frames(image_folder)

#load video
video_path = 'first/result_video/result_video_with_yolo_deeplabv3plus.mp4'
frames = load_video(video_path)

if not frames:
    print("Error: No frames loaded from video.")
else:
    # Overlay predictions on frames
    frames_with_predictions = overlay_predictions(frames, predictions)

    #Save the resulting images
    #output_path = '/home/jnomad/Documents/Semester 6/Thesis/GRIP-master/result_image/'
    #save_processed_frames(frames_with_predictions, output_path)
    #Save video
    output_path = 'first/result_video/final_result.mp4'
    save_video(frames_with_predictions, output_path)
    
