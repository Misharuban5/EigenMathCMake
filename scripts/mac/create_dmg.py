import math
from pathlib import Path
import dmgbuild
import argparse
import os
import shutil

APP_NAME="math"
APP_BUNDLE_TEMP_FOLDER = "temp"
APP_INSTALL_FILE = APP_NAME + ".dmg"
APP_BUNDLE = "math.app"

'''
target = tmp_path / "out.dmg"
    dmgbuild.build_dmg(
        str(target), "Test", str(Path(__file__).parent / "examples" / "settings.py")
    )
'''
def prepare(path):
    # clean folders
    installer_path = os.path.join(path, APP_INSTALL_FILE)
    if os.path.exists(installer_path) and os.path.isfile(installer_path):
        os.remove(installer_path)
    
    bundle_tmp_path = os.path.join(path, APP_BUNDLE_TEMP_FOLDER)
    if os.path.exists(bundle_tmp_path) and os.path.isdir(bundle_tmp_path):
        shutil.rmtree(bundle_tmp_path)

    os.makedirs(bundle_tmp_path)
    
    # prepare bundle tmp folder
    bundle_path = os.path.join(path, APP_BUNDLE)
    
    #shutil.copytree(bundle_path, bundle_tmp_path)
    os.system("cp -rf " + bundle_path + " " + bundle_tmp_path)

def create_dmg(path):
    target = os.path.join(path , APP_INSTALL_FILE)
    app_path = os.path.join(path , APP_BUNDLE)
    dmgbuild.build_dmg(
        str(target), APP_NAME, str(Path(__file__).parent / "settings.py"),defines={"app":app_path}
    )

# Parsing input
parser = argparse.ArgumentParser()
parser.add_argument("path", type=str,
                    help="path to build folder")
args = parser.parse_args()
working_dir = args.path

prepare(working_dir)
create_dmg(working_dir)

