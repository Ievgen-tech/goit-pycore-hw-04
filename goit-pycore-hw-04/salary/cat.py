import os


def get_cats_info(path):
    """
    Reads a file with cat information and returns a list of dictionaries.

    Args:
        path: Path to the text file containing cat data

    Returns:
        List of dictionaries with keys: 'id', 'name', 'age'

    Raises:
        FileNotFoundError: If the file doesn't exist
        IOError/OSError: If there's an error reading the file
    """
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue

                # Split the line by comma
                parts = line.split(',')

                # Validate that we have exactly 3 parts
                if len(parts) != 3:
                    print(f"Warning: Skipping invalid line: {line}")
                    continue

                # Create dictionary for the cat
                cat_dict = {
                    'id': parts[0],
                    'name': parts[1],
                    'age': parts[2]
                }

                cats.append(cat_dict)

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied to read file '{path}'.")
        return []
    except IsADirectoryError:
        print(f"Error: '{path}' is a directory, not a file.")
        return []
    except UnicodeDecodeError as e:
        print(f"Error: File encoding issue. Expected UTF-8. Details: {e}")
        return []
    except (IOError, OSError) as e:
        print(f"Error: Unable to read file '{path}'. Details: {e}")
        return []

    return cats


# Example usage
if __name__ == "__main__":
    # Get the directory of the current script and construct the path to cats.txt
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cats_file = os.path.join(script_dir, 'cats.txt')

    # Test the function with the cats file
    result = get_cats_info(cats_file)
    for cat in result:
        print(cat)
