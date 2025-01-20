import shutil


def delete_directory(path):
    try:
        shutil.rmtree(path)
        print(f"Cleaned")
    except Exception as e:
        print(f"Failed to delete directory: {path}. Error: {e}")
