from cx_Freeze import Executable, setup

version = "1.0.0"

setup(
    name="CIMS-SERVER",
    version=version,
    description="Cloud Infrastructure Management System Server",
    executables=[Executable("main.py")],
)
