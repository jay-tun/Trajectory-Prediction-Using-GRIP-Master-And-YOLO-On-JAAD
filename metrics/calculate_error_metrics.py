import numpy as np

def load_trajectory_data(file_path):
    """
    Load the trajectory data from a file.
    Format: frame_id, object_id, object_type, x, y, object_length, object_width, heading
    """
    data = {}
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split()
            frame_id = int(parts[0])
            object_id = int(parts[1])
            object_type = int(parts[2])  # This is read but not filtered
            x = float(parts[3])
            y = float(parts[4])
            
            if frame_id not in data:
                data[frame_id] = {}
            data[frame_id][object_id] = (x, y)
    return data

def calculate_ADE_FDE(ground_truth, predicted):
    total_ADE = 0
    total_FDE = 0
    count = 0
    
    for frame_id in predicted:
        if frame_id in ground_truth:
            gt_frame_data = ground_truth[frame_id]
            pred_frame_data = predicted[frame_id]
            
            for object_id in pred_frame_data:
                if object_id in gt_frame_data:
                    gt = gt_frame_data[object_id]
                    pred = pred_frame_data[object_id]
                    ade = np.linalg.norm(np.array(gt) - np.array(pred))
                    total_ADE += ade
                    count += 1

            # FDE: Calculate for the last frame
            if count > 0:
                total_FDE += np.linalg.norm(np.array(gt) - np.array(pred))
    
    ADE = total_ADE / count if count > 0 else 0
    FDE = total_FDE / count if count > 0 else 0
    
    return ADE, FDE

# Load ground truth and predicted trajectories for pedestrians (object_type = 3)
ground_truth = load_trajectory_data("../second/data_folder/prediction_test/video_0123.txt")
predicted = load_trajectory_data("../second/prediction_result.txt")

# Calculate ADE and FDE
ADE, FDE = calculate_ADE_FDE(ground_truth, predicted)
print(f"Average Displacement Error (ADE): {ADE}")
print(f"Final Displacement Error (FDE): {FDE}")
