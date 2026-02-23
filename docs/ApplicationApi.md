# assimilate_client.ApplicationApi

All URIs are relative to *https://virtserver.swaggerhub.com/AssimilateInc/AMSREST/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_application_command**](ApplicationApi.md#add_application_command) | **POST** /application/commands | Custom Command Add
[**delete_application_command**](ApplicationApi.md#delete_application_command) | **DELETE** /application/commands/{command_id} | Custom Command Delete
[**get_application_commands**](ApplicationApi.md#get_application_commands) | **GET** /application/commands | Custom Commands List
[**get_application_command**](ApplicationApi.md#get_application_command) | **GET** /application/commands/{command_id} | Custom Command Get
[**set_application_command**](ApplicationApi.md#set_application_command) | **PUT** /application/commands/{command_id} | Custom Command Update
[**add_application_render_queue_item**](ApplicationApi.md#add_application_render_queue_item) | **PUT** /application/render/{output_UUID} | Render Queue Item Add
[**add_application_render_queue_item_start**](ApplicationApi.md#add_application_render_queue_item_start) | **POST** /application/render/{output_UUID} | Render Queue Item Add Start
[**delete_application_render_queue_item**](ApplicationApi.md#delete_application_render_queue_item) | **DELETE** /application/render/{output_UUID} | Render Queue Item Delete
[**do_application_player_enter_shot**](ApplicationApi.md#do_application_player_enter_shot) | **POST** /application/player/entershot/{shot_UUID} | Player Enter Shot
[**do_application_player_enter_slot**](ApplicationApi.md#do_application_player_enter_slot) | **POST** /application/player/enterslot/{slot_IDX} | Player Enter Slot
[**do_application_player_enter_timeline**](ApplicationApi.md#do_application_player_enter_timeline) | **POST** /application/player/entertimeline/{construct_UUID} | Player Enter Timeline (CID)
[**do_application_player_enter_timeline_current**](ApplicationApi.md#do_application_player_enter_timeline_current) | **POST** /application/player/entertimeline | Player Enter Timeline (CC)
[**do_application_player_exit**](ApplicationApi.md#do_application_player_exit) | **POST** /application/player/exit | Player Exit
[**do_application_project_enter**](ApplicationApi.md#do_application_project_enter) | **POST** /application/project/enter/{projectID} | Project Enter
[**do_application_project_exit**](ApplicationApi.md#do_application_project_exit) | **POST** /application/project/exit | Project Exit
[**do_application_render_delete_media_item**](ApplicationApi.md#do_application_render_delete_media_item) | **POST** /application/render/deletemedia/{output_UUID} | Render Queue Item Delete Media
[**do_application_render_snapshot**](ApplicationApi.md#do_application_render_snapshot) | **POST** /application/tools/image | Render Snapshot
[**do_application_render_start**](ApplicationApi.md#do_application_render_start) | **POST** /application/render/start | Render Queue Start
[**do_application_render_stop**](ApplicationApi.md#do_application_render_stop) | **POST** /application/render/stop | Render Queue Stop
[**do_application_render_stop_item**](ApplicationApi.md#do_application_render_stop_item) | **POST** /application/render/stop{output_UUID} | Render Queue Item Stop
[**do_application_restart**](ApplicationApi.md#do_application_restart) | **POST** /application/restart | Application Restart
[**do_application_shutdown**](ApplicationApi.md#do_application_shutdown) | **POST** /application/shutdown | Application Shutdown
[**get_application_player_playmode**](ApplicationApi.md#get_application_player_playmode) | **GET** /application/player/playmode | Player Get Mode
[**get_application_render_queue**](ApplicationApi.md#get_application_render_queue) | **GET** /application/render | Render Queue List
[**get_application_render_queue_item**](ApplicationApi.md#get_application_render_queue_item) | **GET** /application/render/{output_UUID} | Render Queue Item Get
[**post_application_render_start_item**](ApplicationApi.md#post_application_render_start_item) | **POST** /application/render/start/{output_UUID} | Render Queue Item Start
[**set_application_player_playmode**](ApplicationApi.md#set_application_player_playmode) | **PUT** /application/player/playmode | Player Set Mode

# **add_application_render_queue_item**
> RenderQueueItem add_application_render_queue_item(output_uuid)

Render Queue Item Add

Add the Output with UUID as Item to the Render Queue. Returns an error is the item is not found or not a valid output node.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()
output_uuid = assimilate_client.Uuid() # Uuid | Output node UUID

try:
    # Render Queue Item Add
    api_response = api_instance.add_application_render_queue_item(output_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->add_application_render_queue_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_uuid** | [**Uuid**](.md)| Output node UUID | 

### Return type

[**RenderQueueItem**](RenderQueueItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_application_render_queue_item_start**
> RenderQueueItem add_application_render_queue_item_start(output_uuid, body=body)

Render Queue Item Add Start

Add the Output with UUID as Item to the Render Queue and start rendering it. Returns an error is the Output is not found or not a valid Output.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()
output_uuid = assimilate_client.Uuid() # Uuid | Output node UUID
body = assimilate_client.DeleteMediaData() # DeleteMediaData | json with delete_existing_media boolean (optional)

try:
    # Render Queue Item Add Start
    api_response = api_instance.add_application_render_queue_item_start(output_uuid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->add_application_render_queue_item_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_uuid** | [**Uuid**](.md)| Output node UUID | 
 **body** | [**DeleteMediaData**](DeleteMediaData.md)| json with delete_existing_media boolean | [optional] 

### Return type

[**RenderQueueItem**](RenderQueueItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_render_queue_item**
> delete_application_render_queue_item(output_uuid)

Render Queue Item Delete

Remove the Item with UUID from the Render Queue. Returns an error is the item is not found in the queue.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()
output_uuid = assimilate_client.Uuid() # Uuid | Output node UUID

try:
    # Render Queue Item Delete
    api_instance.delete_application_render_queue_item(output_uuid)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_application_render_queue_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_uuid** | [**Uuid**](.md)| Output node UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_application_player_enter_shot**
> do_application_player_enter_shot(shot_uuid)

Player Enter Shot

Enter the player with the Shot with UUID.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()
shot_uuid = assimilate_client.Uuid() # Uuid | Shot UUID

try:
    # Player Enter Shot
    api_instance.do_application_player_enter_shot(shot_uuid)
except ApiException as e:
    print("Exception when calling ApplicationApi->do_application_player_enter_shot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_uuid** | [**Uuid**](.md)| Shot UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_application_player_enter_slot**
> do_application_player_enter_slot(slot_idx)

Player Enter Slot

Enter the player with the Slot with Index in the current Construct.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()
slot_idx = assimilate_client.Uuid() # Uuid | Slot index

try:
    # Player Enter Slot
    api_instance.do_application_player_enter_slot(slot_idx)
except ApiException as e:
    print("Exception when calling ApplicationApi->do_application_player_enter_slot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot_idx** | [**Uuid**](.md)| Slot index | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_application_player_enter_timeline**
> do_application_player_enter_timeline(construct_uuid)

Player Enter Timeline (CID)

Enter the player with the Construct\\Timeline with UUID (CID).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()
construct_uuid = assimilate_client.Uuid() # Uuid | Construct UUID

try:
    # Player Enter Timeline (CID)
    api_instance.do_application_player_enter_timeline(construct_uuid)
except ApiException as e:
    print("Exception when calling ApplicationApi->do_application_player_enter_timeline: %s\n" % e)
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

# **do_application_player_enter_timeline_current**
> do_application_player_enter_timeline_current()

Player Enter Timeline (CC)

Enter the player with the current Timeline/Construct (CC)

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()

try:
    # Player Enter Timeline (CC)
    api_instance.do_application_player_enter_timeline_current()
except ApiException as e:
    print("Exception when calling ApplicationApi->do_application_player_enter_timeline_current: %s\n" % e)
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

# **do_application_player_exit**
> do_application_player_exit()

Player Exit

Exit the player and return to the current Construct menu.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()

try:
    # Player Exit
    api_instance.do_application_player_exit()
except ApiException as e:
    print("Exception when calling ApplicationApi->do_application_player_exit: %s\n" % e)
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

# **do_application_project_enter**
> do_application_project_enter(project_id)

Project Enter

Enter the project specified by name. When another project is currently loaded, it is first unloaded.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()
project_id = 'project_id_example' # str | Project name

try:
    # Project Enter
    api_instance.do_application_project_enter(project_id)
except ApiException as e:
    print("Exception when calling ApplicationApi->do_application_project_enter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_application_project_exit**
> do_application_project_exit()

Project Exit

Exit the currently loaded project.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()

try:
    # Project Exit
    api_instance.do_application_project_exit()
except ApiException as e:
    print("Exception when calling ApplicationApi->do_application_project_exit: %s\n" % e)
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

# **do_application_render_delete_media_item**
> do_application_render_delete_media_item(output_uuid)

Render Queue Item Delete Media

Delete the media of the Queue Item with UUID. Returns an error when the node is not present in the Queue.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()
output_uuid = assimilate_client.Uuid() # Uuid | Output node UUID

try:
    # Render Queue Item Delete Media
    api_instance.do_application_render_delete_media_item(output_uuid)
except ApiException as e:
    print("Exception when calling ApplicationApi->do_application_render_delete_media_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_uuid** | [**Uuid**](.md)| Output node UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_application_render_snapshot**
> str do_application_render_snapshot(body)

Render Snapshot

Generate an image from the Shot with UUID at the specified frame postion, using the default snapshot format settings.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()
body = assimilate_client.ImageSnapshot() # ImageSnapshot | json with the Shot UUID, frame position and render path

try:
    # Render Snapshot
    api_response = api_instance.do_application_render_snapshot(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->do_application_render_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageSnapshot**](ImageSnapshot.md)| json with the Shot UUID, frame position and render path | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/jpeg, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_application_render_start**
> do_application_render_start(body=body)

Render Queue Start

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()
body = assimilate_client.DeleteMediaData() # DeleteMediaData | Start processing the render queue. If delete_existing_media is true, existing media will be deleted before rendering. (optional)

try:
    # Render Queue Start
    api_instance.do_application_render_start(body=body)
except ApiException as e:
    print("Exception when calling ApplicationApi->do_application_render_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteMediaData**](DeleteMediaData.md)| Start processing the render queue. If delete_existing_media is true, existing media will be deleted before rendering. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_application_render_stop**
> do_application_render_stop()

Render Queue Stop

Stop rendering all queue items.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()

try:
    # Render Queue Stop
    api_instance.do_application_render_stop()
except ApiException as e:
    print("Exception when calling ApplicationApi->do_application_render_stop: %s\n" % e)
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

# **do_application_render_stop_item**
> do_application_render_stop_item(output_uuid)

Render Queue Item Stop

Stop rendering the Queue Item with UUID. Returns an error when the node is not present in the Queue.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()
output_uuid = assimilate_client.Uuid() # Uuid | Output node UUID

try:
    # Render Queue Item Stop
    api_instance.do_application_render_stop_item(output_uuid)
except ApiException as e:
    print("Exception when calling ApplicationApi->do_application_render_stop_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_uuid** | [**Uuid**](.md)| Output node UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_application_restart**
> do_application_restart()

Application Restart

Restart the application (Windows only).

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()

try:
    # Application Restart
    api_instance.do_application_restart()
except ApiException as e:
    print("Exception when calling ApplicationApi->do_application_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_application_shutdown**
> do_application_shutdown()

Application Shutdown

Shutdown the application.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()

try:
    # Application Shutdown
    api_instance.do_application_shutdown()
except ApiException as e:
    print("Exception when calling ApplicationApi->do_application_shutdown: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_player_playmode**
> PlaymodeData get_application_player_playmode()

Player Get Mode

Get the current Player mode. Returns an error when not in the Player.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()

try:
    # Player Get Mode
    api_response = api_instance.get_application_player_playmode()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_application_player_playmode: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PlaymodeData**](PlaymodeData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_render_queue**
> RenderQueueList get_application_render_queue()

Render Queue List

List all current Items in the Render Queue.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()

try:
    # Render Queue List
    api_response = api_instance.get_application_render_queue()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_application_render_queue: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RenderQueueList**](RenderQueueList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_render_queue_item**
> RenderQueueItem get_application_render_queue_item(output_uuid)

Render Queue Item Get

Get the status of the Queue Item with UUID. Returns an error is the item is not present in the Render Queue.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()
output_uuid = assimilate_client.Uuid() # Uuid | Output node UUID

try:
    # Render Queue Item Get
    api_response = api_instance.get_application_render_queue_item(output_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_application_render_queue_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_uuid** | [**Uuid**](.md)| Output node UUID | 

### Return type

[**RenderQueueItem**](RenderQueueItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_application_render_start_item**
> post_application_render_start_item(output_uuid, body=body)

Render Queue Item Start

Start processing the Queue Item with UUID. If delete_existing_media is true, existing media will be deleted before rendering. Returns an error if the UUID does not references a valid output node.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()
output_uuid = assimilate_client.Uuid() # Uuid | Output node UUID
body = assimilate_client.DeleteMediaData() # DeleteMediaData | json with delete_existing_media boolean (optional)

try:
    # Render Queue Item Start
    api_instance.post_application_render_start_item(output_uuid, body=body)
except ApiException as e:
    print("Exception when calling ApplicationApi->post_application_render_start_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_uuid** | [**Uuid**](.md)| Output node UUID | 
 **body** | [**DeleteMediaData**](DeleteMediaData.md)| json with delete_existing_media boolean | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_application_player_playmode**
> set_application_player_playmode(body)

Player Set Mode

Set the current Player mode. Returns an error when not in the Player.

### Example
```python
from __future__ import print_function
import time
import assimilate_client
from assimilate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = assimilate_client.ApplicationApi()
body = assimilate_client.PlaymodeData() # PlaymodeData | json with playmode data

try:
    # Player Set Mode
    api_instance.set_application_player_playmode(body)
except ApiException as e:
    print("Exception when calling ApplicationApi->set_application_player_playmode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlaymodeData**](PlaymodeData.md)| json with playmode data |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_commands**
> CustomCommandsList get_application_commands()

Custom Commands List

Get the list of registered Custom Commands including their type, executable path, arguments, and behavioral settings.

### Example
```python
from __future__ import print_function
import assimilate_client
from assimilate_client.rest import ApiException

api_instance = assimilate_client.ApplicationApi()

try:
    api_response = api_instance.get_application_commands()
    for cmd in api_response.commands:
        print("  %s -> %s" % (cmd.name, cmd.file))
except ApiException as e:
    print("Exception: %s" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomCommandsList**](CustomCommandsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_application_command**
> CustomCommandData add_application_command(body)

Custom Command Add

Register a new Custom Command. The command will appear in the context menu and can be invoked on selected shots or as a post-render action.

### Example
```python
from __future__ import print_function
import assimilate_client
from assimilate_client.rest import ApiException

api_instance = assimilate_client.ApplicationApi()
body = assimilate_client.CustomCommandData(
    name="S2ROTO",
    type="application",
    file="/Library/Application Support/RogueLabs/S2ROTO/s2roto.py",
    interpreter="python3",
    arguments='"$ARG1" "$ARG2"',
    wait_till_finished=True,
    xml_export="selection",
    require_selection=True
)

try:
    api_response = api_instance.add_application_command(body)
    print("Registered: %s" % api_response.name)
except ApiException as e:
    print("Exception: %s" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomCommandData**](CustomCommandData.md)| Custom command definition |

### Return type

[**CustomCommandData**](CustomCommandData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_command**
> CustomCommandData get_application_command(command_id)

Custom Command Get

Get the properties of a specific Custom Command by name or index.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| Command name or index |

### Return type

[**CustomCommandData**](CustomCommandData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_application_command**
> CustomCommandData set_application_command(command_id, body)

Custom Command Update

Update the properties of an existing Custom Command.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| Command name or index |
 **body** | [**CustomCommandData**](CustomCommandData.md)| Updated command properties |

### Return type

[**CustomCommandData**](CustomCommandData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_command**
> delete_application_command(command_id)

Custom Command Delete

Remove a Custom Command by name or index.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| Command name or index |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

