cmake_minimum_required(VERSION 3.10)
project(stockup)

set(HEADER_FILES stock_up.hpp)
set(SOURCE_FILES stock_up.cpp)

add_executable(stockup ${HEADER_FILES} ${SOURCE_FILES} main.cpp)
set_property(TARGET stockup PROPERTY CXX_STANDARD 17)


include("${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
conan_basic_setup()

target_link_libraries(stockup ${CONAN_LIBS})


if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")
    target_compile_options(stockup PRIVATE /W4 /permissive-)
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    target_compile_options(stockup PRIVATE -Wall -Wextra -pedantic)
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "CLANG")
    target_compile_options(stockup PRIVATE -Wall -Wextra -pedantic)
endif()
