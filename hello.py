import re
import os

images = ["egg","example file 11313131","GLBC-BCDF-Inc-2-8-68867-Jeep_68867_68867-BelmontDodge_Jeep_Grand Cherokee L_1200x1200","GLBC-BCDF-Inc-2-8-68867-Jeep_68867_68867-BelmontDodge_Jeep_Compass_1200x1200","GLBC-BCDF-Inc-2-8-26326-Chrysler_26326_26326-HidayChrysler_Chrysler_Pacifica_1200x1200"]

def extract_info(input_string):
    match = re.search(r'\b(\d{5})-(\w+)', input_string)
    if match:
        return f"{match.group(1)}-{match.group(2)}".replace("_"+match.group(1),"")
    else:
        return None
# Example usage
model_count = {}
for image in images:
    asset = extract_info(image)
    if asset:
        if asset in model_count:
            model_count[asset].append(image)
        else:
            model_count[asset] = [image]
for model in model_count:
    print(len(model_count[model]))

