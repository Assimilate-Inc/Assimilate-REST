# ViewOptionsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lock** | **bool** | Lock the view to current selected node, allowing to navigate and alter other nodes in a composition while maintaining the view. | [optional] 
**output** | **bool** | View the (main) output node of the timeline. This allows to view the final result of a (multi layered) timeline including framing and final grading and transforms, while working on selected timeline shot. | [optional] 
**spherical** | **bool** | Enable / disable spherical (360) view mode. | [optional] 
**grade** | **bool** | Enable / disable applying the color grade. | [optional] 
**overlay** | **bool** | Toggle showing layer or plugin overlays in the view on/off. | [optional] 
**display_lut** | **bool** | Toggle applying the display LUT (if set) on/off. | [optional] 
**channel_mask** | **str** | Channel mask for the view: combination of R (Red), G (Green), B (Blue), M (Monochrome), L (Luminance), A (Alpha). Leaving the mask empty shows RGB channels. Enabling the Alpha channel, displays black when full opaque and white when full transparent. The mask is applied after the color grade and display LUT. | [optional] 
**layout** | [**ViewportLayoutData**](ViewportLayoutData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

