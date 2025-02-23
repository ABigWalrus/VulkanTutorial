# set(STB_INCLUDE_DIRS "${CMAKE_CURRENT_LIST_DIR}/stb-master")
# set(GLM_INCLUDE_DIRS "${CMAKE_CURRENT_LIST_DIR}/glm")
# set(TINYOBJLOADER_INCLUDE_DIRS "${CMAKE_CURRENT_LIST_DIR}/tinyobjloader-release")

# include(FetchContent)

add_subdirectory(glfw)
add_subdirectory(glm)

target_include_directories(${PROJECT_NAME} PUBLIC
# include_directories(
	glfw/include
	glm
	stb
	tinyobjloader
)
