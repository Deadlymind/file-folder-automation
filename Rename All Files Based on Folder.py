from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def rename_files_in_directory_tree(directory):
    """
    Recursively rename all files in the directory tree by prefixing filenames with their parent folder name.

    Parameters:
    directory (str or Path): The path to the directory containing the files to be renamed.
    """
    root_dir = Path(directory)
    
    # Check if the directory exists and is a directory
    if not root_dir.exists() or not root_dir.is_dir():
        logging.error(f"The directory {root_dir} does not exist or is not a directory.")
        return

    # Iterate over each file in the directory tree
    try:
        file_paths = root_dir.glob('**/*')
        for path in file_paths:
            if path.is_file():
                parent_folder = path.parent.name  # Get the name of the parent folder
                new_filename = f"{parent_folder}-{path.name}"
                new_path = path.with_name(new_filename)
                
                logging.info(f"Renaming {path} to {new_path}")
                path.rename(new_path)
        logging.info("Renaming completed.")
    except Exception as e:
        logging.error(f"An error occurred while renaming files: {e}")

if __name__ == "__main__":
    # Replace 'files' with your directory path if needed
    rename_files_in_directory_tree('files')
