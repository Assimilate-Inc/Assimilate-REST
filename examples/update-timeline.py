#!/usr/bin/python3

import json
import pkg_resources

from assimilate_client import *
from assimilate_client.api import *
from assimilate_client.models import *
from assimilate_client.rest import *

config = Configuration()
config.host = "http://127.0.0.1:8080/APIV2"  # your endpoint
api_client = ApiClient(config)

system_api = SystemApi(api_client)
projects_api = ProjectsApi(api_client)
app_api = ApplicationApi(api_client)

'''
This code processes the currently selected shots in a construct and applies transitions 
and scaling animations to each shot.
First, it retrieves the current construct and reads its resolution, which is used to
calculate scaling so that each shot fills the construct frame.

For each selected shot:
    The corresponding slot is retrieved and its duration is set to a fixed length.
    A transition is applied between consecutive slots:
        If the current shot follows directly after the previous one, a dissolve transition is applied.
        Otherwise, a hard cut is used.

    The updated slot configuration is saved back to the construct.

Next, the shot version for the slot is retrieved and its handle-out value is updated to match the slot length.

The code then calculates a uniform scale factor so the shot fully covers the construct resolution, 
with a small additional scale applied to create a subtle zoom effect.

Finally, a scale animation is applied to the shot by creating keyframes for both the X and Y scale channels,
starting at the initial scale and ending at the slightly increased scale over the duration of the slot.
The updated shot data is then saved.

'''

SLOT_LENGTH = 80
TRANSITION_FRAMES = 10
SCALE_PADDING = 1.04

def build_scale_channel(channel_id, start_key, end_key):
    return AnimationChannelData(
        id=channel_id,
        pre="C",
        post="C",
        key_frames=[start_key, end_key],
    )


def apply_transition(slot, is_continuous):
    if slot.transition is None:
        slot.transition = SlotDataTransition(after=0,before=0,type="Cut")
 
    if is_continuous:
        slot.transition.after = TRANSITION_FRAMES
        slot.transition.before = TRANSITION_FRAMES
        slot.transition.type = "Dissolve"
    else:
        slot.transition.after = 0
        slot.transition.before = 0
        slot.transition.type = "Cut"

def process_shot(item, prev_item, cw, ch):
    slot = projects_api.get_construct_current_slot(slot_idx=item.slot_idx)
    slot.length = SLOT_LENGTH

    is_continuous = (
        prev_item is not None
        and prev_item.slot_idx + 1 == item.slot_idx
    )
    apply_transition(slot, is_continuous)

    projects_api.set_construct_current_slot(
        slot_idx=item.slot_idx,
        body=slot,
    )

    shot = projects_api.get_construct_current_slot_version(
        slot_idx=item.slot_idx,
        version_idx=item.version_idx,
    )

    shot.handles.src_out = slot.length - 1

    print(f"Shot size: {shot.size.width} {shot.size.height}")


    scale = max(cw / shot.size.width, ch / shot.size.height)
    to_scale = scale * SCALE_PADDING

    start_key = KeyFrameData(
        li=0.0, lv=scale,
        ki=0.0, kv=scale,
        ri=TRANSITION_FRAMES, rv=scale,
    )

    end_key = KeyFrameData(
        li=slot.length - 1 - TRANSITION_FRAMES,
        lv=to_scale,
        ki=slot.length - 1,
        kv=to_scale,
        ri=slot.length - 1,
        rv=to_scale,
    )

    shot.framing = ShotDataFraming(
        scale=Vector2(x=scale, y=scale),
        animation=AnimationData(
            channels=[
                build_scale_channel("Scale X", start_key, end_key),
                build_scale_channel("Scale Y", start_key, end_key),
            ]
        ),
    )

    projects_api.set_shot(shot_uuid=item.uuid, body=shot)

try:
    server_version = system_api.get_system_properties().rest_version
    print(f"Server version: {server_version}")
    
    client_version = pkg_resources.get_distribution("assimilate_client").version
    print(f"Client version: {client_version}\n")

    if (server_version != client_version):
        print("❌ Error server and client versin are not the same")
    
    construct = projects_api.get_constructs_current()
    cw, ch = construct.resolution.w, construct.resolution.h

    print(f"Construct size: {cw} {ch}\n")

    selected_shots = projects_api.get_construct_current_selected_shots()
    selection = selected_shots.selection

    if selection:
        for i, item in enumerate(selection):
            prev_item = selection[i - 1] if i > 0 else None
            process_shot(item, prev_item, cw, ch)
        
     
except ApiException as e:
    if e.body:
        error_dict = json.loads(e.body.decode('utf-8'))
        print("Error details:")
        print(json.dumps(error_dict, indent=4))
    else:
        print("No error body returned")
    