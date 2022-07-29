# swagger_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](DefaultApi.md#get) | **GET** /processing/openapi | 
[**get_checks1**](DefaultApi.md#get_checks1) | **GET** /processing/health | 
[**get_json123**](DefaultApi.md#get_json123) | **GET** /processing/metrics/{registry}/{metric} | 
[**get_json12345**](DefaultApi.md#get_json12345) | **GET** /processing/metrics | 
[**get_metadata12**](DefaultApi.md#get_metadata12) | **OPTIONS** /processing/metrics/{registry} | 
[**get_metadata123**](DefaultApi.md#get_metadata123) | **OPTIONS** /processing/metrics/{registry}/{metric} | 
[**get_text12345**](DefaultApi.md#get_text12345) | **GET** /processing/metrics/{registry} | 

# **get**
> OrgEclipseMicroprofileOpenapiModelsOpenAPI get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrgEclipseMicroprofileOpenapiModelsOpenAPI**](OrgEclipseMicroprofileOpenapiModelsOpenAPI.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checks1**
> object get_checks1()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.get_checks1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_checks1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_json123**
> JavaLangObject get_json123(registry, metric)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
registry = 'registry_example' # str | 
metric = 'metric_example' # str | 

try:
    api_response = api_instance.get_json123(registry, metric)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_json123: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry** | **str**|  | 
 **metric** | **str**|  | 

### Return type

[**JavaLangObject**](JavaLangObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_json12345**
> JavaLangObject get_json12345()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.get_json12345()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_json12345: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JavaLangObject**](JavaLangObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata12**
> JavaLangObject get_metadata12(registry)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
registry = 'registry_example' # str | 

try:
    api_response = api_instance.get_metadata12(registry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_metadata12: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry** | **str**|  | 

### Return type

[**JavaLangObject**](JavaLangObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata123**
> JavaLangObject get_metadata123(registry, metric)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
registry = 'registry_example' # str | 
metric = 'metric_example' # str | 

try:
    api_response = api_instance.get_metadata123(registry, metric)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_metadata123: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry** | **str**|  | 
 **metric** | **str**|  | 

### Return type

[**JavaLangObject**](JavaLangObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_text12345**
> str get_text12345(registry)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
registry = 'registry_example' # str | 

try:
    api_response = api_instance.get_text12345(registry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_text12345: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

