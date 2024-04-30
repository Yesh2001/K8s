import subprocess

def install_python():
    # Unpack the source distribution
    subprocess.run(["tar", "xf", "python-3.11.8.tgz"], check=True)

    # Change the working directory
    subprocess.run(["cd", "python-3.11.8"], check=True, shell=True)

    # Run the configure script
    subprocess.run(["./configure"], check=True, shell=True)

    # Compile and install
    subprocess.run(["make"], check=True, shell=True)
    subprocess.run(["make", "install"], check=True, shell=True)

if __name__ == "__main__":
    install_python()
