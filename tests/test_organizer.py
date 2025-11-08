import os
import shutil
import pytest
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from organizer import organize_files


SOURCE_FOLDER = "data"

@pytest.fixture(scope="function")
def setup_test_files():
    
    if os.path.exists(SOURCE_FOLDER):
        shutil.rmtree(SOURCE_FOLDER)
    os.makedirs(SOURCE_FOLDER, exist_ok=True)

 
    files = ["test_doc.pdf", "test_image.jpg", "test_video.mp4", "test_unknown.xyz"]
    for f in files:
        with open(os.path.join(SOURCE_FOLDER, f), "w") as file:
            file.write("sample content")
    yield files

   
    for folder in ["Documents", "Images", "Videos", "Others"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)



def test_organize_files(setup_test_files):
    organize_files()

    assert os.path.exists("Documents/test_doc.pdf")
    assert os.path.exists("Images/test_image.jpg")
    assert os.path.exists("Videos/test_video.mp4")
    assert os.path.exists("Others/test_unknown.xyz")
