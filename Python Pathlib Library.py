from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Create a Path object
    p1 = Path('files/ghi.txt')

    # Print the type of p1
    logging.info(f"Type of p1: {type(p1)}")

    # Check if the file exists, if not, create it and write content
    if not p1.exists():
        try:
            with open(p1, 'w') as f:
                f.write('Content 3')
                logging.info(f"Created and wrote to file: {p1}")
        except Exception as e:
            logging.error(f"Error creating or writing to file: {e}")

    # Print file properties
    logging.info(f"File name: {p1.name}")
    logging.info(f"File stem: {p1.stem}")
    logging.info(f"File suffix: {p1.suffix}")
    logging.info(f"File parent: {p1.parent}")
    logging.info(f"File grandparent: {p1.parent.parent}")

    # Create a Path object for the directory
    p2 = Path('files')

    # Print the contents of the directory
    try:
        for item in p2.iterdir():
            logging.info(f"Directory item: {item}")
    except Exception as e:
        logging.error(f"Error iterating through directory: {e}")

if __name__ == "__main__":
    main()
