import os

while(True):
    name = input("Enter package name: ")
    if name == 'quit':
        exit()
    def install_package():
        os.system(" yum install " + name)

    install_package()
