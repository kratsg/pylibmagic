cmake_minimum_required (VERSION 3.15)

project(pylibmagic DESCRIPTION "Library for compiling libmagic using CMake.")
if(SKBUILD)
  find_package(PythonExtensions REQUIRED)
  message(STATUS "The project is built using scikit-build")
endif()


set(CMAKE_CXX_STANDARD 11)
set(CMAKE_MACOSX_RPATH 1)

include(ExternalProject)
ExternalProject_Add(_libmagic
    GIT_REPOSITORY https://github.com/file/file.git
    GIT_TAG FILE5_41
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/libmagic
    BUILD_IN_SOURCE 1
    CONFIGURE_COMMAND cd <SOURCE_DIR> && autoreconf -f -i && ./configure --prefix=<INSTALL_DIR>
    BUILD_COMMAND ${MAKE_EXE}
    INSTALL_COMMAND ${MAKE_EXE}
)

if(SKBUILD)
  add_library(libmagic SHARED IMPORTED GLOBAL)
  set_target_properties(libmagic
    PROPERTIES IMPORTED_LOCATION
      ${_libmagic_INSTALL_DIR}/libmagic-prefix/lib/libmagic.so.1.0.0
      ${_libmagic_INSTALL_DIR}/libmagic-prefix/lib/libmagic.so.1
      ${_libmagic_INSTALL_DIR}/libmagic-prefix/lib/libmagic.so
  )

  install(TARGETS libmagic LIBRARY DESTINATION pylibmagic)
endif()
