# ShotData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | [**Uuid**](Uuid.md) |  | [optional] 
**type_uuid** | [**Uuid**](Uuid.md) |  | [optional] 
**file** | **str** | Full filename of the Shot media | [optional] 
**name** | **str** | Name of the Shot | [optional] 
**node_preset_file** | **str** | File path to the .pls (plugin preset) file. Input only. | [optional] 
**color_settings_file** | **str** | File path to the .ccr (color settings) file. Input only | [optional] 
**reel_id** | **str** | Reel identifier | [optional] 
**scene** | **str** | Scene identifier | [optional] 
**take** | **str** | Take identifier | [optional] 
**circled** | **bool** | Circle Shot y/n | [optional] 
**fps** | **float** | Frames per second of the shot | [optional] 
**fps_multiplier** | **float** | FPS multiplier for retiming | [optional] 
**fps_offset** | **float** | FPS offset for retiming | [optional] 
**fps_mode** | **int** | FPS mode for retiming (0 &#x3D; Nearest Frame, 1 &#x3D; Rolling Mix) | [optional] 
**frame_tc** | **int** | Frame number of the Shot timecode | [optional] 
**timecode** | [**Timecode**](Timecode.md) |  | [optional] 
**length** | **int** | Length of the Shot in frames | [optional] 
**handles** | [**ShotDataHandles**](ShotDataHandles.md) |  | [optional] 
**size** | [**ShotDataSize**](ShotDataSize.md) |  | [optional] 
**aspect** | **float** | Aspect ratio of the Shot | [optional] 
**output** | [**ShotDataOutput**](ShotDataOutput.md) |  | [optional] 
**framing** | [**ShotDataFraming**](ShotDataFraming.md) |  | [optional] 
**view** | [**ShotDataView**](ShotDataView.md) |  | [optional] 
**orientation** | [**ShotDataOrientation**](ShotDataOrientation.md) |  | [optional] 
**color_format** | [**ShotDataColorFormat**](ShotDataColorFormat.md) |  | [optional] 
**colorgrade** | [**ColorgradeData**](ColorgradeData.md) |  | [optional] 
**camera** | [**CameraData**](CameraData.md) |  | [optional] 
**mos** | **bool** | Mit Ohne Sound Shot | [optional] 
**audio** | [**ShotDataAudio**](ShotDataAudio.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**notes** | [**list[NoteData]**](NoteData.md) | Notes of the Shot | [optional] 
**staging** | [**StagingData**](StagingData.md) |  | [optional] 
**inputs** | [**InputsData**](InputsData.md) |  | [optional] 
**controls** | [**list[ControlData]**](ControlData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

