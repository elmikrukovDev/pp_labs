SIZE_COLUMN_INDEX = 4

def get_mean_size(ls_output):
    total_size = 0
    file_count = 0

    for line in ls_output.strip().split('\n'):
        columns = line.split()

        if len(columns) < SIZE_COLUMN_INDEX:
            continue

        try:
            total_size += int(columns[SIZE_COLUMN_INDEX])
            file_count += 1
        except (ValueError, IndexError):
            continue

    if file_count == 0:
        return None
    
    return total_size / file_count

if __name__ == '__main__':
    import sys

    ls_output = sys.stdin.read()
    mean_size = get_mean_size(ls_output)

    if mean_size is None:
        print("No files for handling")
    else:
        print(f"Average: {mean_size:.2f} bytes")