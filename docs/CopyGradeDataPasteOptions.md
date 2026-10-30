# CopyGradeDataPasteOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **bool** | Copy all elements of the source grade (node controls, grade, curves, vectors, media source, LUT, layers, framing and their animations). | [optional] 
**node_controls** | **bool** | Copy the node specific controls (e.g. plugin controls, decode options for media reader nodes, etc.). | [optional] 
**non_default** | **bool** | Option to only copy the node specific controls that differ from their default value (+ Non-Default). | [optional] 
**grade** | **bool** | Copy the primary grade (Levels, Color and Numeric menus). | [optional] 
**grade_animations** | **bool** | Include all animations of the primary grade in the grade (+Animation). | [optional] 
**curves** | **bool** | Copy the settings from the Curves menu. | [optional] 
**vectors** | **bool** | Copy the settings from the Vectors menu (remapping). | [optional] 
**media_source** | **bool** | Copy the settings of the source remapping of the source node. | [optional] 
**lut** | **bool** | Copy the LUT settings. | [optional] 
**layers** | **bool** | Copy all the layers from the source grade. | [optional] 
**layer_animations** | **bool** | Also copy the animations of the layers (+Animation). | [optional] 
**add_layers** | **bool** | Add the copied layers to the destination node, leaving the existing layers intact (Add Layers). | [optional] 
**fill_matte** | **bool** | Also copy the fill and matte texture nodes of the layers (+Texture). | [optional] 
**framing** | **bool** | Copy the framing settings. | [optional] 
**framing_animations** | **bool** | Also copy the animations of the framing (+Animation). | [optional] 
**animations_relative** | **bool** | Paste animation channels relative to the in-point of the destination node instead of using the absolute position of the source Shot (A. Relative). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

