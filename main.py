from pylibCZIrw import czi as pyczi
from matplotlib import pyplot as plt
from matplotlib import colormaps as cm
from pathlib import Path
from typing import List, Tuple
import time
import argparse


def list_files_with_format(directory, file_extension) -> List[Tuple[str, str]]:
    return [
        (file.name.split(".czi")[0], str(file.resolve()))
        for file in Path(directory).glob(f"*{file_extension}")
    ]


def parse_args() -> Tuple[str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", required=True, type=Path, help="CZI folder directory."
    )
    parser.add_argument(
        "--output", required=True, type=Path, help="PNG folder directory."
    )
    args = parser.parse_args()

    if not args.input.exists():
        print(f"The input path '{args.input}' doesn't exist!")
        exit()

    if not args.input.is_dir():
        print(f"The input path '{args.input}' is not a directory!")
        exit()

    args.output.mkdir(parents=True, exist_ok=True)
    return str(args.input), str(args.output)


def process_files(input_directory: str, output_directory: str) -> None:
    files = list_files_with_format(directory=input_directory, file_extension=".czi")
    print(f"\nProcessing {len(files)} CZI files!")
    print("-----")

    for file_name, file_path in files:
        print(f"Processing {file_name}")
        with pyczi.open_czi(file_path) as czidoc:
            frame = czidoc.read()

        plt.figure(figsize=(12, 12))
        plt.imshow(frame[..., 0], cmap=cm["grey"], vmin=1)
        plt.xticks([])
        plt.yticks([])
        for spine in plt.gca().spines.values():
            spine.set_visible(False)

        plt.savefig(
            f"{output_directory}/{file_name}.png",
            format="png",
            dpi=300,
            bbox_inches="tight",
            pad_inches=0,
        )
        plt.close()


if __name__ == "__main__":
    start_time = time.perf_counter()

    input_directory, output_directory = parse_args()
    process_files(input_directory, output_directory)

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    print("-----")
    print(f"Processing completed in {execution_time:.2f} seconds!")
