def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def compare_files(file1_lines, file2_lines):
    exit_nodes = set(file1_lines).difference(file2_lines)
    only_second_file_lines = set(file2_lines).difference(file1_lines)
    return sorted(exit_nodes), sorted(only_second_file_lines)


    

def main():
    file1_path = 'GStopo2000-01-01 00:00:00.000.txt'
    file2_path = 'GStopo2000-01-01 00:00:10.000.txt'
    output_file_path = 'output.txt'

    file1_lines = read_file(file1_path)
    file2_lines = read_file(file2_path)
    exit_nodes, only_second_file_lines = compare_files(file1_lines, file2_lines)
    with open(output_file_path, 'a') as file:
        file.write("#New Nodes: \n")
        file.write("".join(only_second_file_lines))  
        file.write("#Exit Nodes: \n")
        file.write("".join(exit_nodes))  


if __name__ == "__main__":
    main()

