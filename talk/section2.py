"""
        ███████  █████  ██████  ██████
           ███  ██   ██ ██   ██ ██   ██
          ███   ███████ ██████  ██████
         ███    ██   ██ ██   ██ ██   ██
        ███████ ██   ██ ██   ██ ██   ██
"""

# Q: What is Zarr? #
# A: Zarr is a format for the storage of chunked, compressed, N-dimensional arrays. #





##
import zarr
z = zarr.zeros((10000, 10000), chunks=(1000, 1000), dtype='i4')


##
import numpy as np
z[:] = 123
z[3, :] = np.arange(10000)
z[:, 3] = np.arange(10000)


##
from talk import DATA_DIR
zarr.save(DATA_DIR / "example.zarr", z)
arr = zarr.load(DATA_DIR / "example.zarr")
z1 = zarr.open(DATA_DIR / "example.zarr")
# let's have a look at the structure



##
# so basically: a zarr array is an .zarray definition and a lot of chunks
import json
store = {
    ".zarray": json.dumps({
        "chunks": [5],
        "compressor": None,
        "dtype": "u1",
        "fill_value": 255,
        "order": "C",
        "filters": None,
        "shape": [25],
        "zarr_format": 2,
    }),
    "0": b"\x00\x01\x02\x03\x04",
    "1": b"\x10\x11\x12\x13\x14",
    "2": b"\x20\x21\x22\x23\x24",
    "3": b"\x30\x31\x32\x33\x34",
}


##
from zarr.storage import KVStore
zstore = KVStore(store)

z2 = zarr.open(zstore)


##
import fsspec

fs = fsspec.filesystem(
    "github",
    org="ap--",
    repo="teaching-python-cvcm-adv-oct-2022"
)
# fs.ls()


##
m = fs.get_mapper("data/z2.zarr")
z3 = zarr.open_array(m)
# loaded directly from GitHub!


##
import tiffslide

ts0 = tiffslide.open_slide(
    "https://openslide.cs.cmu.edu/download/openslide-testdata/Aperio/CMU-1.svs"
)


##
from tiffslide import TiffSlide

ts1 = TiffSlide(
    "s3://tcga-2-open/8d197e5d-fb39-4d40-977b-a96954a7c7bc/TCGA-NF-A4X2-01Z-00-DX1.B09588B4-FBD3-4CED-9E88-6D018F0B5098.svs",
    storage_options={"anon": True},
)

