import pathspec

def parse_ignore_file(ignore_file_path):
    with open(ignore_file_path, 'r') as f:
        return pathspec.PathSpec.from_lines('gitwildmatch', f)

def is_ignored(file_path, spec):
    return spec.match_file(file_path)
