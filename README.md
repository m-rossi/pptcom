# pptcom
Use Microsoft PowerPoint within Python with the help of COM

## Usage

You can export the slides of a PowerPoint-presentation:
```python
import pptcom

with pptcom.File('presentation.pptx') as pptfile:
    pptfile.export('png')
```

## Development

### Testing

For testing purposes [python-pptx](https://github.com/scanny/python-pptx) is used, after an installation of this package you can test the package with pytest.
