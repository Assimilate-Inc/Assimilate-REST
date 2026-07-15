#!/usr/bin/python3

"""
Author: Assimilate BV
Date: 15 July 2026
Description: Assimilate Product Suite REST-API example that shows how to render the selected shot and load the rendered shot back into a tray in the project.
             This script goes along a Custom Command (RenderSelectedShot.acc) that will ask the user to select the format (PNG/ProRes), ouotput folder and Tray name before envoking the script.
             The user selection are passed as command line paramters to the script.
"""

import json
import time
import sys

from assimilate_client import Configuration, ApiClient
from assimilate_client.api import ProjectsApi, ApplicationApi
from assimilate_client.models import *
from assimilate_client.rest import ApiException
from datetime import datetime

# get command line paramters 
render_type = 0
if(len(sys.argv) > 2):
    render_type = int(sys.argv[2])

render_folder = datetime.now().strftime("%H%M%S")
if(len(sys.argv) > 4):
    render_folder = sys.argv[4]

load_into_tray = "MyTray"
if(len(sys.argv) > 6):
    load_into_tray = sys.argv[6]

# initialize the API client
config = Configuration()
config.host = "http://192.168.100.61:8080/APIV2"  # your endpoint
api_client = ApiClient(config)
projects_api = ProjectsApi(api_client)
app_api = ApplicationApi(api_client)

try:
    # get selectiion
    select = projects_api.get_construct_current_selected_shots(level="ALL")
    if select.selection:
        num_selection = len(select.selection)
        if num_selection > 0:

            render_node = None
            if render_type == 0:
                # create PNG render node
                sd = ShotData(type_uuid="00000000-0000-0000-0000-000000000004", 
                            name="CC Render Tiff", 
                            output=ShotDataOutput(components=4, extention="tif", filespec=render_folder + "\\#sname.#frame[6].#ext", format=0),
                            color_format=ShotDataColorFormat(colorspace="Rec709", eotf="Gamma 2.4"))
                render_node = projects_api.add_shot(sd)

            elif render_type == 1:
                # create ProRes render node
                ctrl_list = []
                ctrl_list.append(ControlData(id="vcodec", value="Apple ProRes 422"))
                ctrl_list.append(ControlData(id="palpha", value="False"))

                print("start")
                sd = ShotData(type_uuid="4327bcc5-91af-4955-92ce-455522eb84b3", 
                            name=select.selection[0].shot.name, 
                            output=ShotDataOutput(components=4, outputpath="$RENDER$\\"+render_folder, filespec="#name.#ext", extention="mov", format=16777483),
                            color_format=ShotDataColorFormat(colorspace="Rec709", eotf="Gamma 2.4"),
                            controls=ctrl_list)
                render_node = projects_api.add_shot(sd)
                #print(render_node)

            if render_node:
                # set first selected as input to render node
                inp = InputData(create_copy=True, input_uuid=select.selection[0].shot.uuid)
                projects_api.set_shot_input(inp, render_node.uuid, 0)

                # add render to queue
                rst = RenderQueueSettings(output_uuid=render_node.uuid, delete_existing_media=True) 
                queue_itm = app_api.new_application_render_queue_item_start(body=rst)

                # wait for render to finish
                print("processing", end="")
                busy = True
                while busy:
                    queue_itm = app_api.get_application_render_queue_item(queue_itm.uuid)
                    if queue_itm.status == "Idle" or queue_itm.status == "waiting" or queue_itm.status == "processing":
                        print(".", end="", flush=True)
                        time.sleep(1)
                    else:
                        busy = False
                print("")

                # get the render result
                render_results = app_api.get_application_render_queue_item_results(queue_itm.uuid)
                if render_results:
                    # get first file from the render results
                    num_files = len(render_results.files)
                    if num_files > 0:
                        # create a new shot node with it, then move it to the specified tray
                        sd = ShotData(file=render_results.files[0].file)
                        new_node = projects_api.add_shot(sd)

                        move_shot = MoveShotData(tray_name = load_into_tray, tray_position = 0, tray_create = True)
                        projects_api.move_shot(shot_uuid=new_node.uuid, body=move_shot)

                        print("Done")
                    else:
                        print("No render file")
                else:
                    print("No render results")

            else:
                print("No render")
    else:
        print("No selection")        
    
except ApiException as e:
    # probably not in the player / no current shot
    if e.body:
        error_dict = json.loads(e.body.decode('utf-8'))
        print("Error details:")
        print(json.dumps(error_dict, indent=4))
    else:
        print("No error body returned")

