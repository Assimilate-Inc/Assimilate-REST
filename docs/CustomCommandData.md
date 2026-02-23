# CustomCommandData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name of the command (appears in menus). Must be unique. |
**type** | **str** | Command type: "application" (context menu) or "postrender" (after render) | [optional] [default: "application"]
**file** | **str** | Absolute path to the executable or script |
**arguments** | **str** | Argument template. Use $ARG1 for input XML, $ARG2 for output XML | [optional] [default: "$ARG1" "$ARG2"]
**interpreter** | **str** | Interpreter to invoke the command with (e.g. "python3", "/bin/bash") | [optional]
**wait_till_finished** | **bool** | Block until command completes before processing output XML | [optional] [default: true]
**xml_export** | **str** | Data scope: "selection", "all", or "none" | [optional] [default: "selection"]
**require_selection** | **bool** | Only show command when shots are selected | [optional] [default: true]
**enabled** | **bool** | Whether the command is active and visible | [optional] [default: true]

## Command Types

### Application Commands

Invoked from the right-click context menu on selected shots. Receives two arguments:

- `$ARG1` — Path to the input XML containing the selected shot data
- `$ARG2` — Path where the command should write its output XML

### Post-Render Commands

Triggered automatically after an output node finishes rendering. Receives one argument:

- `$ARG1` — Path to the render info XML

## Example

```python
command = {
    "name": "S2ROTO",
    "type": "application",
    "file": "/Library/Application Support/RogueLabs/S2ROTO/s2roto.py",
    "interpreter": "python3",
    "arguments": "\"$ARG1\" \"$ARG2\"",
    "wait_till_finished": True,
    "xml_export": "selection",
    "require_selection": True
}
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
