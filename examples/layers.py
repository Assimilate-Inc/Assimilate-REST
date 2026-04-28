#!/usr/bin/python3

import json

from assimilate_client import Configuration, ApiClient
from assimilate_client.api import SystemApi, ProjectsApi, ApplicationApi
from assimilate_client.models import MoveLayerData
from assimilate_client.rest import ApiException
from importlib.metadata import version

config = Configuration()
config.host = "http://127.0.0.1:8080/APIV2"  # your endpoint
api_client = ApiClient(config)

system_api = SystemApi(api_client)
projects_api = ProjectsApi(api_client)
app_api = ApplicationApi(api_client)

try:
    
    # get the server version and client version
    server_version = system_api.get_system_properties().rest_version
    print(f"Server version: {server_version}")
    
    pip_version = version("assimilate_client")
    print(f"Client version: {pip_version}")
    
    
    # get the first shot in the construct
    shot = projects_api.get_construct_current_slot_version(slot_idx = 0, version_idx = 0)
    print (shot.uuid)
    
    # get the layers of a shot
    layers = projects_api.get_shot_layers(shot_uuid = shot.uuid).layers
    #print (layers)
    
    num_layers = len(layers)
    print (f"number of layers: {num_layers}")
    
    # reset all layers
    for i in range(num_layers):
        layer = layers[i]
        print (f"get layer {i}")
        projects_api.reset_shot_layer_canvas(shot_uuid = shot.uuid, layer_idx = i)
        print (f"layer[{i}] reset canvas")
        if layer.group is False:
            projects_api.reset_shot_layer_color(shot_uuid = shot.uuid, layer_idx = i)
            print (f"layer[{i}] reset color")
            projects_api.reset_shot_layer_fill(shot_uuid = shot.uuid, layer_idx = i)
            print (f"layer[{i}] reset fill")
            projects_api.reset_shot_layer_matte(shot_uuid = shot.uuid, layer_idx = i)
            print (f"layer[{i}] reset matte")
            
    
    # delete all layers
    for i in reversed(range(num_layers)):
        projects_api.delete_shot_layer(shot_uuid = shot.uuid, layer_idx = i)
        print (f"delete layer[{i}]")
    
    # create the layers and groups
    groups_idx = []  # Initialize a list to keep track of group indices
    for i in range(num_layers):
        if layers[i].group:
            #create group
            groups_idx.append(i)  # Add the current group index to the list
            projects_api.add_shot_layer_group(shot_uuid = shot.uuid, body = layers[i] )
            print (f"create group[{i}]")
        else:   
            #create layer
            projects_api.add_shot_layer(shot_uuid = shot.uuid, body = layers[i])
            print (f"create layer[{i}]")
        
        if layers[i].parent is not None:
            # move layer or group to the parent group
            # groups are numbered. The root group is numbered 0 and the first group is numbered 1 etc
            grp_nmbr = groups_idx.index(layers[i].parent) + 1 # Find the group number
            move_to = MoveLayerData(group_index = grp_nmbr)
            projects_api.move_layer(shot_uuid = shot.uuid, layer_idx = i, body = move_to)
            if layers[i].group: 
                print (f"move group[{i}] to parent {layers[i].parent}")
            else:  
                print (f"move layer[{i}] to parent {layers[i].parent}")
            
    print ("Done")

except ApiException as e:
    if e.body:
        error_dict = json.loads(e.body.decode('utf-8'))
        print("Error details:")
        print(json.dumps(error_dict, indent=4))
    else:
        print("No error body returned")
