#include(./.env.cmake OPTIONAL RESULT_VARIABLE LOCAL_ENV)
#message(STATUS "Local .env.cmake: ${LOCAL_ENV}")

cmake_minimum_required (VERSION 3.16)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
project (BigEngine)
include(FetchContent)
set(CMAKE_CXX_STANDARD 17)
find_package(Vulkan REQUIRED)
find_package(glfw3 REQUIRED)
# set(GLFW_PATH ${PROJECT_SOURCE_DIR}/external/glfw-3.4.bin.WIN64)
# set(GLFW_LIB "${GLFW_PATH}/lib-mingw-w64/libglfw3.a")
# set(GLFW_INCLUDE_DIRS "${GLFW_PATH}/include")

set(VULKAN_INCLUDE_DIRS "${VULKAN_SDK_PATH}/Include")

set(PROJECT_INCLUDE_DIRS "${PROJECT_SOURCE_DIR}/src")

FetchContent_Declare(
	glm
	GIT_REPOSITORY	https://github.com/g-truc/glm.git
	GIT_TAG  master
	GIT_PROGRESS    TRUE
)

FetchContent_MakeAvailable(glm)

file(GLOB_RECURSE SOURCES ${PROJECT_SOURCE_DIR}/src/*.cpp)

add_executable(
	${PROJECT_NAME}
	${SOURCES}
)

add_subdirectory("external")

target_include_directories(${PROJECT_NAME} PUBLIC
	${PROJECT_INCLUDE_DIRS}
	${GLFW_INCLUDE_DIRS}
	${VULKAN_INCLUDE_DIRS}

)
# target_link_directories(${PROJECT_NAME} PUBLIC
# ${Vulkan_LIBRARIES}
# ${GLFW_LIB}
# )
target_link_libraries(${PROJECT_NAME} glfw ${Vulkan_LIBRARIES} glm::glm)
# target_link_libraries(VulkanTutorial ${Vulkan_LIBRARIES} glfw)

find_program(GLSL_VALIDATOR glslangValidator HINTS 
	${Vulkan_GLSLANG_VALIDATOR_EXECUTABLE} 
	/usr/bin 
	/usr/local/bin 
	${VULKAN_SDK_PATH}/Bin
	${VULKAN_SDK_PATH}/Bin32
	$ENV{VULKAN_SDK}/Bin/ 
	$ENV{VULKAN_SDK}/Bin32/
)

set(SHADERS_SOURCE_DIR "${PROJECT_SOURCE_DIR}/assets/shaders")

file(GLOB_RECURSE VERTEX_SHADERS
	"${SHADERS_SOURCE_DIR}/*.vert"
)

file(GLOB_RECURSE FRAGMENT_SHADERS
	"${SHADERS_SOURCE_DIR}/*.frag"
)

foreach(SHADER ${VERTEX_SHADERS})
	set(SPIRV "${SHADERS_SOURCE_DIR}/vert.spv")
	add_custom_command(
		OUTPUT ${SPIRV}
		COMMAND ${GLSL_VALIDATOR} -V ${SHADER} -o ${SPIRV}
		DEPENDS ${SHADER}
	)
	list(APPEND SPIRV_BINARY_FILES ${SPIRV})
endforeach(SHADER)

foreach(SHADER ${FRAGMENT_SHADERS})
	set(SPIRV "${SHADERS_SOURCE_DIR}/frag.spv")
	add_custom_command(
		OUTPUT ${SPIRV}
		COMMAND ${GLSL_VALIDATOR} -V ${SHADER} -o ${SPIRV}
		DEPENDS ${SHADER}
	)
	list(APPEND SPIRV_BINARY_FILES ${SPIRV})
endforeach(SHADER)

add_custom_target(
    default ALL
    DEPENDS ${SPIRV_BINARY_FILES}
)
