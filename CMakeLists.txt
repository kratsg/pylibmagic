cmake_minimum_required (VERSION 3.15)

project(pylibmagic VERSION 0.2.0 DESCRIPTION "Library for compiling libmagic using CMake.")

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_MACOSX_RPATH 1)
if (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    set(CMAKE_C_FLAGS "-arch x86_64 -arch arm64")
endif()

set(libmagic_PREFIX libmagic)
set(libmagic_INSTALL_PREFIX ${pylibmagic_BINARY_DIR}/${libmagic_PREFIX}/src/${libmagic_PREFIX}-install)

include(GNUInstallDirs)
include(ExternalProject)
ExternalProject_Add(libmagic
    GIT_REPOSITORY https://github.com/kratsg/file.git
    GIT_TAG feat/cmakelists
    PREFIX ${libmagic_PREFIX}
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX:PATH=<INSTALL_DIR> -DCMAKE_C_FLAGS=${CMAKE_C_FLAGS}
)

if(SKBUILD)
  message(STATUS "The project is built using scikit-build")

  # install libmagic libraries
  install(DIRECTORY ${PROJECT_BINARY_DIR}/${libmagic_PREFIX}/${CMAKE_INSTALL_LIBDIR} DESTINATION .)
endif()
