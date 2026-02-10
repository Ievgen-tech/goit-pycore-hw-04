import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama для роботи з кольорами
init(autoreset=True)


def get_file_color(file_path):
    """
    Повертає колір для файлу за його розширенням.

    Args:
        file_path: Path об'єкт файлу
    """
    suffix = file_path.suffix.lower()

    color_map = {
        ".py": Fore.YELLOW,
        ".txt": Fore.CYAN,
        ".md": Fore.MAGENTA,
        ".json": Fore.LIGHTGREEN_EX,
        ".csv": Fore.LIGHTCYAN_EX,
        ".jpg": Fore.LIGHTRED_EX,
        ".jpeg": Fore.LIGHTRED_EX,
        ".png": Fore.LIGHTRED_EX,
        ".gif": Fore.LIGHTRED_EX,
        ".svg": Fore.LIGHTRED_EX,
        ".pdf": Fore.LIGHTMAGENTA_EX,
        ".zip": Fore.LIGHTYELLOW_EX,
        ".rar": Fore.LIGHTYELLOW_EX,
        ".7z": Fore.LIGHTYELLOW_EX,
    }

    return color_map.get(suffix, Fore.GREEN)


def print_directory_structure(path, prefix=""):
    """
    Рекурсивно виводить структуру директорії з кольорами.

    Args:
        path: Path об'єкт директорії
        prefix: Префікс для форматування (для індентації)
    """
    try:
        # Отримуємо список елементів в директорії
        items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name))

        # Розділяємо на папки і файли
        directories = [item for item in items if item.is_dir()]
        files = [item for item in items if item.is_file()]

        # Загальна кількість елементів
        total_items = len(directories) + len(files)

        # Виводимо папки
        for i, directory in enumerate(directories):
            is_last = (i + len(files) == total_items - 1)

            # Визначаємо символи переходу
            connector = "└── " if is_last else "├── "

            # Виводимо назву папки синім кольором
            print(f"{prefix}{connector}{Fore.BLUE}{directory.name}{Style.RESET_ALL}")

            # Визначаємо префікс для наступного рівня
            extension = "    " if is_last else "│   "

            # Рекурсивно виводимо вміст папки
            print_directory_structure(
                directory,
                prefix + extension
            )

        # Виводимо файли
        for i, file in enumerate(files):
            is_last = (i == len(files) - 1)

            # Визначаємо символи переходу
            connector = "└── " if is_last else "├── "

            # Виводимо назву файлу залежно від розширення
            file_color = get_file_color(file)
            print(f"{prefix}{connector}{file_color}{file.name}{Style.RESET_ALL}")

    except PermissionError:
        print(f"{prefix}{Fore.RED}[Permission Denied]{Style.RESET_ALL}")
    except (OSError, IOError) as e:
        print(f"{prefix}{Fore.RED}[Error: {str(e)}]{Style.RESET_ALL}")


def main():
    """Основна функція програми."""

    # Перевіряємо, чи передан аргумент
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Шлях до директорії не передано.{Style.RESET_ALL}")
        print("Використання: python hw04.py <шлях_до_директорії>")
        sys.exit(1)

    path_str = sys.argv[1]

    try:
        # Конвертуємо рядок в Path об'єкт
        path = Path(path_str)

        # Перевіряємо, чи існує шлях
        if not path.exists():
            print(f"{Fore.RED}Помилка: Шлях '{path_str}' не існує.{Style.RESET_ALL}")
            sys.exit(1)

        # Перевіряємо, чи це директорія
        if not path.is_dir():
            print(f"{Fore.RED}Помилка: '{path_str}' не є директорією.{Style.RESET_ALL}")
            sys.exit(1)

        # Виводимо назву кореневої директорії
        print(f"{Fore.BLUE}{path.name}{Style.RESET_ALL}/")

        # Виводимо структуру директорії
        print_directory_structure(path)

    except (OSError, ValueError) as e:
        print(f"{Fore.RED}Помилка: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)


if __name__ == "__main__":
    main()
