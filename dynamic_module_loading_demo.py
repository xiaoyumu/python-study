import importlib
import os


def import_function_module(name, package=None):
    try:
        mo = importlib.import_module(name, package=package)
        return mo
    except:
        return None


def write_module_function(file_path, script):
    with open(file_path, "wt", encoding="utf-8") as file:
        file.write(script)
        file.close()


def ensure_module_package_exists(package_path):
    if not os.path.exists(package_path):
        os.mkdir(package_path)


if __name__ == "__main__":
    script_content = \
        """import os
def execute(**kwargs):
    return f"Hello {kwargs['name']} from {os.name}"
"""
    package_name = "modules"
    ensure_module_package_exists(f"./{package_name}")
    module_name = "test_module_a"

    # Save script to local store (in a specific module folder)
    write_module_function(f"./{package_name}/{module_name}.py", script_content)

    # Import the function module
    mo = import_function_module(f".{module_name}", package_name)
    if mo is not None:
        print(mo)
        # Invoke the function in imported module
        result = mo.execute(name="fish")
        print(result)
