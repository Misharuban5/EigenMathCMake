#!/bin/sh
# Since create-dmg does not clobber, be sure to delete previous DMG
BUILD_DIR=$1

if [ ! -d "${BUILD_DIR}" ]; then
  echo "$BUILD_DIR does not exist."
  exit -1
fi

[[ -f Math-Installer.dmg ]] && rm Math-Installer.dmg
[ -d "${BUILD_DIR}/source_folder" ] && rm -rf "${BUILD_DIR}/source_folder" 

mkdir ${BUILD_DIR}/source_folder
cp -rf ${BUILD_DIR}/math.app ${BUILD_DIR}/source_folder
# Create the DMG
create-dmg \
  --volname "Math Installer" \
  --window-pos 200 120 \
  --window-size 800 400 \
  --hide-extension "math.app" \
  --app-drop-link 600 185 \
  "Math-Installer.dmg" \
  "${BUILD_DIR}/source_folder"