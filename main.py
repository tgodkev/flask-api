import os
from gui_app import run_gui

def main():
    pid = os.fork()

    if pid == 0:
        # Child process - runs the Flask app
        os.system("python api.py")
    else:
        # Parent process - runs the Tkinter app
        run_gui()
        os.wait()

if __name__ == "__main__":
    main()
