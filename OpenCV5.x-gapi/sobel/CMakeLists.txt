# project(sobel)

# add_executable(${PROJECT_NAME} main.cpp)
# target_link_libraries(${PROJECT_NAME} PRIVATE CONAN_PKG::opencv)
# set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 11)

# install(TARGETS ${PROJECT_NAME} RUNTIME DESTINATION bin)
cmake_minimum_required(VERSION 3.1)
# Define project name
project(demo) #//项目名称
set(CMAKE_CXX_STANDARD 11)  #//c++版本



# Find OpenCV, you may need to set OpenCV_DIR variable
# to the absolute path to the directory containing OpenCVConfig.cmake file
# via the command line or GUI
find_package(OpenCV 5 REQUIRED)




# If the package has been found, several variables will
# be set, you can find the full list with descriptions
# in the OpenCVConfig.cmake file.
# Print some message showing some of them
message(STATUS "OpenCV library status:")
message(STATUS "    config: ${OpenCV_DIR}")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")




# Declare the executable target built from your sources
add_executable(demo main.cpp)  #demo_Serial  demo_Parallel

# Link your application with OpenCV libraries
target_link_libraries(demo PRIVATE ${OpenCV_LIBS}) 
# target_link_libraries(demo PRIVATE ${OpenCV_LIBS} m -lpthread -lOpenCL)