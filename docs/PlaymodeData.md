# PlaymodeData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio** | **str** | Audio settings | [optional] 
**fps** | **float** | Playback framerate | [optional] 
**construct_uuid** | [**Uuid**](Uuid.md) |  | [optional] 
**frame** | **int** | Current timeline frame position | [optional] 
**timecodec** | **str** | Current timelinetimecode (readonly) | [optional] 
**slot_idx** | **int** | Current Slot index being played in the timeline | [optional] 
**shot_uuid** | [**Uuid**](Uuid.md) |  | [optional] 
**shot_frame** | **int** | Current frame position in the Shot being played | [optional] 
**shot_timecode** | **str** | Current record timecode of the Shot being played (readonly) | [optional] 
**version_idx** | **int** | Version index of the shot in the Player. | [optional] 
**session** | **str** | Session type the player is in. One of &#x27;timeline,output,derived_output,shot,compare,slot&#x27; (readonly). | [optional] 
**length** | **int** | Length of the media in the Player in frames | [optional] 
**loop** | **str** | Loop mode | [optional] 
**mark_in** | **int** | View range in-point | [optional] 
**mark_out** | **int** | View range out-point | [optional] 
**mode** | **str** | Playback mode | [optional] 
**range** | **bool** | View range is active / not | [optional] 
**speed** | **int** | Playback multiplier | [optional] 
**timeline** | **str** | Name of the construct being played | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

