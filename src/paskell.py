import subprocess, platform, os

def _os_check(path: str) -> str:
    if platform.system() == "Windows":
        return f"{path}.exe" if not path.lower().endswith(".exe") else path

    return "./" + path


def run(path: str, input_data: str = None):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"{path} was not found. Ensure the path is correct and the file exists."
        )

    file = _os_check(path)

    haskell_process = subprocess.Popen(
        [file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
    )

    if input_data:
        haskell_output, _ = haskell_process.communicate(input=input_data)

    haskell_output, _ = haskell_process.communicate()

    if haskell_process.returncode != 0:
        raise subprocess.CalledProcessError(
            haskell_process.returncode,
            f"Error executing '{file}'.\nError code: {haskell_process.returncode}.\nIts advised to lookup error code {haskell_process.returncode} to understand the underlying issue with Paskell's execution of your Haskell file.",
        )

    result = haskell_output.strip()

    return result