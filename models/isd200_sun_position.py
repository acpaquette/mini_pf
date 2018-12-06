# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mini_pf.models.base_model_ import Model
from mini_pf.models.xyz import XYZ  # noqa: F401,E501
from mini_pf import util


class ISD200SunPosition(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, velocities: XYZ=None, unit: str=None, positions: XYZ=None):  # noqa: E501
        """ISD200SunPosition - a model defined in OpenAPI

        :param velocities: The velocities of this ISD200SunPosition.  # noqa: E501
        :type velocities: XYZ
        :param unit: The unit of this ISD200SunPosition.  # noqa: E501
        :type unit: str
        :param positions: The positions of this ISD200SunPosition.  # noqa: E501
        :type positions: XYZ
        """
        self.openapi_types = {
            'velocities': XYZ,
            'unit': str,
            'positions': XYZ
        }

        self.attribute_map = {
            'velocities': 'velocities',
            'unit': 'unit',
            'positions': 'positions'
        }

        self._velocities = velocities
        self._unit = unit
        self._positions = positions

    @classmethod
    def from_dict(cls, dikt) -> 'ISD200SunPosition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ISD200_sun_position of this ISD200SunPosition.  # noqa: E501
        :rtype: ISD200SunPosition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def velocities(self) -> XYZ:
        """Gets the velocities of this ISD200SunPosition.


        :return: The velocities of this ISD200SunPosition.
        :rtype: XYZ
        """
        return self._velocities

    @velocities.setter
    def velocities(self, velocities: XYZ):
        """Sets the velocities of this ISD200SunPosition.


        :param velocities: The velocities of this ISD200SunPosition.
        :type velocities: XYZ
        """

        self._velocities = velocities

    @property
    def unit(self) -> str:
        """Gets the unit of this ISD200SunPosition.


        :return: The unit of this ISD200SunPosition.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit: str):
        """Sets the unit of this ISD200SunPosition.


        :param unit: The unit of this ISD200SunPosition.
        :type unit: str
        """

        self._unit = unit

    @property
    def positions(self) -> XYZ:
        """Gets the positions of this ISD200SunPosition.


        :return: The positions of this ISD200SunPosition.
        :rtype: XYZ
        """
        return self._positions

    @positions.setter
    def positions(self, positions: XYZ):
        """Sets the positions of this ISD200SunPosition.


        :param positions: The positions of this ISD200SunPosition.
        :type positions: XYZ
        """

        self._positions = positions
