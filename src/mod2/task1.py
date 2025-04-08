RSS_COLUMN_INDEX = 5
size_names = ['B', 'KB', 'MB', 'GB', 'TB']

def get_summary_rss(file_path):
    total_rss = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]
        for line in lines:
            columns = line.split()
            if len(columns) < RSS_COLUMN_INDEX:
                continue
            try:
                rss = int(columns[RSS_COLUMN_INDEX])
                total_rss += rss
            except ValueError:
                continue

    return total_rss

def convert_to_size(bytes):
    index = 0

    while bytes >= 1024 and index < len(size_names) - 1:
        bytes /= 1024.0
        index += 1

    return f"{bytes:.2f} {size_names[index]}"
    
if __name__ == '__main__':
    from pathlib import Path

    file_path = Path(input(f"PS AUX output file path:"))
    if file_path.exists() and file_path.is_file():
        rss_mem_sum = get_summary_rss(file_path)
        rss_mem_size = convert_to_size(rss_mem_sum)
        print(f"RSS Summary: {rss_mem_size}")
    else:
        print("No such PS AUX output file...")