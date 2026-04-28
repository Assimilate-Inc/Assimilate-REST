#!/usr/bin/python3

import json
import sys

from assimilate_client import Configuration, ApiClient
from assimilate_client.api import SystemApi, ProjectsApi, ApplicationApi
from assimilate_client.models import *
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
    
    cur_sel = projects_api.get_construct_current_selected_shots()
    #print (cur_sel)
    
    ref_data = projects_api.get_constructs_current_reference()
    #print (ref_data)
    
    if not ref_data.ref_uuid:
        print ("❌ No reference shot set in the editor")
        sys.exit(1)
        
    play_mode = app_api.get_application_player_playmode()
    #print (play_mode)
    
    if cur_sel.selection:
        sel_item = cur_sel.selection[0]
        
        # create video wall shot
        wall_type_uuid = ShotData(
            type_uuid = '94F2DF40-D364-4EAB-8C85-851A2859A8F0', 
            name = "Side by side compare",
            handles = ShotDataHandles(frame_in = 0, frame_out = play_mode.length))
        video_wall = projects_api.add_shot(body = wall_type_uuid)
        
        shot = projects_api.get_shot(shot_uuid = sel_item.uuid)

        # Add a copy of the current shot as input 0 to the video_wall
        projects_api.set_shot_input(
            shot_uuid = video_wall.uuid,
            input_idx = 0,
            body = InputData(input_uuid = sel_item.uuid, slip = shot.handles.frame_in, create_copy = True))
           
        # Add the reference shot as input 1 to the video wall
        slot_pos = play_mode.frame - play_mode.shot_frame + shot.handles.frame_in
        projects_api.set_shot_input(
            shot_uuid = video_wall.uuid,
            input_idx = 1,
            body = InputData( input_uuid = ref_data.ref_uuid, slip = slot_pos))

        move_data = MoveShotData(slot_idx = sel_item.slot_idx, version_idx = 1, construct_uuid = cur_sel.construct_uuid)
        projects_api.move_shot(shot_uuid = video_wall.uuid, body = move_data)
        
        # Set control values for border size and background color
        controls_data = ControlsData(
            controls=[
                ControlData(id="size",  value=10),
                ControlData(id="color", value={"a": 1, "r": 0.20, "g": 0.20, "b": 0.20})
            ]
        )

        projects_api.set_shot_controls(
            shot_uuid=video_wall.uuid,
            body=controls_data
        )
        
        # Select the video wall node in the version stack
        app_api.set_application_player_playmode(body = PlaymodeData(version_idx = 1))
        
    print ("Done")

except ApiException as e:
    if e.body:
        error_dict = json.loads(e.body.decode('utf-8'))
        print("Error details:")
        print(json.dumps(error_dict, indent=4))
    else:
        print("No error body returned")
