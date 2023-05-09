import os

def format_output():
    current_dir = os.getcwd()
    folder_name = "clippings"
    folder_path = os.path.join(current_dir, folder_name)

    # loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".rst") or filename.endswith('.txt'):
            input_file_path = os.path.join(folder_path, filename)
            output_file_path = os.path.join(folder_path, filename[:-4] + ".txt")

            with open(input_file_path, "r") as input_file:
                # read the lines of the input file
                lines = input_file.readlines()

            filtered_lines = [line for line in lines if not line.startswith("..") and (line[0].isupper() or line.startswith('=') or line.startswith(':'))]

            line_number = 1
            prev_line = ""
            for i in range(len(filtered_lines)):
                if filtered_lines[i] == prev_line:
                    filtered_lines.remove(prev_line)
                elif filtered_lines[i].startswith(':'):
                    filtered_lines.insert(i + 1, "\n")
                elif filtered_lines[i].strip() and i != 0 and not filtered_lines[i].startswith('='):
                    # add the line number
                    filtered_lines[i] = f"{line_number}. {filtered_lines[i]}"
                    line_number += 1
                prev_line = filtered_lines[i]

            with open(output_file_path, "w") as output_file:
                # write the filtered lines to the output file
                output_file.writelines(filtered_lines)

    # loop through all files in the folder, delete if it's an rst file
    for filename in os.listdir(folder_path):
        if filename.endswith(".rst"):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)