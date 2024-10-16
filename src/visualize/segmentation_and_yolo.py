import torch
import cv2
import numpy as np
from torchvision import models, transforms

# Load YOLOv5 model for object detection
model_yolo = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Load DeepLabV3+ model for semantic segmentation
model_deeplab = models.segmentation.deeplabv3_resnet101(pretrained=True).eval()

# Define transformations for DeepLabV3+
preprocess = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((520, 520)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Function to draw bounding boxes
def draw_boxes(frame, results):
    detections = results.xyxy[0].numpy()  # Get detections
    for *box, conf, cls in detections:
        label = f'{model_yolo.names[int(cls)]} {conf:.2f}'
        cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 0), 2)
        cv2.putText(frame, label, (int(box[0]), int(box[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame

# Function to apply DeepLabV3+ semantic segmentation
def apply_segmentation(frame):
    input_image = preprocess(frame).unsqueeze(0)
    with torch.no_grad():
        output = model_deeplab(input_image)['out'][0]
    output_predictions = output.argmax(0).byte().cpu().numpy()
    return output_predictions

# Function to overlay segmentation results
def overlay_segmentation(frame, segmentation):
    segmentation = cv2.resize(segmentation, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_NEAREST)
    color_segmentation = np.zeros((segmentation.shape[0], segmentation.shape[1], 3), dtype=np.uint8)
    
    # Define colors for different classes (PASCAL VOC color scheme)
    colors = {
        0: (0, 0, 0),       # background
        1: (128, 0, 0),     # aeroplane
        2: (0, 128, 0),     # bicycle
        3: (128, 128, 0),   # bird
        4: (0, 0, 128),     # boat
        5: (128, 0, 128),   # bottle
        6: (0, 128, 128),   # bus
        7: (128, 128, 128), # car
        8: (64, 0, 0),      # cat
        9: (192, 0, 0),     # chair
        10: (64, 128, 0),   # cow
        11: (192, 128, 0),  # dining table
        12: (64, 0, 128),   # dog
        13: (192, 0, 128),  # horse
        14: (64, 128, 128), # motorbike
        15: (192, 128, 128),# person
        16: (0, 64, 0),     # potted plant
        17: (128, 64, 0),   # sheep
        18: (0, 192, 0),    # sofa
        19: (128, 192, 0),  # train
        20: (0, 64, 128),   # tv/monitor
    }
    
    for class_id, color in colors.items():
        mask = segmentation == class_id
        color_segmentation[mask] = color
    
    return cv2.addWeighted(frame, 0.7, color_segmentation, 0.3, 0)

# Load video
video_path = 'first/test_video/video_0269.mp4'
cap = cv2.VideoCapture(video_path)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Create VideoWriter object to save the processed video
output_path = 'first/result_video/result_video_with_yolo_deeplabv3plus.mp4'
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Process the video frame by frame
frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    print(f'Processing frame {frame_count}')
    
    # Convert frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Perform YOLO inference
    results = model_yolo(frame_rgb)

    # Draw bounding boxes
    frame_with_boxes = draw_boxes(frame, results)

    # Apply semantic segmentation using DeepLabV3+
    segmentation = apply_segmentation(frame_rgb)
    
    # Overlay segmentation results
    frame_with_segmentation = overlay_segmentation(frame_with_boxes, segmentation)

    # Write the frame into the output video
    out.write(frame_with_segmentation)

# Release everything
cap.release()
out.release()
print(f"Processed video saved to {output_path}")