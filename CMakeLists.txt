cmake_minimum_required(VERSION 3.10)
project(Stockup)

set(HEADER_FILES stock_up.hpp)
set(SOURCE_FILES stock_up.cpp)

add_executable(stockup ${HEADER_FILES} ${SOURCE_FILES} main.cpp)

set_property(TARGET Stockup PROPERTY CXX_STANDARD 17)


if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")
    target_compile_options(Stockup PRIVATE /W4 /permissive-)
    target_compile_options(UnitTestRunner PRIVATE /W4 /permissive-)
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    target_compile_options(Stockup PRIVATE -Wall -Wextra -pedantic)
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "CLANG")
    target_compile_options(Stockup PRIVATE -Wall -Wextra -pedantic)
endif()
