cmake_minimum_required (VERSION 3.15)

project(pylibmagic DESCRIPTION "Library for compiling libmagic using CMake.")

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_MACOSX_RPATH 1)

include(GNUInstallDirs)
include(ExternalProject)
ExternalProject_Add(libmagic
    GIT_REPOSITORY https://github.com/file/file.git
    GIT_TAG FILE5_41
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/libmagic
    BUILD_IN_SOURCE 1
    CONFIGURE_COMMAND cd <SOURCE_DIR> && autoreconf -f -i && ./configure --prefix=<INSTALL_DIR>
    BUILD_COMMAND ${MAKE_EXE}
    INSTALL_COMMAND ${MAKE_EXE}
)

if(SKBUILD)
  message(STATUS "The project is built using scikit-build")

  install(DIRECTORY
    ${pylibmagic_BINARY_DIR}/libmagic-prefix/lib/
    DESTINATION .)
endif()
