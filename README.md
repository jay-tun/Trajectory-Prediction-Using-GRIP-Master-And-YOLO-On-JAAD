
# Real-time Graph-based Interaction-aware Trajectory Prediction for Autonomous Vehicles

This repository contains the code, data, and results for my thesis project, **Real-time Graph-based Interaction-aware Trajectory Prediction for Autonomous Vehicles**. The project involves data preparation, trajectory prediction using a modified version of GRIP++, visualization of results, and error calculation.

## Table of Contents
- [Project Overview](#project-overview)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
The goal of this project is to predict the future trajectories of agents (e.g., vehicles, pedestrians) in real-time using a graph-based interaction-aware model. The project uses the GRIP++ framework with custom modifications for improved accuracy and efficiency. Additionally, visualization scripts are included for better understanding of the predictions, along with error calculation to evaluate performance.

## Folder Structure
```
/
├── data_preparation/            # Scripts for preparing the dataset
│   └── data_loader.py           # Data loading and processing
│
├── grip_plus_plus/              # Modified GRIP++ framework
│   ├── original_code/           # (Optional) Original GRIP++ code
│   ├── modified_code.py         # Code with my parameter adjustments
│   └── parameters_config.py     # Configuration for the custom parameters
│
├── visualization/               # Scripts for visualizing the results
│   ├── segmentation.py          # Segmentation script
│   ├── plot_results.py          # Script to plot results
│   └── error_calculation.py     # Script for calculating prediction errors
│
├── results/                     # Output files from experiments
│   ├── images/                  # Generated result images
│   └── videos/                  # Generated result videos (Note: large files)
│       ├── predictions.mp4      # Example video of prediction overlays
│       └── analysis.mp4         # Analysis video
│
└── README.md                    # Project documentation (this file)
```

## Installation
To run the code in this repository, you need to have Python 3 installed along with the necessary dependencies.

1. Clone this repository:
   ```bash
   git clone https://github.com/jay-tun/Trajectory-Prediction-Using-GRIP--And-YOLO-O.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Trajectory-Prediction-Using-GRIP--And-YOLO-O
   ```

3. Install dependencies (you can set up a virtual environment first if desired):
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Data Preparation
Use the scripts in the `data_preparation/` folder to process and load the dataset:
```bash
python data_preparation/data_loader.py
```

### Running GRIP++ with Modifications
Run the modified GRIP++ model with your parameter adjustments:
```bash
python grip_plus_plus/modified_code.py
```

### Visualizing Results
To visualize the segmentation and prediction results:
```bash
python visualization/segmentation.py
python visualization/plot_results.py
```

### Error Calculation
To calculate prediction errors, run:
```bash
python visualization/error_calculation.py
```

## Results
Example result images and videos are located in the `results/` folder. These include:
- **Images**: Overlays of predictions on the original scenes.
- **Videos**: Predictions visualized over time.
  
Larger video files can be found in [Google Drive](#) or [GitHub Releases](#) (add links to where you've hosted the videos externally if necessary).

## Contributing
If you want to contribute to this project, feel free to open an issue or submit a pull request. Please make sure to follow the contributing guidelines in `CONTRIBUTING.md` (if applicable).

## License
This project is licensed under the [MIT License](LICENSE).
