# swagger_client.LegacyApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_landing_page**](LegacyApi.md#get_landing_page) | **GET** /processing | landing page of this API
[**get_requirements_classes**](LegacyApi.md#get_requirements_classes) | **GET** /processing/conformance | information about standards that this API conforms to (optional implementation in ALTIUS)

# **get_landing_page**
> BeSpacebelAltiusProcessingTransactionalModelLandingPage get_landing_page(f=f)

landing page of this API

The landing page provides links to the API definition, the Conformance statements and the metadata about the processes offered by this API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LegacyApi()
f = 'f_example' # str | undefined (optional)

try:
    # landing page of this API
    api_response = api_instance.get_landing_page(f=f)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyApi->get_landing_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f** | **str**| undefined | [optional] 

### Return type

[**BeSpacebelAltiusProcessingTransactionalModelLandingPage**](BeSpacebelAltiusProcessingTransactionalModelLandingPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_requirements_classes**
> BeSpacebelAltiusProcessingTransactionalModelReqClasses get_requirements_classes()

information about standards that this API conforms to (optional implementation in ALTIUS)

list all requirements classes specified in a standard (e.g., WPS REST/JSON Binding Core) that the server conforms to

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LegacyApi()

try:
    # information about standards that this API conforms to (optional implementation in ALTIUS)
    api_response = api_instance.get_requirements_classes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyApi->get_requirements_classes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BeSpacebelAltiusProcessingTransactionalModelReqClasses**](BeSpacebelAltiusProcessingTransactionalModelReqClasses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

