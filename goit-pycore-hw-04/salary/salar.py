def total_salary(path):
    """
    Analyzes a file with developer salaries and returns total and average salary.

    Args:
        path: Path to the text file with salary data (each line: name,salary)

    Returns:
        Tuple of (total_salary, average_salary) where:
            - total_salary: Sum of all developer salaries
            - average_salary: Average salary per developer

    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    try:
        total = 0
        count = 0

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue

                parts = line.split(',')
                if len(parts) >= 2:
                    try:
                        salary = int(parts[1])
                        total += salary
                        count += 1
                    except (ValueError, IndexError):
                        print(f"Warning: Invalid salary data in line: {line}")
                        continue

        if count == 0:
            return (0, 0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print(f"Error: File not found - {path}")
        raise
    except Exception as e:
        print(f"Error: An error occurred while reading the file - {e}")
        raise


# Example usage and testing
if __name__ == "__main__":
    # Test with sample data
    try:
        result = total_salary("salary_data.txt")
        print(f"Total salary: {result[0]}")
        print(f"Average salary: {result[1]}")
    except FileNotFoundError:
        print("Please create a salary_data.txt file with developer salaries")
