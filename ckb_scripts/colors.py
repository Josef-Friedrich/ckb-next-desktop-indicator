import time
import webcolors

from .ckbpipe import CKBPipe


colors: dict[str, str] = {**webcolors.CSS21_NAMES_TO_HEX, **webcolors.CSS3_NAMES_TO_HEX}


def print_colors() -> None:
    for color, _ in colors.items():
        print(color)

def set_colors(pipe: CKBPipe) -> None:

    for color, rgb in colors.items():
        print(color)
        pipe.set_rgb(rgb)
        time.sleep(1)