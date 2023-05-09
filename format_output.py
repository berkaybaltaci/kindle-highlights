import os

def format_output():
    # get the current directory
    current_dir = os.getcwd()

    # set the folder name
    folder_name = "clippings"

    # create the path to the folder
    folder_path = os.path.join(current_dir, folder_name)

    # loop through all files in the folder
    for filename in os.listdir(folder_path):
        # check if the file is a text file
        if filename.endswith(".rst") or filename.endswith('.txt'):
            # create the path to the input file
            input_file_path = os.path.join(folder_path, filename)

            # create the path to the output file
            output_file_path = os.path.join(folder_path, filename[:-4] + ".txt")

            # open the input file
            with open(input_file_path, "r") as input_file:
                # read the lines of the input file
                lines = input_file.readlines()

            filtered_lines = [line for line in lines if not line.startswith("..") and (line[0].isupper() or line.startswith('=') or line.startswith(':'))]

            # set the line number to 1
            line_number = 1
            prev_line = ""
            for i in range(len(filtered_lines)):
                if filtered_lines[i] == prev_line:
                    filtered_lines.remove(prev_line)
                # check if the line is not blank
                elif filtered_lines[i].startswith(':'):
                    filtered_lines.insert(i + 1, "\n")
                elif filtered_lines[i].strip() and i != 0 and not filtered_lines[i].startswith('='):
                    # add the line number and the line to the line
                    filtered_lines[i] = f"{line_number}. {filtered_lines[i]}"
                    # increment the line number
                    line_number += 1
                prev_line = filtered_lines[i]

            # open the output file
            with open(output_file_path, "w") as output_file:
                # write the filtered lines to the output file
                output_file.writelines(filtered_lines)


    # loop through all files in the folder
    for filename in os.listdir(folder_path):
        # check if the file has a .rst extension
        if filename.endswith(".rst"):
            # create the path to the file
            file_path = os.path.join(folder_path, filename)

            # delete the file
            os.remove(file_path)