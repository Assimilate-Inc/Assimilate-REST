# ShotDataOutput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outputpath** | **str** | Output folder for the render | [optional] 
**filespec** | **str** | File specification / mask for the render. Include mask codes to dynamically create the output filename. See the documentation for details. | [optional] 
**format** | **int** | Format mask is a combination of bit depth and component type. 0 (8bit), 1 (10bit), 2 (16bit int), 3 (16bit float), 4 (32bit float). Note that most media formats only allow for specific combinations of bit depth and type. Not all combinations are valid. Check the sotware UI for valid combinations. | [optional] 
**components** | **int** | Channel count (3 for RGB, 4 for RGBA) | [optional] 
**extention** | **str** | File extension | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

