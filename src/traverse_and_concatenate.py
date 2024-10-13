import os
import logging
from .ignore_parser import parse_ignore_file, is_ignored
from .file_handler import read_file, write_to_output

def traverse_and_concatenate(root_dir, output_file, ignore_file):
    spec = parse_ignore_file(ignore_file)
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for current_path, dirs, files in os.walk(root_dir):
            # Modify dirs in-place to skip ignored directories
            dirs[:] = [d for d in dirs if not is_ignored(os.path.join(current_path, d), spec)]
            for file in files:
                file_path = os.path.join(current_path, file)
                relative_path = os.path.relpath(file_path, root_dir)
                if is_ignored(relative_path, spec):
                    logging.info(f"Excluding {relative_path}")
                    continue
                try:
                    content = read_file(file_path)
                    outfile.write(f'\n# ----- {relative_path} -----\n')
                    outfile.write(content)
                    logging.info(f"Added {relative_path}")
                except Exception as e:
                    logging.error(f"Failed to read {relative_path}: {e}")
