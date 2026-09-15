#!/usr/bin/python3

"""
Author: Assimilate BV
Date: 14 September 2026
Description: Assimilate Product Suite REST-API example that shows how to add a node to the render tree and render it. 
             The scripts checks the resolution of the current construct and first creates a Transformer node directly after the Main output node of the timeline 
             to either upscale or downscale the timeline output before rendering. Also the Apply option of the Transfomer node is set to ensure the timeline / input is 
             converted to Rec709 (if not already). After the Transformer node, the ProRes render node is added, which is then added to the render queue and the render is started. 
"""

import json
import time
import sys

from assimilate_client import Configuration, ApiClient
from assimilate_client.api import ProjectsApi, ApplicationApi
from assimilate_client.models import *
from assimilate_client.rest import ApiException
from datetime import datetime

# default render sub folder - optionally can use first command line parameter
render_folder = datetime.now().strftime("%H%M%S")
if(len(sys.argv) > 1):
    render_folder = sys.argv[1]

# initialize the API client
config = Configuration()
config.host = "http://192.168.100.61:8080/APIV2"  # your endpoint
api_client = ApiClient(config)
projects_api = ProjectsApi(api_client)
app_api = ApplicationApi(api_client)

try:
    # get current construct and list all outputs
    construct = projects_api.get_constructs_current()
    if(construct):
        # if timeline is HD or smaller, we upscale to UHD, otherwise downscale to HD
        scaleX = 1.0
        scaleY = 1.0
        if(construct.resolution.w <= 1920.0):
            scaleX = 3840.0 / construct.resolution.w * 100.0
            scaleY = 2160.0 / construct.resolution.h * 100.0
        else:
            scaleX = 1920.0 / construct.resolution.w * 100.0
            scaleY = 1080.0 / construct.resolution.h * 100.0

        # create a transformer node to resize the timeline output and ensure it is converted to rec709
        trs_ctrl = []
        trs_ctrl.append(ControlData(id="xScale", value=scaleX))
        trs_ctrl.append(ControlData(id="yScale", value=scaleY))

        trs_sd = ShotData(type_uuid="00000000-0000-0000-0000-000000000004", 
                    name="Resize Timeline", 
                    output=ShotDataOutput(components=4, outputpath="$RENDER$\\"+render_folder),
                    color_format=ShotDataColorFormat(colorspace="Rec709", eotf="Gamma 2.4", apply=True),
                    controls=trs_ctrl)
        trs_node = projects_api.add_construct_current_output(trs_sd)

        if(trs_node):
            # create ProRes render node
            prs_ctrl = []
            prs_ctrl.append(ControlData(id="vcodec", value="Apple ProRes 422"))
            prs_ctrl.append(ControlData(id="palpha", value="False"))

            prs_inp = InputData(create_copy=False, input_uuid=trs_node.uuid, index=0)

            prs_sd = ShotData(type_uuid="4327bcc5-91af-4955-92ce-455522eb84b3", 
                        name="ProRes Render", 
                        output=ShotDataOutput(components=4, outputpath="$RENDER$\\"+render_folder, filespec="#name.#ext", extention="mov", format=16777483),
                        color_format=ShotDataColorFormat(colorspace="Rec709", eotf="Gamma 2.4", apply=True),
                        controls=prs_ctrl, inputs=[prs_inp])

            prs_node = projects_api.add_construct_current_output(prs_sd)

            if(prs_node):
                # start render of  the ProRes node
                rnd_set = RenderQueueSettings(output_uuid=prs_node.uuid, delete_existing_media=True)
                que_itm = app_api.new_application_render_queue_item_start(body=rnd_set)
                if(que_itm):
                    print("Render started for ProRes node: " + prs_node.name)
                else:
                    print("Failed to start the Prores render")

            else:
                print("Failed to create ProRes node")
        else:
            print("Failed to create Transformer node")
    else:
        print("No current Construct found")
    
except ApiException as e:
    # probably not in the player / no current shot
    if e.body:
        error_dict = json.loads(e.body.decode('utf-8'))
        print("Error details:")
        print(json.dumps(error_dict, indent=4))
    else:
        print("No error body returned")

