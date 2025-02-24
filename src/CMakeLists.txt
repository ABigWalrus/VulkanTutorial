list(APPEND SOURCE_FILES
    main.cpp
)

add_subdirectory(Render)
add_subdirectory(Engine)

add_executable(
	${PROJECT_NAME}
	${SOURCE_FILES}
)

target_include_directories(${PROJECT_NAME} PUBLIC
	src/Render
)

target_include_directories(${PROJECT_NAME} PUBLIC
	src/Engine
)

target_include_directories(${PROJECT_NAME} PUBLIC
	src
)