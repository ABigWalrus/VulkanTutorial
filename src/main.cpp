#include "Engine/app.hpp"
#include <iostream>
#include <stdexcept>
#include <cstdlib>

int main() {

    Application app1;
    try {
        // app1.init();
        app1.run();
        // app1.cleanup();
    }
    catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}