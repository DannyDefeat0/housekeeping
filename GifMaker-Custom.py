import imageio
import os
import re
from os import walk


#Try creating a free account in AWS in S3 and see if this can run automatically
#Try generative AI to fix images (GIF ERROR)
#No exception handling



def assemble_animated_mov(dir_path, filenames, filename_out):
    filepath_out = os.path.join(dir_path, filename_out)
    images = []
    for filename in filenames:
        temp = os.path.join(dir_path, filename)
        image = imageio.imread(temp)
        images.append(image)
    imageio.mimsave(filepath_out, images, format='FFMPEG', fps=.33)


def extract_info(input_string):
    match = re.search(r'\b(\d{5})-(\w+)', input_string)
    if match:
        return f"{match.group(1)}-{match.group(2)}".replace("_"+match.group(1),"")
    else:
        #We could improve this by making sure either an error or the expected file type is returned
        #later on we have to write "if asset" as a check
        return None


def main(parent_folder):
    #this gets a list of all files in our directory, which is how BCs are organized
    filenames = next(walk(parent_folder), (None, None, []))[2]  # [] if no file
    model_count = {}
    for file in filenames:
        asset = extract_info(file)
        if asset:
            if asset in model_count:
                model_count[asset].append(file)
            else:
                model_count[asset] = [file]
    for model in model_count:
        if len(model_count[model]) > 1:
            assemble_animated_mov(parent_folder, model_count[model], model+"_Combo_Apr24_mov.mov")
    print(model_count)

main("C:/Users/damon.melton/Documents/Display Ads")
#assemble_animated_mov("C:/Users/damon.melton/Documents/Display Ads",['12345-April_1200x1200.jpg','12345-April_1500_1200x1200.jpg','12345-April_2500_1200x1200.jpg'],"Test")
