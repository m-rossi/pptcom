# pptcom

[![PyPi Version](https://img.shields.io/pypi/v/pptcom.svg)](https://pypi.python.org/pypi/pptcom)
[![Conda Version](https://img.shields.io/conda/vn/mrossi/pptcom.svg)](https://anaconda.org/mrossi/pptcom)

Use Microsoft PowerPoint within Python with the help of COM

## Installation

```
pip install pptcom
```

```
conda install -c mrossi pptcom
```

## Usage

You can export the slides of a PowerPoint-presentation:
```python
import pptcom

with pptcom.File('presentation.pptx') as pptfile:
    pptfile.export('png')
```

## Development

### Building

It is recommended to use [conda-build](https://github.com/conda/conda-build) for building the package. Due to the required packages for testing you need to execute the follwing command inside the repository folder to successfully build the package:
```
conda-build conda.recipe conda.recipe -c defaults -c conda-forge
```

### Testing

For testing purposes [python-pptx](https://github.com/scanny/python-pptx) is used, after an installation of this package you can test the package with pytest.
