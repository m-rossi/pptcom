# pptcom
Use Microsoft PowerPoint within Python with the help of COM

## Usage

You can export the slides of a PowerPoint-presentation:
```python
import pptcom

with pptcom.File('presentation.pptx') as pptfile:
    pptfile.export('png')
```

