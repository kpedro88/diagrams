# diagrams
Code to generate Feynman diagrams using pyfeyn

This repo uses Python 2.7 and depends on a custom version of [pyfeyn](https://github.com/kpedro88/pyfeyn).

Installation instructions:
```
pip install PyX==0.12.1
pip install git+https://github.com/kpedro88/pyfeyn.git@v1.1.0
```

All drawing classes in the custom version of pyfeyn can be constructed using `kwargs`.
This enables diagrams to be completely specified as Python dictionaries, to reduce code duplication and improve flexibility.

There is a single driver script, [generateDiagram.py](./generateDiagram.py), which interprets an input dictionary to assemble the specified diagram.
```
Options:
  -h, --help                       show this help message and exit
  -d DICTFILE, --dict=DICTFILE     file containing dict w/ diagram components
  -o OUTPUT, --output=OUTPUT       output name for diagram images (default = [dict name]+'_feyn')
  -p PFORMAT, --pformat=PFORMAT    comma-separated list of print formats (default = ['pdf', 'png'])
```
