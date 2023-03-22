# CMAKE with custom library tutorial

## Introduction

This project aims to be tutorial to cmake to create a custom library and a sample application to verify the function

## Prepare build environment

### On Windows

- Visual Studio 2019
- Cmake
- Conan
- Wix Toolset 3.11
- Python 3.10

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

- Install conan

```
$ pip3 install conan
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

- Build

```
$ conan profile detect
$ conan install . --output-folder=build_console --build=missing -s build_type=Release
$ cd ./build_console
$ ./conanbuild.bat
$ cmake .. -DCMAKE_TOOLCHAIN_FILE=./conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release -DEigen3_DIR="$pwd"
$ ./deactivate_conanbuild.bat
$ cmake --build .
```

- Create installer:
```
cd scripts/windows
python3 ./scripts/windows/build_windows_installer.py
```

### On Mac

#### Without xcode

- Build

```
$ conan profile detect
$ conan install . --output-folder=build_console --build=missing -s build_type=Release
$ cd ./build_console
$ . ./conanbuild.sh
$ cmake .. -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release
$ . ./deactivate_conanbuild.sh
$ cmake --build .
```

- Run examples

```
# Run math without parameters
$ /math.app/Contents/MacOS/math
```

#### Build with xcode

- Generate xcode project

```
$ conan install . --output-folder=build_xcode --build=missing -s build_type=Debug
$ cd ./build_xcode
$ . ./conanbuild.sh
$ cmake .. -GXcode -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Debug -DDEBUG=ON
$ . ./deactivate_conanbuild.sh 
```

- Open `cgcustommath.xcodeproj` in `./build_xcode` by xcode

## Release
### On Mac
```
# Build bundle
$ conan profile detect
$ conan install . --output-folder=generate --build=missing -s build_type=Release
$ cd ./generate
$ . ./conanbuild.sh
$ cmake .. -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release
$ . ./deactivate_conanbuild.sh
$ cmake --build .


# Run script to create dmg-file
python3 ./../scripts/mac/create_dmg.py ./
```