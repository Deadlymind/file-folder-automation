from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def rename_files_in_directory(directory):
    """
    Rename all files in the specified directory by adding a 'new-' prefix to each filename.

    Parameters:
    directory (str or Path): The path to the directory containing the files to be renamed.
    """
    root_dir = Path(directory)

    # Check if the directory exists
    if not root_dir.exists() or not root_dir.is_dir():
        logging.error(f"The directory {root_dir} does not exist or is not a directory.")
        return

    # Iterate over each file in the directory
    try:
        for path in root_dir.iterdir():
            if path.is_file():
                new_filename = "new-" + path.stem + path.suffix
                new_filepath = path.with_name(new_filename)
                logging.info(f"Renaming {path} to {new_filepath}")
                path.rename(new_filepath)
    except Exception as e:
        logging.error(f"An error occurred while renaming files: {e}")

if __name__ == "__main__":
    # Replace 'files' with your directory path if needed
    rename_files_in_directory('files')
