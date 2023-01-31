# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
"""
utils/initialization
"""

from pathlib import Path
import os
import sys

# WINDOWS
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(FILE.parents[0])  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative
print("ROOT", ROOT)
print("FILE", FILE)
print("PARENT", FILE.parents[0])

# UBUNTU
sys.path.append("/deepsort-yolov5/yolov5")
sys.path.append("/deepsort-yolov5/yolov5/utils")
print("sys_path", sys.path)


def notebook_init(verbose=True):
    # Check system software and hardware
    print('Checking setup...')

    import os
    import shutil

    from utils.general import check_requirements, emojis, is_colab
    from utils.torch_utils import select_device  # imports

    check_requirements(('psutil', 'IPython'))
    import psutil
    from IPython import display  # to display images and clear console output

    if is_colab():
        shutil.rmtree('/content/sample_data', ignore_errors=True)  # remove colab /sample_data directory

    if verbose:
        # System info
        # gb = 1 / 1000 ** 3  # bytes to GB
        gib = 1 / 1024 ** 3  # bytes to GiB
        ram = psutil.virtual_memory().total
        total, used, free = shutil.disk_usage("/")
        display.clear_output()
        s = f'({os.cpu_count()} CPUs, {ram * gib:.1f} GB RAM, {(total - free) * gib:.1f}/{total * gib:.1f} GB disk)'
    else:
        s = ''

    select_device(newline=False)
    print(emojis(f'Setup complete ✅ {s}'))
    return display
