from glob import glob
import os

import numpy as np
import pvl
import spiceypy as spice

from minipf.util import get_metakernels
from minipf.drivers.base import LineScanner
from minipf.drivers.distortion import RadialDistortion

class LRO_LROC(LineScanner, RadialDistortion):

    @property
    def metakernel(self):
        metakernels = get_metakernels(years=self.start_time.year, missions='lro', versions='latest')
        self._metakernel = metakernels['data'][0]['path']
        return self._metakernel

    @property
    def instrument_id(self):
        """
        Ignores Wide Angle for now
        """

        instrument = self.label.get("INSTRUMENT_ID")

        # should be left or right
        frame_id = self.label.get("FRAME_ID")

        if instrument == "LROC" and frame_id == "LEFT":
            return "LRO_LROCNACL"
        elif instrument == "LROC" and frame_id == "RIGHT":
            return "LRO_LROCNACR"

    @property
    def spacecraft_name(self):
        return "LRO"
