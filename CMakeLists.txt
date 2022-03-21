cmake_minimum_required (VERSION 3.15)

project(pylibmagic VERSION 0.1.0 DESCRIPTION "Library for compiling libmagic using CMake.")

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_MACOSX_RPATH 1)

set(libmagic_PREFIX libmagic)

include(GNUInstallDirs)
include(ExternalProject)
ExternalProject_Add(libmagic
    GIT_REPOSITORY https://github.com/file/file.git
    GIT_TAG FILE5_41
    PREFIX ${libmagic_PREFIX}
    BUILD_IN_SOURCE 1
    CONFIGURE_COMMAND autoreconf -f -i && ./configure --prefix=<INSTALL_DIR> --libdir=<INSTALL_DIR>/${CMAKE_INSTALL_LIBDIR} --datadir=<INSTALL_DIR>/${CMAKE_INSTALL_DATADIR}
    BUILD_COMMAND ${MAKE_EXE}
    INSTALL_COMMAND ${MAKE_EXE}
)

if(SKBUILD)
  message(STATUS "The project is built using scikit-build")

  # install libmagic libraries
  install(DIRECTORY
    ${pylibmagic_BINARY_DIR}/${libmagic_PREFIX}/${CMAKE_INSTALL_LIBDIR}/
    DESTINATION .
  )
  # Note: ./configure has pkgdatadir hardcoded as '$(datadir)/misc'
  install(FILES
    ${pylibmagic_BINARY_DIR}/${libmagic_PREFIX}/${CMAKE_INSTALL_DATADIR}/misc/magic.mgc
    DESTINATION .
  )
endif()
