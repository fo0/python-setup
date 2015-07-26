import sys
from cx_Freeze import setup, Executable

setup(
    name = "ZipCracker",
    version = "1.1",
    description = "ZipCracker",
    executables = [Executable("ZipCracker.py", base = "Win32GUI")])
