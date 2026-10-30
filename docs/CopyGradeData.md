# CopyGradeData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_uuid** | [**Uuid**](Uuid.md) |  | 
**dst_uuid** | [**Uuid**](Uuid.md) |  | 
**src_layer_idx** | **int** | Index of the layer of the source Shot to copy from. When omitted or negative, the primary grade of the source Shot is used, including all layers and node controls. | [optional] 
**dst_layer_idx** | **int** | Index of the layer of the destination Shot to copy to. When omitted or negative, the primary grade of the destination Shot is targeted. | [optional] 
**paste_options** | [**CopyGradeDataPasteOptions**](CopyGradeDataPasteOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

