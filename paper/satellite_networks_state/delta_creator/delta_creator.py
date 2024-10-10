import os
import re

# Function to read file contents
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Function to compare two files and return deltas
def compare_files(file1_lines, file2_lines):
    exit_nodes = set(file1_lines).difference(file2_lines)
    only_second_file_lines = set(file2_lines).difference(file1_lines)
    return sorted(exit_nodes), sorted(only_second_file_lines)

# Function to extract the timestamp from the filename
def extract_timestamp(file_name):
    match = re.search(r'GStopo(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3})\.txt', file_name)
    if match:
        return match.group(1)
    return None
    

# Main function to handle the comparison of all adjacent files
def main():
    # Get list of all files in the current directory
    files = [f for f in os.listdir() if f.startswith('GStopo') and f.endswith('.txt')]

    # Sort files based on their timestamp
    files.sort(key=lambda f: extract_timestamp(f))

    # Iterate through adjacent file pairs
    for i in range(len(files) - 1):
        file1_path = files[i]
        file2_path = files[i + 1]

        # Extract timestamps for the filenames
        time1 = extract_timestamp(file1_path)
        time2 = extract_timestamp(file2_path)

        if time1 and time2:
            # Generate a meaningful output file name
            output_file_name = f"{time1}-{time2}_delta.txt"

            # Read the contents of the two files
            file1_lines = read_file(file1_path)
            file2_lines = read_file(file2_path)

            # Compare the two files and get the deltas
            exit_nodes, only_second_file_lines = compare_files(file1_lines, file2_lines)

            # Write the deltas to the new output file
            with open(output_file_name, 'w') as output_file:
                output_file.write("# New Nodes:\n")
                output_file.write("".join(only_second_file_lines))
                output_file.write("# Exit Nodes:\n")
                output_file.write("".join(exit_nodes))

            print(f"Delta written to {output_file_name}")

if __name__ == "__main__":
    main()

