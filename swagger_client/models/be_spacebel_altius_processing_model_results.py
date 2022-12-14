# coding: utf-8

"""


    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BeSpacebelAltiusProcessingModelResults(object):
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
        '': 'list[object]',
        'or_default': 'list[object]',
        'mod_count': 'int',
        'node': 'list[object]',
        'size': 'int',
        'load_factor': 'float',
        'entry_set': 'list[object]',
        'values': 'list[object]',
        'threshold': 'int',
        'key_set': 'list[object]',
        'table': 'list[object]',
        'empty': 'bool'
    }

    attribute_map = {
        'or_default': 'orDefault',
        'mod_count': 'modCount',
        'node': 'node',
        'size': 'size',
        'load_factor': 'loadFactor',
        'entry_set': 'entrySet',
        'values': 'values',
        'threshold': 'threshold',
        'key_set': 'keySet',
        'table': 'table',
        'empty': 'empty'
    }

    def __init__(self, or_default=None, mod_count=None, node=None, size=None, load_factor=None, entry_set=None, values=None, threshold=None, key_set=None, table=None, empty=None, **kwarg):  # noqa: E501
        """BeSpacebelAltiusProcessingModelResults - a model defined in Swagger"""  # noqa: E501
        self._ = None
        self._or_default = None
        self._mod_count = None
        self._node = None
        self._size = None
        self._load_factor = None
        self._entry_set = None
        self._values = None
        self._threshold = None
        self._key_set = None
        self._table = None
        self._empty = None
        self.discriminator = None
        
        if or_default is not None:
            self.or_default = or_default
        if mod_count is not None:
            self.mod_count = mod_count
        if node is not None:
            self.node = node
        if size is not None:
            self.size = size
        if load_factor is not None:
            self.load_factor = load_factor
        if entry_set is not None:
            self.entry_set = entry_set
        if values is not None:
            self.values = values
        if threshold is not None:
            self.threshold = threshold
        if key_set is not None:
            self.key_set = key_set
        if table is not None:
            self.table = table
        if empty is not None:
            self.empty = empty
            

    @property
    def or_default(self):
        """Gets the or_default of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501


        :return: The or_default of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :rtype: list[object]
        """
        return self._or_default

    @or_default.setter
    def or_default(self, or_default):
        """Sets the or_default of this BeSpacebelAltiusProcessingModelResults.


        :param or_default: The or_default of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :type: list[object]
        """

        self._or_default = or_default

    @property
    def mod_count(self):
        """Gets the mod_count of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501


        :return: The mod_count of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :rtype: int
        """
        return self._mod_count

    @mod_count.setter
    def mod_count(self, mod_count):
        """Sets the mod_count of this BeSpacebelAltiusProcessingModelResults.


        :param mod_count: The mod_count of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :type: int
        """

        self._mod_count = mod_count

    @property
    def node(self):
        """Gets the node of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501


        :return: The node of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :rtype: list[object]
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this BeSpacebelAltiusProcessingModelResults.


        :param node: The node of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :type: list[object]
        """

        self._node = node

    @property
    def size(self):
        """Gets the size of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501


        :return: The size of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BeSpacebelAltiusProcessingModelResults.


        :param size: The size of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def load_factor(self):
        """Gets the load_factor of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501


        :return: The load_factor of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :rtype: float
        """
        return self._load_factor

    @load_factor.setter
    def load_factor(self, load_factor):
        """Sets the load_factor of this BeSpacebelAltiusProcessingModelResults.


        :param load_factor: The load_factor of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :type: float
        """

        self._load_factor = load_factor

    @property
    def entry_set(self):
        """Gets the entry_set of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501


        :return: The entry_set of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :rtype: list[object]
        """
        return self._entry_set

    @entry_set.setter
    def entry_set(self, entry_set):
        """Sets the entry_set of this BeSpacebelAltiusProcessingModelResults.


        :param entry_set: The entry_set of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :type: list[object]
        """

        self._entry_set = entry_set

    @property
    def values(self):
        """Gets the values of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501


        :return: The values of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :rtype: list[object]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this BeSpacebelAltiusProcessingModelResults.


        :param values: The values of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :type: list[object]
        """

        self._values = values

    @property
    def threshold(self):
        """Gets the threshold of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501


        :return: The threshold of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this BeSpacebelAltiusProcessingModelResults.


        :param threshold: The threshold of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :type: int
        """

        self._threshold = threshold

    @property
    def key_set(self):
        """Gets the key_set of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501


        :return: The key_set of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :rtype: list[object]
        """
        return self._key_set

    @key_set.setter
    def key_set(self, key_set):
        """Sets the key_set of this BeSpacebelAltiusProcessingModelResults.


        :param key_set: The key_set of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :type: list[object]
        """

        self._key_set = key_set

    @property
    def table(self):
        """Gets the table of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501


        :return: The table of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :rtype: list[object]
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this BeSpacebelAltiusProcessingModelResults.


        :param table: The table of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :type: list[object]
        """

        self._table = table

    @property
    def empty(self):
        """Gets the empty of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501


        :return: The empty of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        """Sets the empty of this BeSpacebelAltiusProcessingModelResults.


        :param empty: The empty of this BeSpacebelAltiusProcessingModelResults.  # noqa: E501
        :type: bool
        """

        self._empty = empty

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if attr != '':
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
        if issubclass(BeSpacebelAltiusProcessingModelResults, dict):
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
        if not isinstance(other, BeSpacebelAltiusProcessingModelResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
