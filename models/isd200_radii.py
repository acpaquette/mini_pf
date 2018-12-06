# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mini_pf.models.base_model_ import Model
from mini_pf import util


class ISD200Radii(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, semimajor: float=None, semiminor: float=None, unit: str=None):  # noqa: E501
        """ISD200Radii - a model defined in OpenAPI

        :param semimajor: The semimajor of this ISD200Radii.  # noqa: E501
        :type semimajor: float
        :param semiminor: The semiminor of this ISD200Radii.  # noqa: E501
        :type semiminor: float
        :param unit: The unit of this ISD200Radii.  # noqa: E501
        :type unit: str
        """
        self.openapi_types = {
            'semimajor': float,
            'semiminor': float,
            'unit': str
        }

        self.attribute_map = {
            'semimajor': 'semimajor',
            'semiminor': 'semiminor',
            'unit': 'unit'
        }

        self._semimajor = semimajor
        self._semiminor = semiminor
        self._unit = unit

    @classmethod
    def from_dict(cls, dikt) -> 'ISD200Radii':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ISD200_radii of this ISD200Radii.  # noqa: E501
        :rtype: ISD200Radii
        """
        return util.deserialize_model(dikt, cls)

    @property
    def semimajor(self) -> float:
        """Gets the semimajor of this ISD200Radii.


        :return: The semimajor of this ISD200Radii.
        :rtype: float
        """
        return self._semimajor

    @semimajor.setter
    def semimajor(self, semimajor: float):
        """Sets the semimajor of this ISD200Radii.


        :param semimajor: The semimajor of this ISD200Radii.
        :type semimajor: float
        """
        if semimajor is None:
            raise ValueError("Invalid value for `semimajor`, must not be `None`")  # noqa: E501

        self._semimajor = semimajor

    @property
    def semiminor(self) -> float:
        """Gets the semiminor of this ISD200Radii.


        :return: The semiminor of this ISD200Radii.
        :rtype: float
        """
        return self._semiminor

    @semiminor.setter
    def semiminor(self, semiminor: float):
        """Sets the semiminor of this ISD200Radii.


        :param semiminor: The semiminor of this ISD200Radii.
        :type semiminor: float
        """

        self._semiminor = semiminor

    @property
    def unit(self) -> str:
        """Gets the unit of this ISD200Radii.


        :return: The unit of this ISD200Radii.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit: str):
        """Sets the unit of this ISD200Radii.


        :param unit: The unit of this ISD200Radii.
        :type unit: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit
