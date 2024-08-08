# This starter code is provided for your convenience if you want to use it.

def read_csv(filename, delimiter=',', encoding='utf-8'):
    data = []
    try:
        with open(filename, 'r', newline='', encoding=encoding) as file:
            for line in file:
                row = line.strip().split(delimiter)
                if row:  # Check if row is not empty after stripping
                    data.append(row)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return data


airports_data = read_csv('airports.csv')


if airports_data:
    for row in airports_data:
        print(row)  # Or further process the rows