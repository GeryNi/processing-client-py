# coding: utf-8

"""


    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BeSpacebelAltiusProcessingModelJobInfo(object):
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
        'creation_time': 'str',
        'message': 'str',
        'parent_id': 'str',
        'execution_request': 'BeSpacebelAltiusProcessingModelExecutionRequest',
        'job_id': 'str',
        'process_id': 'str',
        'last_update': 'str',
        'results': 'object',
        'logs': 'str',
        'status': 'str'
    }

    attribute_map = {
        'creation_time': 'creation_time',
        'message': 'message',
        'parent_id': 'parentID',
        'execution_request': 'executionRequest',
        'job_id': 'jobID',
        'process_id': 'processID',
        'last_update': 'last_update',
        'results': 'results',
        'logs': 'logs',
        'status': 'status'
    }

    def __init__(self, creation_time=None, message=None, parent_id=None, execution_request=None, job_id=None, process_id=None, last_update=None, results=None, logs=None, status=None):  # noqa: E501
        """BeSpacebelAltiusProcessingModelJobInfo - a model defined in Swagger"""  # noqa: E501
        self._creation_time = None
        self._message = None
        self._parent_id = None
        self._execution_request = None
        self._job_id = None
        self._process_id = None
        self._last_update = None
        self._results = None
        self._logs = None
        self._status = None
        self.discriminator = None
        if creation_time is not None:
            self.creation_time = creation_time
        if message is not None:
            self.message = message
        self.parent_id = parent_id
        if execution_request is not None:
            self.execution_request = execution_request
        self.job_id = job_id
        if process_id is not None:
            self.process_id = process_id
        if last_update is not None:
            self.last_update = last_update
        if results is not None:
            self.results = results
        if logs is not None:
            self.logs = logs
        self.status = status

    @property
    def creation_time(self):
        """Gets the creation_time of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501

        Date of creation  # noqa: E501

        :return: The creation_time of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this BeSpacebelAltiusProcessingModelJobInfo.

        Date of creation  # noqa: E501

        :param creation_time: The creation_time of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def message(self):
        """Gets the message of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501


        :return: The message of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BeSpacebelAltiusProcessingModelJobInfo.


        :param message: The message of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def parent_id(self):
        """Gets the parent_id of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501

        Parent identifier  # noqa: E501

        :return: The parent_id of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BeSpacebelAltiusProcessingModelJobInfo.

        Parent identifier  # noqa: E501

        :param parent_id: The parent_id of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :type: str
        """
        if parent_id is None:
            raise ValueError("Invalid value for `parent_id`, must not be `None`")  # noqa: E501

        self._parent_id = parent_id

    @property
    def execution_request(self):
        """Gets the execution_request of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501


        :return: The execution_request of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :rtype: BeSpacebelAltiusProcessingModelExecutionRequest
        """
        return self._execution_request

    @execution_request.setter
    def execution_request(self, execution_request):
        """Sets the execution_request of this BeSpacebelAltiusProcessingModelJobInfo.


        :param execution_request: The execution_request of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :type: BeSpacebelAltiusProcessingModelExecutionRequest
        """

        self._execution_request = execution_request

    @property
    def job_id(self):
        """Gets the job_id of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501

        Job identifier  # noqa: E501

        :return: The job_id of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this BeSpacebelAltiusProcessingModelJobInfo.

        Job identifier  # noqa: E501

        :param job_id: The job_id of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :type: str
        """
        if job_id is None:
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501

        self._job_id = job_id

    @property
    def process_id(self):
        """Gets the process_id of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501

        Process Identifier  # noqa: E501

        :return: The process_id of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :rtype: str
        """
        return self._process_id

    @process_id.setter
    def process_id(self, process_id):
        """Sets the process_id of this BeSpacebelAltiusProcessingModelJobInfo.

        Process Identifier  # noqa: E501

        :param process_id: The process_id of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :type: str
        """

        self._process_id = process_id

    @property
    def last_update(self):
        """Gets the last_update of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501

        Date of last modicification  # noqa: E501

        :return: The last_update of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this BeSpacebelAltiusProcessingModelJobInfo.

        Date of last modicification  # noqa: E501

        :param last_update: The last_update of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :type: str
        """

        self._last_update = last_update

    @property
    def results(self):
        """Gets the results of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501


        :return: The results of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :rtype: BeSpacebelAltiusProcessingModelResults
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this BeSpacebelAltiusProcessingModelJobInfo.


        :param results: The results of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :type: BeSpacebelAltiusProcessingModelResults
        """

        self._results = results

    @property
    def logs(self):
        """Gets the logs of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501


        :return: The logs of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :rtype: str
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this BeSpacebelAltiusProcessingModelJobInfo.


        :param logs: The logs of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :type: str
        """

        self._logs = logs

    @property
    def status(self):
        """Gets the status of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501


        :return: The status of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BeSpacebelAltiusProcessingModelJobInfo.


        :param status: The status of this BeSpacebelAltiusProcessingModelJobInfo.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["accepted", "recovering", "queued", "running", "successful", "failed", "dismissed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(BeSpacebelAltiusProcessingModelJobInfo, dict):
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
        if not isinstance(other, BeSpacebelAltiusProcessingModelJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
