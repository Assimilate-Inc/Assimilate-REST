# ViewOptionsBData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source node of the B view. &#x27;Output&#x27; refers to the main output node of the current timeline. &#x27;Current&#x27; shows the active node, the same as the left view (but with potential different view options). &#x27;Tray&#x27; refers to the current selected tray item. &#x27;Custom&#x27; requires shot_uuid to be set and allows to select any show to be viewed. &#x27;Reference&#x27; refers to the shot set in the Editor as reference for the current timeline. &#x27;All versions&#x27; refers to a viedeowall node creted from all versions in the current slot. | [optional] 
**shot_uuid** | [**Uuid**](Uuid.md) |  | [optional] 
**over_mode** | [**OverModeData**](OverModeData.md) |  | [optional] 
**spherical** | **bool** | Enable / disable spherical (360) view mode. | [optional] 
**grade** | **bool** | Enable / disable applying the color grade. | [optional] 
**link** | **bool** | Link the pan/zoom of both views. | [optional] 
**display_lut** | **bool** | Toggle applying the display LUT (if set) on/off. | [optional] 
**channel_mask** | **str** | Channel mask for the view: combination of R (Red), G (Green), B (Blue), M (Monochrome), L (Luminance), A (Alpha). Leaving the mask empty shows RGB channels. Enabling the Alpha channel, displays black when full opaque and white when full transparent. The mask is applied after the color grade and display LUT. | [optional] 
**layout** | [**ViewportLayoutData**](ViewportLayoutData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

