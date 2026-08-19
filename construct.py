import sys
import os
import site

'''
Create a program called construct.py that:
• Detects whether it is running inside a virtual environment
• Displays information about the current Python environment
• Provides instructions for creating and activating a virtual environment if
none is detected
• Shows the difference between global and virtual environment package locations
'''


def is_virtual() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if is_virtual():
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment:", os.path.basename(sys.prefix))
        print("\nSUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting the global system.")
        print("\nPackage installation path:", site.getsitepackages()[0])
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!\n"
              "The machines can see everything you install.\n")
        print("To enter the construct, run:\n"
              "python3 -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              r"matrix_env\Scripts\activate # On Windows"
              "\n\nThen run this program again.")


if __name__ == "__main__":
    main()
