cmake_minimum_required(VERSION 3.10)

project(otb2zcfg)

cmake_policy(SET CMP0072 NEW)
set(OpenGL_GL_PREFERENCE GLVND)

find_package(Boost 1.65.0 COMPONENTS serialization filesystem REQUIRED)
find_package(OTB REQUIRED)
find_package(OpenGL REQUIRED)
if(OTB_FOUND)
  include(${OTB_USE_FILE})
else(OTB_FOUND)
  message(FATAL_ERROR "Cannot build OTB project without OTB.  Please set OTB_DIR.")
endif(OTB_FOUND)

ADD_EXECUTABLE(otb2zcfg otb2zcfg.cxx)
TARGET_LINK_LIBRARIES(otb2zcfg ${OTB_LIBRARIES} ${Boost_LIBRARIES})
