# assimilate_client.ProjectsApi

All URIs are relative to *http://localhost:8080/APIV2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_construct**](ProjectsApi.md#add_construct) | **POST** /constructs/new | Construct Add
[**add_construct_current_output**](ProjectsApi.md#add_construct_current_output) | **POST** /constructs/current/outputs/new | Output Add (CC)
[**add_construct_current_slot**](ProjectsApi.md#add_construct_current_slot) | **POST** /constructs/current/slots/new/{slot_IDX} | Slot Add (CC)
[**add_construct_output**](ProjectsApi.md#add_construct_output) | **POST** /constructs/{construct_UUID}/outputs/new | Output Add (CID)
[**add_construct_slot**](ProjectsApi.md#add_construct_slot) | **POST** /constructs/{construct_UUID}/slots/new/{slot_IDX} | Slot Add (CID)
[**add_group**](ProjectsApi.md#add_group) | **POST** /groups/new | Group Add
[**add_project**](ProjectsApi.md#add_project) | **POST** /projects/new | Project Add
[**add_shot**](ProjectsApi.md#add_shot) | **POST** /shot/new | Shot Add
[**add_shot_layer**](ProjectsApi.md#add_shot_layer) | **POST** /shot/{shot_id}/layers/new | Shot Create Layer
[**add_shot_layer_group**](ProjectsApi.md#add_shot_layer_group) | **POST** /shot/{shot_id}/layers/group | Shot Create Layer Group
[**delete_construct**](ProjectsApi.md#delete_construct) | **DELETE** /constructs/{construct_UUID} | Construct Delete
[**delete_construct_current_output**](ProjectsApi.md#delete_construct_current_output) | **DELETE** /constructs/current/outputs/{output_id} | Output Delete (CC)
[**delete_construct_current_slot**](ProjectsApi.md#delete_construct_current_slot) | **DELETE** /constructs/current/slots/{slot_IDX} | Slot Delete (CC)
[**delete_construct_current_slot_version**](ProjectsApi.md#delete_construct_current_slot_version) | **DELETE** /constructs/current/slots/{slot_IDX}/versions/{version_IDX} | Shot Delete (CC)
[**delete_construct_output**](ProjectsApi.md#delete_construct_output) | **DELETE** /constructs/{construct_UUID}/outputs/{output_id} | Output Delete (CID)
[**delete_construct_slot**](ProjectsApi.md#delete_construct_slot) | **DELETE** /constructs/{construct_UUID}/slots/{slot_IDX} | Slot Delete (CID)
[**delete_construct_slot_version**](ProjectsApi.md#delete_construct_slot_version) | **DELETE** /constructs/{construct_UUID}/slots/{slot_IDX}/versions/{version_IDX} | Shot Delete (VRS)
[**delete_constructs_current**](ProjectsApi.md#delete_constructs_current) | **DELETE** /constructs/current | Construct Current Delete
[**delete_constructs_current_reference**](ProjectsApi.md#delete_constructs_current_reference) | **DELETE** /constructs/current/ref_shot | Construct Current Reference shot Delete
[**delete_constructs_reference**](ProjectsApi.md#delete_constructs_reference) | **DELETE** /constructs/{construct_UUID}/ref_shot | Construct Current Reference shot Delete
[**delete_group**](ProjectsApi.md#delete_group) | **DELETE** /groups/{group_UUID} | Group Delete
[**delete_group_current**](ProjectsApi.md#delete_group_current) | **DELETE** /groups/current | Group Current Delete
[**delete_shot**](ProjectsApi.md#delete_shot) | **DELETE** /shot/{shot_id} | Shot Delete
[**delete_shot_color**](ProjectsApi.md#delete_shot_color) | **DELETE** /shot/{shot_id}/color | Shot Reset Color Properties
[**delete_shot_input**](ProjectsApi.md#delete_shot_input) | **DELETE** /shot/{shot_id}/inputs/{input_idx} | Input Delete
[**delete_shot_layer**](ProjectsApi.md#delete_shot_layer) | **DELETE** /shot/{shot_id}/layers/{layer_idx} | Shot Delete Layer
[**get_construct**](ProjectsApi.md#get_construct) | **GET** /constructs/{construct_UUID} | Construct Get Properties
[**get_construct_current_output**](ProjectsApi.md#get_construct_current_output) | **GET** /constructs/current/outputs/{output_id} | Output Get Properties (CC)
[**get_construct_current_outputs**](ProjectsApi.md#get_construct_current_outputs) | **GET** /constructs/current/outputs | Output List (CC)
[**get_construct_current_selected_shots**](ProjectsApi.md#get_construct_current_selected_shots) | **GET** /constructs/current/sel_shots | Shot Selection (CC)
[**get_construct_current_slot**](ProjectsApi.md#get_construct_current_slot) | **GET** /constructs/current/slots/{slot_IDX} | Slot Get Properties (CC)
[**get_construct_current_slot_version**](ProjectsApi.md#get_construct_current_slot_version) | **GET** /constructs/current/slots/{slot_IDX}/versions/{version_IDX} | Shot Get Properties (CC)
[**get_construct_current_slot_versions**](ProjectsApi.md#get_construct_current_slot_versions) | **GET** /constructs/current/slots/{slot_IDX}/versions | Shot List (CC)
[**get_construct_current_slots**](ProjectsApi.md#get_construct_current_slots) | **GET** /constructs/current/slots | Slot List (CC)
[**get_construct_output**](ProjectsApi.md#get_construct_output) | **GET** /constructs/{construct_UUID}/outputs/{output_id} | Output Get Properties (CID)
[**get_construct_outputs**](ProjectsApi.md#get_construct_outputs) | **GET** /constructs/{construct_UUID}/outputs | Output List (CID)
[**get_construct_slot**](ProjectsApi.md#get_construct_slot) | **GET** /constructs/{construct_UUID}/slots/{slot_IDX} | Slot Get Properties (CID)
[**get_construct_slot_version**](ProjectsApi.md#get_construct_slot_version) | **GET** /constructs/{construct_UUID}/slots/{slot_IDX}/versions/{version_IDX} | Shot Get Properties (VRS)
[**get_construct_slot_versions**](ProjectsApi.md#get_construct_slot_versions) | **GET** /constructs/{construct_UUID}/slots/{slot_IDX}/versions | Shot List (VRS)
[**get_construct_slots**](ProjectsApi.md#get_construct_slots) | **GET** /constructs/{construct_UUID}/slots | Slot List (CID)
[**get_constructs**](ProjectsApi.md#get_constructs) | **GET** /constructs | Construct List
[**get_constructs_current**](ProjectsApi.md#get_constructs_current) | **GET** /constructs/current | Construct Current Get
[**get_constructs_current_reference**](ProjectsApi.md#get_constructs_current_reference) | **GET** /constructs/current/ref_shot | Construct Current Get Reference shot
[**get_constructs_reference**](ProjectsApi.md#get_constructs_reference) | **GET** /constructs/{construct_UUID}/ref_shot | Construct Get Reference shot
[**get_group**](ProjectsApi.md#get_group) | **GET** /groups/{group_UUID} | Group Get Properties
[**get_group_current**](ProjectsApi.md#get_group_current) | **GET** /groups/current | Group Current Get
[**get_groups**](ProjectsApi.md#get_groups) | **GET** /groups | Group List
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /projects | Project List
[**get_projects_current**](ProjectsApi.md#get_projects_current) | **GET** /projects/current | Project Current
[**get_projects_item**](ProjectsApi.md#get_projects_item) | **GET** /projects/item/{projectID} | Project Get Properties
[**get_shot**](ProjectsApi.md#get_shot) | **GET** /shot/{shot_id} | Shot Get Properties
[**get_shot_color**](ProjectsApi.md#get_shot_color) | **GET** /shot/{shot_id}/color | Shot Get Color Properties
[**get_shot_input**](ProjectsApi.md#get_shot_input) | **GET** /shot/{shot_id}/inputs/{input_idx} | Input Get Properties
[**get_shot_inputs**](ProjectsApi.md#get_shot_inputs) | **GET** /shot/{shot_id}/inputs | Inputs List
[**get_shot_layer**](ProjectsApi.md#get_shot_layer) | **GET** /shot/{shot_id}/layers/{layer_idx} | Shot Get Layer Properties
[**get_shot_layer_canvas**](ProjectsApi.md#get_shot_layer_canvas) | **GET** /shot/{shot_id}/layers/{layer_idx}/canvas | Shot Layer Get Canvas Properties
[**get_shot_layer_color**](ProjectsApi.md#get_shot_layer_color) | **GET** /shot/{shot_id}/layers/{layer_idx}/color | Shot Layer Get Color Properties
[**get_shot_layer_fill**](ProjectsApi.md#get_shot_layer_fill) | **GET** /shot/{shot_id}/layers/{layer_idx}/fill | Shot Layer Get Fill Properties
[**get_shot_layer_matte**](ProjectsApi.md#get_shot_layer_matte) | **GET** /shot/{shot_id}/layers/{layer_idx}/matte | Shot Layer Get Matte Properties
[**get_shot_layers**](ProjectsApi.md#get_shot_layers) | **GET** /shot/{shot_id}/layers | Shot Get Layers Properties
[**move_construct**](ProjectsApi.md#move_construct) | **PATCH** /constructs/{construct_UUID} | Construct Move
[**move_construct_current_slot_version**](ProjectsApi.md#move_construct_current_slot_version) | **PATCH** /constructs/current/slots/{slot_IDX}/versions/{version_IDX} | Shot Move (CC)
[**move_construct_slot_version**](ProjectsApi.md#move_construct_slot_version) | **PATCH** /constructs/{construct_UUID}/slots/{slot_IDX}/versions/{version_IDX} | Shot Move (VRS)
[**move_constructs_current**](ProjectsApi.md#move_constructs_current) | **PATCH** /constructs/current | Construct Current Move
[**move_group**](ProjectsApi.md#move_group) | **PATCH** /groups/{group_UUID} | Group Move
[**move_group_current**](ProjectsApi.md#move_group_current) | **PATCH** /groups/current | Group Current Move
[**move_layer**](ProjectsApi.md#move_layer) | **PATCH** /shot/{shot_id}/layers/{layer_idx} | Layer Move
[**move_shot**](ProjectsApi.md#move_shot) | **PATCH** /shot/{shot_id} | Shot Move
[**reset_shot_layer_canvas**](ProjectsApi.md#reset_shot_layer_canvas) | **DELETE** /shot/{shot_id}/layers/{layer_idx}/canvas | Shot Layer Reset Canvas Properties
[**reset_shot_layer_color**](ProjectsApi.md#reset_shot_layer_color) | **DELETE** /shot/{shot_id}/layers/{layer_idx}/color | Shot Layer Reset Color Properties
[**reset_shot_layer_fill**](ProjectsApi.md#reset_shot_layer_fill) | **DELETE** /shot/{shot_id}/layers/{layer_idx}/fill | Shot Layer Reset Fill Properties
[**reset_shot_layer_matte**](ProjectsApi.md#reset_shot_layer_matte) | **DELETE** /shot/{shot_id}/layers/{layer_idx}/matte | Shot Layer Reset Matte Properties
[**select_construct**](ProjectsApi.md#select_construct) | **POST** /constructs/{construct_UUID} | Construct Select
[**select_group**](ProjectsApi.md#select_group) | **POST** /groups/{group_UUID} | Group Select
[**set_construct**](ProjectsApi.md#set_construct) | **PUT** /constructs/{construct_UUID} | Construct Set Properties
[**set_construct_current_output**](ProjectsApi.md#set_construct_current_output) | **PUT** /constructs/current/outputs/{output_id} | Output Set Properties (CC)
[**set_construct_current_slot**](ProjectsApi.md#set_construct_current_slot) | **PUT** /constructs/current/slots/{slot_IDX} | Slot Set Properties (CC)
[**set_construct_current_slot_version**](ProjectsApi.md#set_construct_current_slot_version) | **PUT** /constructs/current/slots/{slot_IDX}/versions/{version_IDX} | Shot Set Properties (CC)
[**set_construct_output**](ProjectsApi.md#set_construct_output) | **PUT** /constructs/{construct_UUID}/outputs/{output_id} | Output Set Properties (CID)
[**set_construct_slot**](ProjectsApi.md#set_construct_slot) | **PUT** /constructs/{construct_UUID}/slots/{slot_IDX} | Slot Set Properties (CID)
[**set_construct_slot_version**](ProjectsApi.md#set_construct_slot_version) | **PUT** /constructs/{construct_UUID}/slots/{slot_IDX}/versions/{version_IDX} | Shot Set Properties (VRS)
[**set_constructs_current**](ProjectsApi.md#set_constructs_current) | **PUT** /constructs/current | Construct Current Set Properties
[**set_constructs_current_reference**](ProjectsApi.md#set_constructs_current_reference) | **PUT** /constructs/current/ref_shot | Construct Current Set reference shot
[**set_constructs_reference**](ProjectsApi.md#set_constructs_reference) | **PUT** /constructs/{construct_UUID}/ref_shot | Construct Current Set reference shot
[**set_group**](ProjectsApi.md#set_group) | **PUT** /groups/{group_UUID} | Group Set Properties
[**set_projects_item**](ProjectsApi.md#set_projects_item) | **PUT** /projects/item/{projectID} | Project Set Properties
[**set_shot**](ProjectsApi.md#set_shot) | **PUT** /shot/{shot_id} | Shot Set Properties
[**set_shot_color**](ProjectsApi.md#set_shot_color) | **PUT** /shot/{shot_id}/color | Shot Set Color Properties
[**set_shot_input**](ProjectsApi.md#set_shot_input) | **PUT** /shot/{shot_id}/inputs/{input_idx} | Input Set Properties
[**set_shot_layer**](ProjectsApi.md#set_shot_layer) | **PUT** /shot/{shot_id}/layers/{layer_idx} | Shot Set Layer Properties
[**set_shot_layer_canvas**](ProjectsApi.md#set_shot_layer_canvas) | **PUT** /shot/{shot_id}/layers/{layer_idx}/canvas | Shot Layer Set  Canvas Properties
[**set_shot_layer_color**](ProjectsApi.md#set_shot_layer_color) | **PUT** /shot/{shot_id}/layers/{layer_idx}/color | Shot Layer Set  Color Properties
[**set_shot_layer_fill**](ProjectsApi.md#set_shot_layer_fill) | **PUT** /shot/{shot_id}/layers/{layer_idx}/fill | Shot Layer Set  Fill Properties
[**set_shot_layer_matte**](ProjectsApi.md#set_shot_layer_matte) | **PUT** /shot/{shot_id}/layers/{layer_idx}/matte | Shot Layer Set  Matte Properties

# **add_construct**
> ConstructData add_construct()

Construct Add

Create a new Construct in the current active Group

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()

try:
    # Construct Add
    api_response = api_instance.add_construct()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_construct: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConstructData**](ConstructData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_construct_current_output**
> ShotData add_construct_current_output(body, level=level)

Output Add (CC)

Create a new Output in the Current Construct (CC).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ShotData() # ShotData | json output node data
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Output Add (CC)
    api_response = api_instance.add_construct_current_output(body, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_construct_current_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShotData**](ShotData.md)| json output node data | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotData**](ShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_construct_current_slot**
> SlotData add_construct_current_slot(slot_idx)

Slot Add (CC)

Create a new Slot in the n-th position in the current Construct (CC).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
slot_idx = 56 # int | Slot Index

try:
    # Slot Add (CC)
    api_response = api_instance.add_construct_current_slot(slot_idx)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_construct_current_slot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot_idx** | **int**| Slot Index | 

### Return type

[**SlotData**](SlotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_construct_output**
> ShotData add_construct_output(body, construct_uuid, level=level)

Output Add (CID)

Add a new Output in the Constuct with UUID (CID).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ShotData() # ShotData | json output node data
construct_uuid = assimilate_client.Uuid() # Uuid | Construct UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Output Add (CID)
    api_response = api_instance.add_construct_output(body, construct_uuid, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_construct_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShotData**](ShotData.md)| json output node data | 
 **construct_uuid** | [**Uuid**](.md)| Construct UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotData**](ShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_construct_slot**
> SlotData add_construct_slot(construct_uuid, slot_idx)

Slot Add (CID)

Create new Slot in Construct with UUID (CID).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
construct_uuid = 'construct_uuid_example' # str | Construct UUID
slot_idx = 56 # int | Slot Index

try:
    # Slot Add (CID)
    api_response = api_instance.add_construct_slot(construct_uuid, slot_idx)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_construct_slot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construct_uuid** | **str**| Construct UUID | 
 **slot_idx** | **int**| Slot Index | 

### Return type

[**SlotData**](SlotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group**
> GroupsData add_group()

Group Add

Create a new Group in the Project tree.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()

try:
    # Group Add
    api_response = api_instance.add_group()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_group: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupsData**](GroupsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_project**
> ProjectData add_project(body)

Project Add

Create a new project and set its properties. Returns an error when another project is currently loaded.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ProjectData() # ProjectData | json with project data

try:
    # Project Add
    api_response = api_instance.add_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectData**](ProjectData.md)| json with project data | 

### Return type

[**ProjectData**](ProjectData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_shot**
> ShotData add_shot(body)

Shot Add

Create a new Shot based on a type-uuid or a filename. The new Shot is not automatically added to a Construct.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ShotData() # ShotData | json with shot data

try:
    # Shot Add
    api_response = api_instance.add_shot(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_shot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShotData**](ShotData.md)| json with shot data | 

### Return type

[**ShotData**](ShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_shot_layer**
> LayerData add_shot_layer(body, shot_id, level=level)

Shot Create Layer

Create a new layer for the Shot with UUID. The new layer is added at the end of the layer list.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.LayerData() # LayerData | json with shot data
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Create Layer
    api_response = api_instance.add_shot_layer(body, shot_id, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_shot_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayerData**](LayerData.md)| json with shot data | 
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**LayerData**](LayerData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_shot_layer_group**
> add_shot_layer_group(shot_id, body=body, level=level)

Shot Create Layer Group

Create a new group for the Shot with UUID. The new group is added at the end of the layer list.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
body = assimilate_client.LayerData() # LayerData | json with shot data (optional)
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Create Layer Group
    api_instance.add_shot_layer_group(shot_id, body=body, level=level)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_shot_layer_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **body** | [**LayerData**](LayerData.md)| json with shot data | [optional] 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_construct**
> delete_construct(construct_uuid)

Construct Delete

Delete the Construct with UUID. If this is the last Construct ina Group, a new Construct is automatically created.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
construct_uuid = assimilate_client.Uuid() # Uuid | Construct UUID

try:
    # Construct Delete
    api_instance.delete_construct(construct_uuid)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_construct: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construct_uuid** | [**Uuid**](.md)| Construct UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_construct_current_output**
> delete_construct_current_output(output_id)

Output Delete (CC)

Delete the Output with UUID in the current Construct (CC).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
output_id = assimilate_client.Uuid() # Uuid | Output Node UUID

try:
    # Output Delete (CC)
    api_instance.delete_construct_current_output(output_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_construct_current_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_id** | [**Uuid**](.md)| Output Node UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_construct_current_slot**
> delete_construct_current_slot(slot_idx, level=level)

Slot Delete (CC)

Delete the n-th Slot in the current Construct (CC).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
slot_idx = 56 # int | Slot Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Slot Delete (CC)
    api_instance.delete_construct_current_slot(slot_idx, level=level)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_construct_current_slot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot_idx** | **int**| Slot Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_construct_current_slot_version**
> delete_construct_current_slot_version(slot_idx, version_idx)

Shot Delete (CC)

Delete the n-th Shot in the m-th Slot in the current Construct (CC).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
slot_idx = 56 # int | Slot Index
version_idx = 56 # int | version Index, representing the nth version

try:
    # Shot Delete (CC)
    api_instance.delete_construct_current_slot_version(slot_idx, version_idx)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_construct_current_slot_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot_idx** | **int**| Slot Index | 
 **version_idx** | **int**| version Index, representing the nth version | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_construct_output**
> delete_construct_output(construct_uuid, output_id)

Output Delete (CID)

Delete Output with UUI in the Construct with UUID (CID).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
construct_uuid = assimilate_client.Uuid() # Uuid | Construct UUID
output_id = assimilate_client.Uuid() # Uuid | Output Node UUID

try:
    # Output Delete (CID)
    api_instance.delete_construct_output(construct_uuid, output_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_construct_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construct_uuid** | [**Uuid**](.md)| Construct UUID | 
 **output_id** | [**Uuid**](.md)| Output Node UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_construct_slot**
> delete_construct_slot(construct_uuid, slot_idx, level=level)

Slot Delete (CID)

Delete Slot wint Index in Construct with UUID. Any Shots in the Slot are also removed (CID).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
construct_uuid = 'construct_uuid_example' # str | Construct UUID
slot_idx = 56 # int | Slot Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Slot Delete (CID)
    api_instance.delete_construct_slot(construct_uuid, slot_idx, level=level)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_construct_slot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construct_uuid** | **str**| Construct UUID | 
 **slot_idx** | **int**| Slot Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_construct_slot_version**
> delete_construct_slot_version(construct_uuid, slot_idx, version_idx)

Shot Delete (VRS)

Delete the n-th Shot in Slot with Index in Construct with UUI.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
construct_uuid = 'construct_uuid_example' # str | Construct UUID
slot_idx = 56 # int | Slot Index
version_idx = 56 # int | Version index, representing the nth version in a slot

try:
    # Shot Delete (VRS)
    api_instance.delete_construct_slot_version(construct_uuid, slot_idx, version_idx)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_construct_slot_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construct_uuid** | **str**| Construct UUID | 
 **slot_idx** | **int**| Slot Index | 
 **version_idx** | **int**| Version index, representing the nth version in a slot | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_constructs_current**
> delete_constructs_current()

Construct Current Delete

Delete the current selected Construct. The prior Construct in the Group will become the new active. If no Constructs are left in the Group a new Construct is created automatically.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()

try:
    # Construct Current Delete
    api_instance.delete_constructs_current()
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_constructs_current: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_constructs_current_reference**
> delete_constructs_current_reference()

Construct Current Reference shot Delete

Delete the reference shot of the current Construct.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()

try:
    # Construct Current Reference shot Delete
    api_instance.delete_constructs_current_reference()
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_constructs_current_reference: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_constructs_reference**
> delete_constructs_reference(construct_uuid)

Construct Current Reference shot Delete

Delete the reference shot of a construct with the specified UUID.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
construct_uuid = 'construct_uuid_example' # str | Construct UUID

try:
    # Construct Current Reference shot Delete
    api_instance.delete_constructs_reference(construct_uuid)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_constructs_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construct_uuid** | **str**| Construct UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group_uuid)

Group Delete

Delete the Group with UUI and all underlying Timelines.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
group_uuid = assimilate_client.Uuid() # Uuid | Group UUID

try:
    # Group Delete
    api_instance.delete_group(group_uuid)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uuid** | [**Uuid**](.md)| Group UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_current**
> delete_group_current()

Group Current Delete

Remove the current selected Group and all underlying Timelines

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()

try:
    # Group Current Delete
    api_instance.delete_group_current()
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_group_current: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shot**
> delete_shot(shot_id)

Shot Delete

Delete the Shot with UUID. The Shot is removed from all locations it is used and any Input Shot of the Shot composition are also deleted.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID

try:
    # Shot Delete
    api_instance.delete_shot(shot_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_shot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shot_color**
> delete_shot_color(shot_id)

Shot Reset Color Properties

Reset the color properties of the Shot with UUID.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID

try:
    # Shot Reset Color Properties
    api_instance.delete_shot_color(shot_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_shot_color: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shot_input**
> delete_shot_input(shot_id, input_idx)

Input Delete

Remove the n-th Input of Shot with UUID. The Input of the shot is cleard. The Input Shot itself is not deleted and is maintained when used elsewhere.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
input_idx = 56 # int | index of the nth input

try:
    # Input Delete
    api_instance.delete_shot_input(shot_id, input_idx)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_shot_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **input_idx** | **int**| index of the nth input | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shot_layer**
> delete_shot_layer(shot_id, layer_idx)

Shot Delete Layer

Delete the layer at the specified index for the Shot with UUID.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index

try:
    # Shot Delete Layer
    api_instance.delete_shot_layer(shot_id, layer_idx)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_shot_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_construct**
> ConstructData get_construct(construct_uuid, level=level)

Construct Get Properties

Get the properties of Construct with UUID

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
construct_uuid = assimilate_client.Uuid() # Uuid | Construct UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Construct Get Properties
    api_response = api_instance.get_construct(construct_uuid, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_construct: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construct_uuid** | [**Uuid**](.md)| Construct UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ConstructData**](ConstructData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_construct_current_output**
> ShotData get_construct_current_output(output_id, level=level)

Output Get Properties (CC)

Get the properties of Output with UUID in the current Construct (CC).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
output_id = assimilate_client.Uuid() # Uuid | Output Node UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Output Get Properties (CC)
    api_response = api_instance.get_construct_current_output(output_id, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_construct_current_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_id** | [**Uuid**](.md)| Output Node UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotData**](ShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_construct_current_outputs**
> ShotsData get_construct_current_outputs(level=level)

Output List (CC)

Get the list of Outputs of the current Construct (CC).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Output List (CC)
    api_response = api_instance.get_construct_current_outputs(level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_construct_current_outputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotsData**](ShotsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_construct_current_selected_shots**
> SelectedShotsData get_construct_current_selected_shots(level=level)

Shot Selection (CC)

Get the list of selected Shots of the current Construct (CC).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Selection (CC)
    api_response = api_instance.get_construct_current_selected_shots(level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_construct_current_selected_shots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**SelectedShotsData**](SelectedShotsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_construct_current_slot**
> SlotData get_construct_current_slot(slot_idx, level=level)

Slot Get Properties (CC)

Get the properties of the n-th Slot in the current Construct (CC).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
slot_idx = 56 # int | Slot Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Slot Get Properties (CC)
    api_response = api_instance.get_construct_current_slot(slot_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_construct_current_slot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot_idx** | **int**| Slot Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**SlotData**](SlotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_construct_current_slot_version**
> ShotData get_construct_current_slot_version(slot_idx, version_idx, level=level)

Shot Get Properties (CC)

Get the properties of the n-th Shot in the m-th Slot in current Construct (CC).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
slot_idx = 56 # int | Slot Index
version_idx = 56 # int | version Index, representing the nth version
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Get Properties (CC)
    api_response = api_instance.get_construct_current_slot_version(slot_idx, version_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_construct_current_slot_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot_idx** | **int**| Slot Index | 
 **version_idx** | **int**| version Index, representing the nth version | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotData**](ShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_construct_current_slot_versions**
> ShotsData get_construct_current_slot_versions(slot_idx, level=level)

Shot List (CC)

Get a list of Shots in the n-th Slot of the current Construct (CC).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
slot_idx = 56 # int | Slot Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot List (CC)
    api_response = api_instance.get_construct_current_slot_versions(slot_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_construct_current_slot_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot_idx** | **int**| Slot Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotsData**](ShotsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_construct_current_slots**
> SlotsData get_construct_current_slots(level=level)

Slot List (CC)

Get the list of Slots in the current Constuct (CC).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Slot List (CC)
    api_response = api_instance.get_construct_current_slots(level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_construct_current_slots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**SlotsData**](SlotsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_construct_output**
> ShotData get_construct_output(construct_uuid, output_id, level=level)

Output Get Properties (CID)

Get the properties of Output with UUID in the Constuct with UUID (CID).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
construct_uuid = assimilate_client.Uuid() # Uuid | Construct UUID
output_id = assimilate_client.Uuid() # Uuid | Output Node UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Output Get Properties (CID)
    api_response = api_instance.get_construct_output(construct_uuid, output_id, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_construct_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construct_uuid** | [**Uuid**](.md)| Construct UUID | 
 **output_id** | [**Uuid**](.md)| Output Node UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotData**](ShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_construct_outputs**
> ShotsData get_construct_outputs(construct_uuid, level=level)

Output List (CID)

Get the list of Output nodes of Construct with UUID (CID).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
construct_uuid = assimilate_client.Uuid() # Uuid | Construct UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Output List (CID)
    api_response = api_instance.get_construct_outputs(construct_uuid, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_construct_outputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construct_uuid** | [**Uuid**](.md)| Construct UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotsData**](ShotsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_construct_slot**
> SlotData get_construct_slot(construct_uuid, slot_idx, level=level)

Slot Get Properties (CID)

Get the properties of SLot with Index a Constuct with UUID (CID).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
construct_uuid = 'construct_uuid_example' # str | Construct UUID
slot_idx = 56 # int | Slot Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Slot Get Properties (CID)
    api_response = api_instance.get_construct_slot(construct_uuid, slot_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_construct_slot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construct_uuid** | **str**| Construct UUID | 
 **slot_idx** | **int**| Slot Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**SlotData**](SlotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_construct_slot_version**
> ShotData get_construct_slot_version(construct_uuid, slot_idx, version_idx, level=level)

Shot Get Properties (VRS)

Get the properties of the n-th Shot in Slot with Index in Construct with UUID.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
construct_uuid = 'construct_uuid_example' # str | Construct UUID
slot_idx = 56 # int | Slot Index
version_idx = 56 # int | Version index, representing the nth version in a slot
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Get Properties (VRS)
    api_response = api_instance.get_construct_slot_version(construct_uuid, slot_idx, version_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_construct_slot_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construct_uuid** | **str**| Construct UUID | 
 **slot_idx** | **int**| Slot Index | 
 **version_idx** | **int**| Version index, representing the nth version in a slot | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotData**](ShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_construct_slot_versions**
> ShotsData get_construct_slot_versions(construct_uuid, slot_idx, level=level)

Shot List (VRS)

Get a list of Shots in Slot with Index in Construct with UUID.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
construct_uuid = 'construct_uuid_example' # str | Construct UUID
slot_idx = 56 # int | Slot Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot List (VRS)
    api_response = api_instance.get_construct_slot_versions(construct_uuid, slot_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_construct_slot_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construct_uuid** | **str**| Construct UUID | 
 **slot_idx** | **int**| Slot Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotsData**](ShotsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_construct_slots**
> SlotsData get_construct_slots(construct_uuid, level=level)

Slot List (CID)

Get all Slots in the Constuct with UUID (CID).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
construct_uuid = assimilate_client.Uuid() # Uuid | Construct UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Slot List (CID)
    api_response = api_instance.get_construct_slots(construct_uuid, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_construct_slots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construct_uuid** | [**Uuid**](.md)| Construct UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**SlotsData**](SlotsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_constructs**
> ConstructsData get_constructs(level=level)

Construct List

Get list of Constructs in the active Group

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Construct List
    api_response = api_instance.get_constructs(level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_constructs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ConstructsData**](ConstructsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_constructs_current**
> ConstructData get_constructs_current(level=level)

Construct Current Get

Get the active Construct in the active Group.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Construct Current Get
    api_response = api_instance.get_constructs_current(level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_constructs_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ConstructData**](ConstructData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_constructs_current_reference**
> ReferenceShotData get_constructs_current_reference()

Construct Current Get Reference shot

Get the reference shot of the current Construct.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()

try:
    # Construct Current Get Reference shot
    api_response = api_instance.get_constructs_current_reference()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_constructs_current_reference: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReferenceShotData**](ReferenceShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_constructs_reference**
> ReferenceShotData get_constructs_reference(construct_uuid)

Construct Get Reference shot

Get the reference shot of a construct with the specified UUID.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
construct_uuid = 'construct_uuid_example' # str | Construct UUID

try:
    # Construct Get Reference shot
    api_response = api_instance.get_constructs_reference(construct_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_constructs_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construct_uuid** | **str**| Construct UUID | 

### Return type

[**ReferenceShotData**](ReferenceShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> GroupData get_group(group_uuid, level=level)

Group Get Properties

Get the properties of Group with UUID

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
group_uuid = assimilate_client.Uuid() # Uuid | Group UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Group Get Properties
    api_response = api_instance.get_group(group_uuid, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uuid** | [**Uuid**](.md)| Group UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**GroupData**](GroupData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_current**
> GroupData get_group_current(level=level)

Group Current Get

Get the properties of the active Ggroup in the current loaded Project

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Group Current Get
    api_response = api_instance.get_group_current(level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_group_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**GroupData**](GroupData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> GroupsData get_groups(level=level)

Group List

Get list of Groups in the current loaded Project.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Group List
    api_response = api_instance.get_groups(level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**GroupsData**](GroupsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> ProjectList get_projects()

Project List

Get the list of available projects.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()

try:
    # Project List
    api_response = api_instance.get_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_current**
> ProjectData get_projects_current()

Project Current

Get the current loaded project. Returns an error when no project is currently loaded.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()

try:
    # Project Current
    api_response = api_instance.get_projects_current()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects_current: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProjectData**](ProjectData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_item**
> ProjectData get_projects_item(project_id)

Project Get Properties

Get the properties of the project specified by name. Returns an error when another project is currently loaded.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
project_id = 'project_id_example' # str | Project name

try:
    # Project Get Properties
    api_response = api_instance.get_projects_item(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project name | 

### Return type

[**ProjectData**](ProjectData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot**
> ShotData get_shot(shot_id, level=level)

Shot Get Properties

Get the properties of the Shot with UUID

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Get Properties
    api_response = api_instance.get_shot(shot_id, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_shot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotData**](ShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_color**
> ColorgradeData get_shot_color(shot_id, level=level)

Shot Get Color Properties

Get the color properties of the Shot with UUID

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Get Color Properties
    api_response = api_instance.get_shot_color(shot_id, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_shot_color: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ColorgradeData**](ColorgradeData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_input**
> InputData get_shot_input(shot_id, input_idx)

Input Get Properties

Get the properties of the n-th Input of the Shot with UUID.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
input_idx = 56 # int | index of the nth input

try:
    # Input Get Properties
    api_response = api_instance.get_shot_input(shot_id, input_idx)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_shot_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **input_idx** | **int**| index of the nth input | 

### Return type

[**InputData**](InputData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_inputs**
> InputsData get_shot_inputs(shot_id)

Inputs List

Get the list of input SDhots of the Shot with UUID.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID

try:
    # Inputs List
    api_response = api_instance.get_shot_inputs(shot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_shot_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 

### Return type

[**InputsData**](InputsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_layer**
> LayerData get_shot_layer(shot_id, layer_idx, level=level)

Shot Get Layer Properties

Get the properties of the layer at the specified index for the Shot with UUID

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Get Layer Properties
    api_response = api_instance.get_shot_layer(shot_id, layer_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_shot_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**LayerData**](LayerData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_layer_canvas**
> CanvasData get_shot_layer_canvas(shot_id, layer_idx, level=level)

Shot Layer Get Canvas Properties

Get the canvas properties of the Shot with UUID at the specified layer index.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Layer Get Canvas Properties
    api_response = api_instance.get_shot_layer_canvas(shot_id, layer_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_shot_layer_canvas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**CanvasData**](CanvasData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_layer_color**
> ColorgradeData get_shot_layer_color(shot_id, layer_idx, level=level)

Shot Layer Get Color Properties

Get the color properties of the Shot with UUID at the specified layer index.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Layer Get Color Properties
    api_response = api_instance.get_shot_layer_color(shot_id, layer_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_shot_layer_color: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ColorgradeData**](ColorgradeData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_layer_fill**
> FillData get_shot_layer_fill(shot_id, layer_idx, level=level)

Shot Layer Get Fill Properties

Get the fill properties of the Shot with UUID at the specified layer index.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Layer Get Fill Properties
    api_response = api_instance.get_shot_layer_fill(shot_id, layer_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_shot_layer_fill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**FillData**](FillData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_layer_matte**
> MatteData get_shot_layer_matte(shot_id, layer_idx, level=level)

Shot Layer Get Matte Properties

Get the matte properties of the Shot with UUID at the specified layer index.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Layer Get Matte Properties
    api_response = api_instance.get_shot_layer_matte(shot_id, layer_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_shot_layer_matte: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**MatteData**](MatteData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_layers**
> LayersData get_shot_layers(shot_id, level=level)

Shot Get Layers Properties

Get the layers properties of the Shot with UUID

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Get Layers Properties
    api_response = api_instance.get_shot_layers(shot_id, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_shot_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**LayersData**](LayersData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_construct**
> move_construct(body, construct_uuid)

Construct Move

Move the Construct with UUID to another position in the Project tree

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.MoveConstructData() # MoveConstructData | json with construct move data
construct_uuid = assimilate_client.Uuid() # Uuid | Construct UUID

try:
    # Construct Move
    api_instance.move_construct(body, construct_uuid)
except ApiException as e:
    print("Exception when calling ProjectsApi->move_construct: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoveConstructData**](MoveConstructData.md)| json with construct move data | 
 **construct_uuid** | [**Uuid**](.md)| Construct UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_construct_current_slot_version**
> move_construct_current_slot_version(body, slot_idx, version_idx)

Shot Move (CC)

Mover the n-th Shot in the m-th Slot in the current Construct (CC) to a different location.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.MoveShotData() # MoveShotData | json with move data for the shot
slot_idx = 56 # int | Slot Index
version_idx = 56 # int | version Index, representing the nth version

try:
    # Shot Move (CC)
    api_instance.move_construct_current_slot_version(body, slot_idx, version_idx)
except ApiException as e:
    print("Exception when calling ProjectsApi->move_construct_current_slot_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoveShotData**](MoveShotData.md)| json with move data for the shot | 
 **slot_idx** | **int**| Slot Index | 
 **version_idx** | **int**| version Index, representing the nth version | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_construct_slot_version**
> move_construct_slot_version(body, construct_uuid, slot_idx, version_idx)

Shot Move (VRS)

Move the n-th Shot in Slot with Index in Construct with UUI to a different location.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.MoveShotData() # MoveShotData | json with move data for the shot
construct_uuid = 'construct_uuid_example' # str | Construct UUID
slot_idx = 56 # int | Slot Index
version_idx = 56 # int | Version index, representing the nth version in a slot

try:
    # Shot Move (VRS)
    api_instance.move_construct_slot_version(body, construct_uuid, slot_idx, version_idx)
except ApiException as e:
    print("Exception when calling ProjectsApi->move_construct_slot_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoveShotData**](MoveShotData.md)| json with move data for the shot | 
 **construct_uuid** | **str**| Construct UUID | 
 **slot_idx** | **int**| Slot Index | 
 **version_idx** | **int**| Version index, representing the nth version in a slot | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_constructs_current**
> move_constructs_current(body)

Construct Current Move

Move the current selected Construct to a different position in the Project tree

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.MoveConstructData() # MoveConstructData | json with construct move data

try:
    # Construct Current Move
    api_instance.move_constructs_current(body)
except ApiException as e:
    print("Exception when calling ProjectsApi->move_constructs_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoveConstructData**](MoveConstructData.md)| json with construct move data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_group**
> move_group(body, group_uuid)

Group Move

Move the Group with UUID to a different position in the Project tree.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.MoveGroupData() # MoveGroupData | json with move data
group_uuid = assimilate_client.Uuid() # Uuid | Group UUID

try:
    # Group Move
    api_instance.move_group(body, group_uuid)
except ApiException as e:
    print("Exception when calling ProjectsApi->move_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoveGroupData**](MoveGroupData.md)| json with move data | 
 **group_uuid** | [**Uuid**](.md)| Group UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_group_current**
> move_group_current(body)

Group Current Move

Move the current selected Group to a different position in the Project tree

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.MoveGroupData() # MoveGroupData | json with move data

try:
    # Group Current Move
    api_instance.move_group_current(body)
except ApiException as e:
    print("Exception when calling ProjectsApi->move_group_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoveGroupData**](MoveGroupData.md)| json with move data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_layer**
> move_layer(body, shot_id, layer_idx)

Layer Move

Move the layer to a specified position at the layer sta for the Shot with UUID.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.MoveLayerData() # MoveLayerData | json with move data for the layer
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index

try:
    # Layer Move
    api_instance.move_layer(body, shot_id, layer_idx)
except ApiException as e:
    print("Exception when calling ProjectsApi->move_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoveLayerData**](MoveLayerData.md)| json with move data for the layer | 
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_shot**
> move_shot(body, shot_id, level=level)

Shot Move

Mover the Shot with UUID to a specific location. Depending on the current location of the Shot it might be necessary to make a copy of the Shot when moving it.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.MoveShotData() # MoveShotData | json with shot move data
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Move
    api_instance.move_shot(body, shot_id, level=level)
except ApiException as e:
    print("Exception when calling ProjectsApi->move_shot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoveShotData**](MoveShotData.md)| json with shot move data | 
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_shot_layer_canvas**
> reset_shot_layer_canvas(shot_id, layer_idx)

Shot Layer Reset Canvas Properties

Reset the canvas properties of the Shot with UUID at the specified layer index.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index

try:
    # Shot Layer Reset Canvas Properties
    api_instance.reset_shot_layer_canvas(shot_id, layer_idx)
except ApiException as e:
    print("Exception when calling ProjectsApi->reset_shot_layer_canvas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_shot_layer_color**
> reset_shot_layer_color(shot_id, layer_idx)

Shot Layer Reset Color Properties

Reset the color properties of the Shot with UUID at the specified layer index.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index

try:
    # Shot Layer Reset Color Properties
    api_instance.reset_shot_layer_color(shot_id, layer_idx)
except ApiException as e:
    print("Exception when calling ProjectsApi->reset_shot_layer_color: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_shot_layer_fill**
> reset_shot_layer_fill(shot_id, layer_idx)

Shot Layer Reset Fill Properties

Reset the fill properties of the Shot with UUID at the specified layer index.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index

try:
    # Shot Layer Reset Fill Properties
    api_instance.reset_shot_layer_fill(shot_id, layer_idx)
except ApiException as e:
    print("Exception when calling ProjectsApi->reset_shot_layer_fill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_shot_layer_matte**
> reset_shot_layer_matte(shot_id, layer_idx)

Shot Layer Reset Matte Properties

Reset the matte properties of the Shot with UUID at the specified layer index.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index

try:
    # Shot Layer Reset Matte Properties
    api_instance.reset_shot_layer_matte(shot_id, layer_idx)
except ApiException as e:
    print("Exception when calling ProjectsApi->reset_shot_layer_matte: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **select_construct**
> ConstructData select_construct(construct_uuid)

Construct Select

Make Construct with UUI the active construct. The Group the Construct is part of will automaticaly be selected as well.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
construct_uuid = assimilate_client.Uuid() # Uuid | Construct UUID

try:
    # Construct Select
    api_response = api_instance.select_construct(construct_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->select_construct: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construct_uuid** | [**Uuid**](.md)| Construct UUID | 

### Return type

[**ConstructData**](ConstructData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **select_group**
> GroupData select_group(group_uuid, level=level)

Group Select

Make Group with UUID the active group, with the first Timeline in the group the active Timeline.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
group_uuid = assimilate_client.Uuid() # Uuid | Group UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Group Select
    api_response = api_instance.select_group(group_uuid, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->select_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uuid** | [**Uuid**](.md)| Group UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**GroupData**](GroupData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_construct**
> ConstructData set_construct(body, construct_uuid, level=level)

Construct Set Properties

Set properties of the Construct with UUID

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ConstructData() # ConstructData | json with construct data
construct_uuid = assimilate_client.Uuid() # Uuid | Construct UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Construct Set Properties
    api_response = api_instance.set_construct(body, construct_uuid, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_construct: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConstructData**](ConstructData.md)| json with construct data | 
 **construct_uuid** | [**Uuid**](.md)| Construct UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ConstructData**](ConstructData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_construct_current_output**
> ShotData set_construct_current_output(body, output_id, level=level)

Output Set Properties (CC)

Update the properties of Output with UUID in the current Construct (CC).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ShotData() # ShotData | json output node data
output_id = assimilate_client.Uuid() # Uuid | Output Node UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Output Set Properties (CC)
    api_response = api_instance.set_construct_current_output(body, output_id, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_construct_current_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShotData**](ShotData.md)| json output node data | 
 **output_id** | [**Uuid**](.md)| Output Node UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotData**](ShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_construct_current_slot**
> SlotData set_construct_current_slot(body, slot_idx, level=level)

Slot Set Properties (CC)

Update the properties of the n-th Slot in the current Construct (CC).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.SlotData() # SlotData | json with slot data
slot_idx = 56 # int | Slot Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Slot Set Properties (CC)
    api_response = api_instance.set_construct_current_slot(body, slot_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_construct_current_slot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SlotData**](SlotData.md)| json with slot data | 
 **slot_idx** | **int**| Slot Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**SlotData**](SlotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_construct_current_slot_version**
> ShotData set_construct_current_slot_version(body, slot_idx, version_idx, level=level)

Shot Set Properties (CC)

Update the properties of the n-th shot in the m-th Slot in the current Construct (CC).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ShotData() # ShotData | json with shot data
slot_idx = 56 # int | Slot Index
version_idx = 56 # int | version Index, representing the nth version
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Set Properties (CC)
    api_response = api_instance.set_construct_current_slot_version(body, slot_idx, version_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_construct_current_slot_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShotData**](ShotData.md)| json with shot data | 
 **slot_idx** | **int**| Slot Index | 
 **version_idx** | **int**| version Index, representing the nth version | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotData**](ShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_construct_output**
> ShotData set_construct_output(body, construct_uuid, output_id, level=level)

Output Set Properties (CID)

Update the properties of Output with UUID in the Constuct with UUID (CID).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ShotData() # ShotData | json output node data
construct_uuid = assimilate_client.Uuid() # Uuid | Construct UUID
output_id = assimilate_client.Uuid() # Uuid | Output Node UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Output Set Properties (CID)
    api_response = api_instance.set_construct_output(body, construct_uuid, output_id, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_construct_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShotData**](ShotData.md)| json output node data | 
 **construct_uuid** | [**Uuid**](.md)| Construct UUID | 
 **output_id** | [**Uuid**](.md)| Output Node UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotData**](ShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_construct_slot**
> SlotData set_construct_slot(body, construct_uuid, slot_idx, level=level)

Slot Set Properties (CID)

Update the properties of SLot with Index a Constuct with UUID (CID).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.SlotData() # SlotData | json with playmode data
construct_uuid = 'construct_uuid_example' # str | Construct UUID
slot_idx = 56 # int | Slot Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Slot Set Properties (CID)
    api_response = api_instance.set_construct_slot(body, construct_uuid, slot_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_construct_slot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SlotData**](SlotData.md)| json with playmode data | 
 **construct_uuid** | **str**| Construct UUID | 
 **slot_idx** | **int**| Slot Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**SlotData**](SlotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_construct_slot_version**
> ShotData set_construct_slot_version(body, construct_uuid, slot_idx, version_idx, level=level)

Shot Set Properties (VRS)

Update the properties of the n-th Shot in Slot with Index in Construct with UUID.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ShotData() # ShotData | json with shot data
construct_uuid = 'construct_uuid_example' # str | Construct UUID
slot_idx = 56 # int | Slot Index
version_idx = 56 # int | Version index, representing the nth version in a slot
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Set Properties (VRS)
    api_response = api_instance.set_construct_slot_version(body, construct_uuid, slot_idx, version_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_construct_slot_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShotData**](ShotData.md)| json with shot data | 
 **construct_uuid** | **str**| Construct UUID | 
 **slot_idx** | **int**| Slot Index | 
 **version_idx** | **int**| Version index, representing the nth version in a slot | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotData**](ShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_constructs_current**
> ConstructData set_constructs_current(body, level=level)

Construct Current Set Properties

Set the properties of the active Construct in the active Group.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ConstructData() # ConstructData | json with construct data
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Construct Current Set Properties
    api_response = api_instance.set_constructs_current(body, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_constructs_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConstructData**](ConstructData.md)| json with construct data | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ConstructData**](ConstructData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_constructs_current_reference**
> ReferenceShotData set_constructs_current_reference(body)

Construct Current Set reference shot

Set the reference shot of the current Construct.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ReferenceShotData() # ReferenceShotData | json with reference shot data

try:
    # Construct Current Set reference shot
    api_response = api_instance.set_constructs_current_reference(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_constructs_current_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReferenceShotData**](ReferenceShotData.md)| json with reference shot data | 

### Return type

[**ReferenceShotData**](ReferenceShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_constructs_reference**
> ReferenceShotData set_constructs_reference(body, construct_uuid)

Construct Current Set reference shot

Set the reference shot of a construct with the specified UUID.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ReferenceShotData() # ReferenceShotData | json with reference shot data
construct_uuid = 'construct_uuid_example' # str | Construct UUID

try:
    # Construct Current Set reference shot
    api_response = api_instance.set_constructs_reference(body, construct_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_constructs_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReferenceShotData**](ReferenceShotData.md)| json with reference shot data | 
 **construct_uuid** | **str**| Construct UUID | 

### Return type

[**ReferenceShotData**](ReferenceShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_group**
> GroupData set_group(body, group_uuid, level=level)

Group Set Properties

Set the properties of Group with UUID

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.GroupData() # GroupData | json with group data
group_uuid = assimilate_client.Uuid() # Uuid | Group UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Group Set Properties
    api_response = api_instance.set_group(body, group_uuid, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupData**](GroupData.md)| json with group data | 
 **group_uuid** | [**Uuid**](.md)| Group UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**GroupData**](GroupData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_projects_item**
> set_projects_item(body, project_id)

Project Set Properties

Update the properties of the project specified by name. Returns an error when another project is currently loaded.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ProjectData() # ProjectData | json with project data
project_id = 'project_id_example' # str | Project name

try:
    # Project Set Properties
    api_instance.set_projects_item(body, project_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_projects_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectData**](ProjectData.md)| json with project data | 
 **project_id** | **str**| Project name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_shot**
> ShotData set_shot(body, shot_id, level=level)

Shot Set Properties

Update the properties of the Shot with UUID

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ShotData() # ShotData | json with shot data
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Set Properties
    api_response = api_instance.set_shot(body, shot_id, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_shot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShotData**](ShotData.md)| json with shot data | 
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ShotData**](ShotData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_shot_color**
> ColorgradeData set_shot_color(body, shot_id, level=level)

Shot Set Color Properties

Update the color properties of the Shot with UUID

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ColorgradeData() # ColorgradeData | json with shot data
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Set Color Properties
    api_response = api_instance.set_shot_color(body, shot_id, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_shot_color: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ColorgradeData**](ColorgradeData.md)| json with shot data | 
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ColorgradeData**](ColorgradeData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_shot_input**
> InputData set_shot_input(shot_id, input_idx)

Input Set Properties

Update the properties of the n-th Input of the Shot with UUID.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
input_idx = 56 # int | index of the nth input

try:
    # Input Set Properties
    api_response = api_instance.set_shot_input(shot_id, input_idx)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_shot_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **input_idx** | **int**| index of the nth input | 

### Return type

[**InputData**](InputData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_shot_layer**
> LayerData set_shot_layer(body, shot_id, layer_idx, level=level)

Shot Set Layer Properties

Update the properties of the layer at the specified index for the Shot with UUID

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.LayerData() # LayerData | json with shot data
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Set Layer Properties
    api_response = api_instance.set_shot_layer(body, shot_id, layer_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_shot_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayerData**](LayerData.md)| json with shot data | 
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**LayerData**](LayerData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_shot_layer_canvas**
> CanvasData set_shot_layer_canvas(body, shot_id, layer_idx, level=level)

Shot Layer Set  Canvas Properties

Update the canvas properties of the Shot with UUID at the specified layer index.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.CanvasData() # CanvasData | json with shot data
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Layer Set  Canvas Properties
    api_response = api_instance.set_shot_layer_canvas(body, shot_id, layer_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_shot_layer_canvas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CanvasData**](CanvasData.md)| json with shot data | 
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**CanvasData**](CanvasData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_shot_layer_color**
> ColorgradeData set_shot_layer_color(body, shot_id, layer_idx, level=level)

Shot Layer Set  Color Properties

Update the color properties of the Shot with UUID at the specified layer index.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.ColorgradeData() # ColorgradeData | json with shot data
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Layer Set  Color Properties
    api_response = api_instance.set_shot_layer_color(body, shot_id, layer_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_shot_layer_color: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ColorgradeData**](ColorgradeData.md)| json with shot data | 
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**ColorgradeData**](ColorgradeData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_shot_layer_fill**
> FillData set_shot_layer_fill(body, shot_id, layer_idx, level=level)

Shot Layer Set  Fill Properties

Update the fill properties of the Shot with UUID at the specified layer index.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.FillData() # FillData | json with Fill data
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Layer Set  Fill Properties
    api_response = api_instance.set_shot_layer_fill(body, shot_id, layer_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_shot_layer_fill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FillData**](FillData.md)| json with Fill data | 
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**FillData**](FillData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_shot_layer_matte**
> MatteData set_shot_layer_matte(body, shot_id, layer_idx, level=level)

Shot Layer Set  Matte Properties

Update the matte properties of the Shot with UUID at the specified layer index.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ProjectsApi()
body = assimilate_client.MatteData() # MatteData | json with Matte data
shot_id = assimilate_client.Uuid() # Uuid | Shot UUID
layer_idx = 56 # int | Layer Index
level = 'level_example' # str | Level of detail. If set to ALL the full data model is returned. (optional)

try:
    # Shot Layer Set  Matte Properties
    api_response = api_instance.set_shot_layer_matte(body, shot_id, layer_idx, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_shot_layer_matte: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MatteData**](MatteData.md)| json with Matte data | 
 **shot_id** | [**Uuid**](.md)| Shot UUID | 
 **layer_idx** | **int**| Layer Index | 
 **level** | **str**| Level of detail. If set to ALL the full data model is returned. | [optional] 

### Return type

[**MatteData**](MatteData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

