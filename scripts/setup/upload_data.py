"""Script to upload CSV files"""
import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..')))
from scripts.authentication.service_principal import ws

def data_filepaths(data_folder=None):
    """Get full paths to discrete data files"""
    full_filepaths = []
    absolute_path = Path(data_folder).absolute()
    data_files = os.listdir(data_folder)
    for file in data_files:
        file_with_path = str(absolute_path) + '/' + str(file)
        full_filepaths.append(file_with_path)
    return full_filepaths

def upload_files_from_local(
        local_data_folder=None,
        target_def_blob_store_path=None,
        def_blob_store=None):
    """Function to upload files."""

    # Get input data files from local
    data_file_paths = data_filepaths(data_folder = local_data_folder)

    # Upload files to blob store
    def_blob_store.upload_files(
            files=data_file_paths,
            target_path=target_def_blob_store_path,
            overwrite=True,
            show_progress=True
            )

def main():
    """Set target locations, retrieve default blob store and upload files"""
    local_data_folder = './input-data'
    target_def_blob_store_path = '/blob-input-data/'
    def_blob_store = ws.get_default_datastore()

    # Upload files
    upload_files_from_local(
            local_data_folder=local_data_folder,
            target_def_blob_store_path=target_def_blob_store_path,
            def_blob_store=def_blob_store
            )

if __name__ == "__main__":
    main()
