# CMAKE with custom library tutorial

## Introduction

This project aims to be tutorial to cmake to create a custom library and a sample application to verify the function

## Prepare build environment

### On Windows

- Microsoft Visual Studio 2019.
- Python 3.10.
- WiX Toolset 3.11

### On Mac

- Install build tool(clang, xcode) - refer details at https://mac.install.guide/commandlinetools/4.html

```
$ xcode-select --install
```

- Install pkg-config

```
$ brew install pkg-config
```

- Install cmake

```
$ brew install cmake
```

- Install Eigen3 lib

```
$ brew install eigen
```

- Install create-dmg tool to create dmg installer
```
# incase you want to use shell script
$ brew install create-dmg

# incase you want to use python script
$ pip3 install dmgbuild
```

## Build & Testing

### On Windows
- Open Visual Studio 2019
- File --> Open --> Cmake: Then choose Eigen3Demo folder.
- Project --> Configure ...
- Then you can Build/Debug the application.

### On Mac

#### Without xcode

- Build

```
$ mkdir build_console
$ cd build_console
$ cmake ../
$ make
```

- Run examples

```
// Run math without parameters
$ /math.app/Contents/MacOS/math
```

#### Build without xcode

- Generate xcode project

```
mkdir build_xcode
cd build_xcode
cmake -G Xcode -DDEBUG=ON ./.. 
```

- Open `cgcustommath.xcodeproj` in `./build_xcode` by xcode

## Release
### On Mac
```
# Build bundle
$ mkdir release
$ cd release
$ cmake ./..
$ make
```
## Build & Testing

### On Windows
```
# Run script to create msi-file
python3 ./../scripts/windows/build_windows_installer.py
```

### On Mac

```
# Run script to create dmg-file
python3 ./../scripts/mac/create_dmg.py ./
```