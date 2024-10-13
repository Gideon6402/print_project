def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as infile:
        return infile.read()

def write_to_output(output_file, content):
    with open(output_file, 'a', encoding='utf-8') as outfile:
        outfile.write(content)
