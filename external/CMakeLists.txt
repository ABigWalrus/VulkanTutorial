add_subdirectory(glfw)
add_subdirectory(glm)

target_include_directories(${PROJECT_NAME} PUBLIC
	glfw/include
	glm
	stb
	tinyobjloader
)
