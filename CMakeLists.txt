cmake_minimum_required(VERSION 3.0)
project(cgcustommath)

# this depends on eigen3 3.4
find_package(Eigen3 3.4 REQUIRED NO_MODULE)
# find_package(Eigen3 3.4)

set(APP_NAME math)
set(LIB_NAME cgcustommath)

# Enable Hot Reload for MSVC compilers if supported.
if (POLICY CMP0141)
  cmake_policy(SET CMP0141 NEW)
  set(CMAKE_MSVC_DEBUG_INFORMATION_FORMAT "$<IF:$<AND:$<C_COMPILER_ID:MSVC>,$<CXX_COMPILER_ID:MSVC>>,$<$<CONFIG:Debug,RelWithDebInfo>:EditAndContinue>,$<$<CONFIG:Debug,RelWithDebInfo>:ProgramDatabase>>")
endif()

# create test application
if(APPLE)
  if (DEBUG)
    add_executable(${APP_NAME} src/math.cpp 
        include/cgcustommath.hpp 
        src/cgcustommath.cpp)
  else()
    add_executable(${APP_NAME} MACOSX_BUNDLE src/math.cpp 
        include/cgcustommath.hpp 
        src/cgcustommath.cpp)
  endif()
else()
  add_executable(${APP_NAME} src/math.cpp 
      include/cgcustommath.hpp 
      src/cgcustommath.cpp)
endif()

add_library(${LIB_NAME} SHARED 
      include/cgcustommath.hpp 
      src/cgcustommath.cpp
  )

message(EIGEN3_INCLUDE_DIRS="${Eigen3_INCLUDE_DIRS}")
include_directories( ${Eigen3_INCLUDE_DIRS})
include_directories(include)

#install(TARGETS ${APP_NAME} RUNTIME DESTINATION bin COMPONENT apps)
#install(TARGETS ${LIB_NAME} ARCHIVE DESTINATION lib COMPONENT lib)
#install(FILES include/cgcustommath.hpp DESTINATION include COMPONENT devel)

# add CPack to project
set(CPACK_PACKAGE_NAME "Mat")
set(CPACK_PACKAGE_VENDOR "CMake.org")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY
    "Mat - CPack Component Installation Example")
set(CPACK_PACKAGE_VERSION "1.0.0")
set(CPACK_PACKAGE_VERSION_MAJOR "1")
set(CPACK_PACKAGE_VERSION_MINOR "0")
set(CPACK_PACKAGE_VERSION_PATCH "0")
set(CPACK_PACKAGE_INSTALL_DIRECTORY "CPack Component Example")

set(CPACK_COMPONENT_LIB_DISPLAY_NAME "Library")
set(CPACK_COMPONENT_LIB_DESCRIPTION "The library including documentation.")

set(CPACK_COMPONENT_DEVEL_DISPLAY_NAME "Development")
set(CPACK_COMPONENT_DEVEL_DESCRIPTION "Header files for C and C++ required to develop applications.")

set(CPACK_COMPONENT_APPS_DISPLAY_NAME "Applications")
set(CPACK_COMPONENT_APPS_DESCRIPTION "Example mat")

# dependencies between components
set(CPACK_COMPONENT_DEVEL_DEPENDS lib)
set(CPACK_COMPONENT_APPS_DEPENDS lib)
set(CPACK_COMPONENT_LIB_REQUIRED ON) # always install the libs

set(CPACK_COMPONENTS_ALL lib devel apps)

include(CPack)