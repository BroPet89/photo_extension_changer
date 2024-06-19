import os
import logging

def rename_jfif_to_jpg(folder_path, dry_run=False):
    """
    Renames all .jfif files in the specified folder to .jpg.

    Parameters:
    folder_path (str): The path to the folder containing .jfif files.
    dry_run (bool): If True, perform a dry run without renaming files. Default is False.

    Returns:
    None
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    renamed_files_count = 0

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.jfif'):
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, filename[:-5] + '.jpg')
            
            if dry_run:
                logging.info(f'Dry Run: {old_file} -> {new_file}')
            else:
                try:
                    os.rename(old_file, new_file)
                    logging.info(f'Renamed: {old_file} -> {new_file}')
                    renamed_files_count += 1
                except Exception as e:
                    logging.error(f'Error renaming {old_file} to {new_file}: {e}')

    logging.info(f'Total files renamed: {renamed_files_count}')

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing .jfif files: ")
    dry_run = input("Perform a dry run? (yes/no): ").strip().lower() == 'yes'

    if not os.path.isdir(folder_path):
        logging.error(f'The directory {folder_path} does not exist.')
    else:
        rename_jfif_to_jpg(folder_path, dry_run)
