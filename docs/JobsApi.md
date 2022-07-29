# swagger_client.JobsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dismiss1**](JobsApi.md#dismiss1) | **DELETE** /processing/jobs/{jobID} | cancel a job execution, remove a finished job
[**execute1**](JobsApi.md#execute1) | **POST** /processing/jobs | Execute a process.
[**get_logs1**](JobsApi.md#get_logs1) | **GET** /processing/jobs/{jobID}/logs | Retrieve logs of a job
[**get_status1**](JobsApi.md#get_status1) | **GET** /processing/jobs/{jobID} | Retrieve the information about a job (status, results)

# **dismiss1**
> BeSpacebelAltiusProcessingModelJobInfo dismiss1(job_id)

cancel a job execution, remove a finished job

Cancel a job execution and remove it from the jobs list.  For more information, see [Section 14](http://docs.ogc.org/DRAFTS/18-062.html#Dismiss). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
job_id = 'job_id_example' # str | The id of a job

try:
    # cancel a job execution, remove a finished job
    api_response = api_instance.dismiss1(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->dismiss1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The id of a job | 

### Return type

[**BeSpacebelAltiusProcessingModelJobInfo**](BeSpacebelAltiusProcessingModelJobInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute1**
> object execute1(body)

Execute a process.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
body = swagger_client.BeSpacebelAltiusProcessingModelExecutionRequest() # BeSpacebelAltiusProcessingModelExecutionRequest | 

try:
    # Execute a process.
    api_response = api_instance.execute1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->execute1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BeSpacebelAltiusProcessingModelExecutionRequest**](BeSpacebelAltiusProcessingModelExecutionRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs1**
> object get_logs1(job_id)

Retrieve logs of a job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
job_id = 'job_id_example' # str | The id of a job

try:
    # Retrieve logs of a job
    api_response = api_instance.get_logs1(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_logs1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The id of a job | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status1**
> BeSpacebelAltiusProcessingModelJobInfo get_status1(job_id)

Retrieve the information about a job (status, results)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
job_id = 'job_id_example' # str | The id of a job

try:
    # Retrieve the information about a job (status, results)
    api_response = api_instance.get_status1(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_status1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The id of a job | 

### Return type

[**BeSpacebelAltiusProcessingModelJobInfo**](BeSpacebelAltiusProcessingModelJobInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

