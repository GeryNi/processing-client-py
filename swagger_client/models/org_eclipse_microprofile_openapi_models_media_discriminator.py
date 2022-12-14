# coding: utf-8

"""


    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OrgEclipseMicroprofileOpenapiModelsMediaDiscriminator(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'mapping': 'list[object]',
        'property_name': 'str'
    }

    attribute_map = {
        'mapping': 'mapping',
        'property_name': 'propertyName'
    }

    def __init__(self, mapping=None, property_name=None):  # noqa: E501
        """OrgEclipseMicroprofileOpenapiModelsMediaDiscriminator - a model defined in Swagger"""  # noqa: E501
        self._mapping = None
        self._property_name = None
        self.discriminator = None
        if mapping is not None:
            self.mapping = mapping
        if property_name is not None:
            self.property_name = property_name

    @property
    def mapping(self):
        """Gets the mapping of this OrgEclipseMicroprofileOpenapiModelsMediaDiscriminator.  # noqa: E501


        :return: The mapping of this OrgEclipseMicroprofileOpenapiModelsMediaDiscriminator.  # noqa: E501
        :rtype: list[object]
        """
        return self._mapping

    @mapping.setter
    def mapping(self, mapping):
        """Sets the mapping of this OrgEclipseMicroprofileOpenapiModelsMediaDiscriminator.


        :param mapping: The mapping of this OrgEclipseMicroprofileOpenapiModelsMediaDiscriminator.  # noqa: E501
        :type: list[object]
        """

        self._mapping = mapping

    @property
    def property_name(self):
        """Gets the property_name of this OrgEclipseMicroprofileOpenapiModelsMediaDiscriminator.  # noqa: E501


        :return: The property_name of this OrgEclipseMicroprofileOpenapiModelsMediaDiscriminator.  # noqa: E501
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this OrgEclipseMicroprofileOpenapiModelsMediaDiscriminator.


        :param property_name: The property_name of this OrgEclipseMicroprofileOpenapiModelsMediaDiscriminator.  # noqa: E501
        :type: str
        """

        self._property_name = property_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OrgEclipseMicroprofileOpenapiModelsMediaDiscriminator, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrgEclipseMicroprofileOpenapiModelsMediaDiscriminator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
