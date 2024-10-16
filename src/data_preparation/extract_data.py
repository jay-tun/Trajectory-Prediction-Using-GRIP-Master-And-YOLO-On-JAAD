import os
import xml.etree.ElementTree as ET
import math

# Function to calculate heading
def calculate_heading(xtl, ytl, xbr, ybr):
    # Assuming the heading is the angle of the vector from (xtl, ytl) to (xbr, ybr) with respect to the x-axis
    delta_x = xbr - xtl
    delta_y = ybr - ytl
    heading = math.atan2(delta_y, delta_x)
    # Round the heading to 3 decimal places
    heading = round(heading, 3)
    return heading

# Function to convert label to object type ID
def get_object_type_id(label):
    object_types = {
        "small vehicles": 1,
        "big vehicles": 2,
        "pedestrian": 3,
        "motorcyclist and bicyclist": 4,
        "others": 5
    }
    return object_types.get(label, 5)  # Default to 5 for unknown types

data_path = "/home/jnomad/Documents/Semester 6/Thesis/GRIP-master/JAAD-JAAD_2.0/annotations"
output_file_path = "/home/jnomad/Documents/Semester 6/Thesis/GRIP-master/data_folder/data_set/"

for filename in os.listdir(data_path):
    if filename.endswith(".xml"):
        tree = ET.parse(os.path.join(data_path, filename))
        root = tree.getroot()

        output_filename = os.path.splitext(filename)[0] + ".txt"
        output_filepath = os.path.join(output_file_path, output_filename)

        data = []
        for track in root.findall('.//track'):
            label = track.get('label')
            object_type = get_object_type_id(label)
            for box in track.findall('.//box'):
                frame_id = int(box.get('frame'))
                #remove the last character "b" or "p" as well as "_"
                #to avoid conflict while data processing
                object_id = box.find('attribute[@name="id"]').text.lstrip("0").rstrip("pb").replace("_","")
                xtl = float(box.get('xtl'))
                ytl = float(box.get('ytl'))
                xbr = float(box.get('xbr'))
                ybr = float(box.get('ybr'))
                position_x = (xtl + xbr) / 2
                position_y = (ytl + ybr) / 2
                heading = calculate_heading(xtl, ytl, xbr, ybr)
                data.append((frame_id, object_id, object_type, position_x, position_y, xbr - xtl, ybr - ytl, heading))

        # Sort the data by frame_id
        data.sort(key=lambda x: x[0])

        with open(output_filepath, "w") as output_file:
            for col in data:
                output_file.write(f"{col[0]} {col[1]} {col[2]} {col[3]} {col[4]} {col[5]} {col[6]} {col[7]}\n")

print("Conversion completed successfully.")
