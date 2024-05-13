def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def compare_files(file1_lines, file2_lines):
    common_lines = set(file1_lines).intersection(file2_lines)
    only_second_file_lines = set(file2_lines).difference(file1_lines)
    return sorted(common_lines), sorted(only_second_file_lines)

def write_to_file(lines, output_file):
    with open(output_file, 'w') as file:
        file.writelines(lines)

def main():
    file1_path = 'GStopo2000-01-01 00:00:00.000.txt'
    file2_path = 'GStopo2000-01-01 00:00:10.000.txt'
    output_file_path = 'output.txt'

    file1_lines = read_file(file1_path)
    file2_lines = read_file(file2_path)

    common_lines, only_second_file_lines = compare_files(file1_lines, file2_lines)

    new_file_lines = common_lines + only_second_file_lines
    write_to_file(new_file_lines, output_file_path)

if __name__ == "__main__":
    main()
