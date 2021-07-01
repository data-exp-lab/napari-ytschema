"""
This module is an example of a barebones numpy reader plugin for napari.

It implements the ``napari_get_reader`` hook specification, (to create
a reader plugin) but your plugin may choose to implement any of the hook
specifications offered by napari.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below accordingly.  For complete documentation see:
https://napari.org/docs/dev/plugins/for_plugin_developers.html
"""
import numpy as np
from napari_plugin_engine import napari_hook_implementation
from analysis_schema import ytModel
import json

@napari_hook_implementation
def napari_get_reader(path):
    """A basic implementation of the napari_get_reader hook specification.

    Parameters
    ----------
    path : str or list of str
        Path to file, or list of paths.

    Returns
    -------
    function or None
        If the path is a recognized format, return a function that accepts the
        same path or list of paths, and returns a list of layer data tuples.
    """
    if isinstance(path, list):
        # reader plugins may be handed single path, or a list of paths.
        # if it is a list, it is assumed to be an image stack...
        # so we are only going to look at the first file.
        path = path[0]

    # if we know we cannot read the file, we immediately return None.
    if not path.endswith(".json"):
        return None

    with open(path, "r") as jhandle:
        schema_raw = json.load(jhandle)
        schema_version = schema_raw.get("$schema", None)

    if schema_version is None or "yt_analysis_schema" not in schema_version:
        return None

    # check the action here
    Plots = schema_raw.get('Plot',None)
    if Plots is None:
        return None

    if sum(['Napari' in p for p in Plots]):
        print("YESSSSSSSSSSSSSS")
        return reader_function

    print("NOOOOOOOOOOOOOOOOO")

    return None


def reader_function(path):
    """Take a path or list of paths and return a list of LayerData tuples.

    Readers are expected to return data as a list of tuples, where each tuple
    is (data, [add_kwargs, [layer_type]]), "add_kwargs" and "layer_type" are
    both optional.

    Parameters
    ----------
    path : str or list of str
        Path to file, or list of paths.

    Returns
    -------
    layer_data : list of tuples
        A list of LayerData tuples where each tuple in the list contains
        (data, metadata, layer_type), where data is a numpy array, metadata is
        a dict of keyword arguments for the corresponding viewer.add_* method
        in napari, and layer_type is a lower-case string naming the type of layer.
        Both "meta", and "layer_type" are optional. napari will default to
        layer_type=="image" if not provided
    """
    # handle both a string and a list of strings
    if not isinstance(path, str):
        raise NotImplementedError("schema loader can only load a single path for now")

    schema_model = ytModel.parse_file(path)

    data = None
    for p in schema_model.Plot:
        if p.Napari and data is None:
            data = p.Napari._run(napari=True)

    # optional kwargs for the corresponding viewer.add_* method
    add_kwargs = {}

    layer_type = "image"  # optional, default is "image"
    return [(data, add_kwargs, layer_type)]
