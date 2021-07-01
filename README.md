# napari-ytschema

[![License](https://img.shields.io/pypi/l/napari-ytschema.svg?color=green)](https://github.com/chrishavlin/napari-ytschema/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-ytschema.svg?color=green)](https://pypi.org/project/napari-ytschema)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-ytschema.svg?color=green)](https://python.org)
[![tests](https://github.com/chrishavlin/napari-ytschema/workflows/tests/badge.svg)](https://github.com/chrishavlin/napari-ytschema/actions)
[![codecov](https://codecov.io/gh/chrishavlin/napari-ytschema/branch/master/graph/badge.svg)](https://codecov.io/gh/chrishavlin/napari-ytschema)

test of a schema based loader for use with https://github.com/data-exp-lab/analysis_schema 

### temporary usage instructions:


This plugin currently relies on an experiment PR to the analysis_schema repo: https://github.com/data-exp-lab/analysis_schema/pull/5 which adds a convenience class that to easily return a 3D ndarray sampling of a dataset.  

here's a sample of a json that can be loaded into napari with this plugin:

```
{
    "$schema": "./yt_analysis_schema.json",
    "Plot": [
    {
      "ProjectionPlot": {
        "Dataset": {
          "FileName": "IsolatedGalaxy/galaxy0030/galaxy0030"
        },
        "Axis":"y",
        "FieldNames": {
          "field": "density"
        },
        "DataSource":{
          "Center": [0.5, 0.5, 0.5],
          "Radius": 0.1
        }
      },
      "Napari": {
        "Dataset": {
          "FileName": "IsolatedGalaxy/galaxy0030/galaxy0030"
        },
        "Field": {
          "field": "enzo,Density"
        },
        "left_edge": [0.45, 0.45, 0.45],
        "right_edge": [0.55, 0.55, 0.55],
        "resolution": [500, 500, 500],
        "take_log": 1
      }
    }
  ]
}
```

The plugin looks specifically for the `yt_analysis_schema` schema version and a `["Plot"]["Napari"]` property. Other properties are ignored. 



----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Installation

### Local installation (works): 

analysis_schema manual install of PR: https://github.com/data-exp-lab/analysis_schema/pull/5
clone this repo, then `pip install .` (or `pip install -e .` if you want to continue the experiment!)


### general installation (does not work)

You can install `napari-ytschema` via [pip]:

    pip install napari-ytschema

## Usage 

after installing the plugin, from the napari gui (which you can start with `$ napari` for a terminal) click `File --> Open` and select a validated json (the source code contains the above sample json: `napari_ytschema/test_json.json`). This will use the `analysis_schema` repo to parse the json, instantiate the necessary yt objects and return a 3D sampling of the dataset and specified field. 

Can also load the file from a jupyter notebook with 

```
%gui qt5
import napari
v = napari.Viewer()
v.open('/path/to/validated/json/test_json.json')
```

which should spawn a napari GUI and load the image data. Full [example nb here](https://github.com/chrishavlin/yt_scratch/blob/master/notebooks/test_napari_plugin.ipynb).

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-ytschema" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
[file an issue]: https://github.com/chrishavlin/napari-ytschema/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
