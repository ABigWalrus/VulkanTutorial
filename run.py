import sys
import subprocess
import os


def main():
    mode = 'DEFAULT'
    project_name = 'BigEngine'
    command = []

    if sys.argv[1] == 'cmake':
        mode = 'CMAKE'
        if not os.path.exists('./cmake-build-debug'):
            os.mkdir('cmake-build-debug')
        command.append('cmake')
        command.append('-S .')
        command.append('-B ./cmake-build-debug')
        command.append('-G Ninja')
        command.append('-D GLFW_BUILD_X11=1')
        command.append('-D GLFW_BUILD_WAYLAND=0')
        command.append('DCMAKE_EXPORT_COMPILE_COMMANDS')
    elif sys.argv[1] == 'build':
        mode = 'BUILD'
        command.append('cmake')
        command.append('--build')
        command.append('./build-debug')
        command.append('-j 12')
    else:
        print('UNKNOWN MODE')
        return
    print(f"Running in {mode}")
    # print(command)
    subprocess.run(command)
    # subprocess.run(['touch', 'CMakeLists.txt'])
    # subprocess.run(['cmake', '--build', './build-debug', '-j 12'])
    if mode == 'BUILD':
        subprocess.run(['./cmake-build-debug/' + project_name])


if __name__ == '__main__':
    main()
