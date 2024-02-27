"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button>   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from unicourt.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from unicourt.exceptions import ApiAttributeError



class ServiceHistory(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('object',): {
            'max_length': 14,
        },
        ('appointed_by',): {
            'max_length': 100,
        },
        ('reason_for_termination',): {
            'max_length': 50,
        },
        ('source_court',): {
            'max_length': 250,
        },
        ('title',): {
            'max_length': 50,
        },
        ('from_date',): {
            'max_length': 25,
        },
        ('to_date',): {
            'max_length': 25,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'object': (str,),  # noqa: E501
            'appointed_by': (str, none_type,),  # noqa: E501
            'reason_for_termination': (str, none_type,),  # noqa: E501
            'source_court': (str, none_type,),  # noqa: E501
            'title': (str, none_type,),  # noqa: E501
            'from_year': (int, none_type,),  # noqa: E501
            'to_year': (int, none_type,),  # noqa: E501
            'from_date': (datetime, none_type,),  # noqa: E501
            'to_date': (datetime, none_type,),  # noqa: E501
            'is_visible': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'object': 'object',  # noqa: E501
        'appointed_by': 'appointedBy',  # noqa: E501
        'reason_for_termination': 'reasonForTermination',  # noqa: E501
        'source_court': 'sourceCourt',  # noqa: E501
        'title': 'title',  # noqa: E501
        'from_year': 'fromYear',  # noqa: E501
        'to_year': 'toYear',  # noqa: E501
        'from_date': 'fromDate',  # noqa: E501
        'to_date': 'toDate',  # noqa: E501
        'is_visible': 'isVisible',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, appointed_by, reason_for_termination, source_court, title, from_year, to_year, from_date, to_date, is_visible, *args, **kwargs):  # noqa: E501
        """ServiceHistory - a model defined in OpenAPI

        Args:
            appointed_by (str, none_type): The President-in-charge of the Judges appointment.
            reason_for_termination (str, none_type): The reason for the Judges termination for the current position.
            source_court (str, none_type): The court served by the Judge. The court is taken from source.
            title (str, none_type): Title held by the Judge.
            from_year (int, none_type): The year in which the Judge began practicing in his current service.
            to_year (int, none_type): The year in which the Judge stoped practicing in his current service.
            from_date (datetime, none_type): The year in which the Judge began practicing in his current service.
            to_date (datetime, none_type): The year in which the Judge stoped practicing in his current service.
            is_visible (bool): Boolean indicating if the service history  is visible or not.

        Keyword Args:
            object (str): defaults to "ServiceHistory"  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        object = kwargs.get('object', "ServiceHistory")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.object = object
        self.appointed_by = appointed_by
        self.reason_for_termination = reason_for_termination
        self.source_court = source_court
        self.title = title
        self.from_year = from_year
        self.to_year = to_year
        self.from_date = from_date
        self.to_date = to_date
        self.is_visible = is_visible
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, appointed_by, reason_for_termination, source_court, title, from_year, to_year, from_date, to_date, is_visible, *args, **kwargs):  # noqa: E501
        """ServiceHistory - a model defined in OpenAPI

        Args:
            appointed_by (str, none_type): The President-in-charge of the Judges appointment.
            reason_for_termination (str, none_type): The reason for the Judges termination for the current position.
            source_court (str, none_type): The court served by the Judge. The court is taken from source.
            title (str, none_type): Title held by the Judge.
            from_year (int, none_type): The year in which the Judge began practicing in his current service.
            to_year (int, none_type): The year in which the Judge stoped practicing in his current service.
            from_date (datetime, none_type): The year in which the Judge began practicing in his current service.
            to_date (datetime, none_type): The year in which the Judge stoped practicing in his current service.
            is_visible (bool): Boolean indicating if the service history  is visible or not.

        Keyword Args:
            object (str): defaults to "ServiceHistory"  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        object = kwargs.get('object', "ServiceHistory")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.object = object
        self.appointed_by = appointed_by
        self.reason_for_termination = reason_for_termination
        self.source_court = source_court
        self.title = title
        self.from_year = from_year
        self.to_year = to_year
        self.from_date = from_date
        self.to_date = to_date
        self.is_visible = is_visible
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")