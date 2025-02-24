#include <string>
#include <chrono>
#include <iostream>

#include "app.hpp"
#include "render.hpp"
#include "window.hpp"

Application::Application(){
    init();
}

Application::~Application(){
    cleanup();
}

void Application::run(){
    while (window.isOpen()) {
        glfwPollEvents();
        renderer.render();
    }
}

void Application::init(){
    // renderer.init(window.getWindow(), window.getWidth(), window.getWidth());   
}


void Application::cleanup(){
    // renderer.cleanup();
}