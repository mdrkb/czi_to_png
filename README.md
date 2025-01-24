# CZI to PNG Converter

[![Dependencies](https://img.shields.io/badge/Python-3.11.0-red.svg)]()
[![Dependencies](https://img.shields.io/badge/pylibCZIrw-4.1.3-green.svg)]()
[![Dependencies](https://img.shields.io/badge/Matplotlib-3.10.0-blue.svg)]()

A python program to convert CZI image to PNG image. The program reads CZI images from a given input directory, processes them and finally writes the PNG images into a given output directory.


## Installation

- Clone the repo and navigate into the directory `czi_to_png`.

- Create virtual envrionment:
```
python -m venv .venv 
```

- Activate virtual environment:
```
.\.venv\Scripts\activate
```

- Install dependencies using pip:
```
pip install -r .\requirements.txt
```


## Run

- Navigate into the directory `czi_to_png`.

- Activate virtual environment:
```
.\.venv\Scripts\activate
```

- Run the program by passing the absolute path of input and output directory:
```
python .\main.py --input "input_directory" --output "output_directory"
```
