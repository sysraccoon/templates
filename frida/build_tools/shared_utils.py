from pathlib import Path

BASE_PATH = Path(__file__).parent.parent.relative_to(Path.cwd())
SRC_PATH = BASE_PATH / Path("src")
BUILD_PATH = BASE_PATH / Path("build")
BUILD_PATH.mkdir(exist_ok=True)


def get_scripts_build_map():
    result = {}
    ts_scripts = SRC_PATH.glob("*.ts")
    
    for script_path in ts_scripts:
        out_path = BUILD_PATH / Path(script_path.name).with_suffix(".js")
        result[script_path] = out_path
    
    return result
