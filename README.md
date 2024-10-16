
# Real-time Graph-based Interaction-aware Trajectory Prediction for Autonomous Vehicles

## Project Overview

This repository contains the implementation and results of the thesis titled "Real-time Graph-based Interaction-aware Trajectory Prediction for Autonomous Vehicles." The project focuses on developing a system that predicts vehicle trajectories in real time using interaction-aware models based on graph representations.

## Project Structure

The repository is organized as follows:

```
├── data_folder/
│   ├── first_iteration/
│   │   ├── prediction_test/
│   │   └── prediction_train/
│   └── second_iteration/
│       ├── prediction_test/
│       └── prediction_train/
├── data_preparation/
│   ├── erase_empty_file.py
│   ├── extract_data.py
│   ├── randomize_data.py
│   └── split_data.py
├── docs/
│   ├── thesis.pdf
│   └── extracted_latex/
├── grip_plus_plus/
│   └── modified_GRIP++/
├── metrics/
│   ├── calculate_error_metrics.py
│   └── identify_epoch.py
├── results/
│   ├── numerical_results/
│   └── videos/
├── visualize/
│   ├── overlay_trajectory.py
│   └── segmentation_and_yolo.py
└── requirements.txt
```

## Installation

To set up the project environment, you will need Python 3 and pip. You can create a virtual environment (recommended) and install the required packages using the following commands:

```bash
# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install the required packages
pip install -r requirements.txt
```

## Usage

### Data Preparation

Before running the models, ensure that the data is correctly prepared. You can use the scripts in the `data_preparation/` folder to clean and preprocess your data.

### Running the Model

1. Navigate to the folder containing the model scripts.
2. Run the desired script to start the training or testing process.

For example, to overlay trajectories, you can run:

```bash
python visualize/overlay_trajectory.py
```

### Results

After running the models, you will find the output in the `results/` folder, including numerical results and generated videos.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your improvements or features.

