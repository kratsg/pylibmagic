cmake_minimum_required (VERSION 3.15)

project(pylibmagic DESCRIPTION "Library for compiling libmagic using CMake.")
if(SKBUILD)
  find_package(PythonExtensions REQUIRED)
  message(STATUS "The project is built using scikit-build")
endif()


set(CMAKE_CXX_STANDARD 11)
set(CMAKE_MACOSX_RPATH 1)

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
  install(TARGETS libmagic LIBRARY DESTINATION pylibmagic)
endif()

#SET(FXCM_INCLUDE_DIR ${CMAKE_CURRENT_BINARY_DIR}/3rd_party/src/ForexConnectDownload/include)
#SET(FXCM_LIB_DIR ${CMAKE_CURRENT_BINARY_DIR}/3rd_party/src/ForexConnectDownload/lib)


#add_library(ForexConnect SHARED IMPORTED)
#set_target_properties(ForexConnect PROPERTIES IMPORTED_LOCATION ${FXCM_LIB_DIR}/libForexConnect.so)
#
#include_directories(${FXCM_INCLUDE_DIR})
#add_executable(syncDatabase syncDatabase.cpp trader/database.cpp trader/fxcm.cpp)
#target_link_libraries(syncDatabase ForexConnect)
#add_dependencies(syncDatabase ForexConnectDownload)

