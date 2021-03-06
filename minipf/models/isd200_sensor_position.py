# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from minipf.models.base_model_ import Model
from minipf.models.xyz import XYZ  # noqa: F401,E501
from minipf import util


class ISD200SensorPosition(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, velocities: List[XYZ]=None, unit: str=None, positions: List[XYZ]=None):  # noqa: E501
        """ISD200SensorPosition - a model defined in OpenAPI

        :param velocities: The velocities of this ISD200SensorPosition.  # noqa: E501
        :type velocities: List[XYZ]
        :param unit: The unit of this ISD200SensorPosition.  # noqa: E501
        :type unit: str
        :param positions: The positions of this ISD200SensorPosition.  # noqa: E501
        :type positions: List[XYZ]
        """
        self.openapi_types = {
            'velocities': List[XYZ],
            'unit': str,
            'positions': List[XYZ]
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
    def from_dict(cls, dikt) -> 'ISD200SensorPosition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ISD200_sensor_position of this ISD200SensorPosition.  # noqa: E501
        :rtype: ISD200SensorPosition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def velocities(self) -> List[XYZ]:
        """Gets the velocities of this ISD200SensorPosition.


        :return: The velocities of this ISD200SensorPosition.
        :rtype: List[XYZ]
        """
        return self._velocities

    @velocities.setter
    def velocities(self, velocities: List[XYZ]):
        """Sets the velocities of this ISD200SensorPosition.


        :param velocities: The velocities of this ISD200SensorPosition.
        :type velocities: List[XYZ]
        """

        self._velocities = velocities

    @property
    def unit(self) -> str:
        """Gets the unit of this ISD200SensorPosition.


        :return: The unit of this ISD200SensorPosition.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit: str):
        """Sets the unit of this ISD200SensorPosition.


        :param unit: The unit of this ISD200SensorPosition.
        :type unit: str
        """

        self._unit = unit

    @property
    def positions(self) -> List[XYZ]:
        """Gets the positions of this ISD200SensorPosition.


        :return: The positions of this ISD200SensorPosition.
        :rtype: List[XYZ]
        """
        return self._positions

    @positions.setter
    def positions(self, positions: List[XYZ]):
        """Sets the positions of this ISD200SensorPosition.


        :param positions: The positions of this ISD200SensorPosition.
        :type positions: List[XYZ]
        """

        self._positions = positions
