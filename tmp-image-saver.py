import obspython as obs
import json
import os
from PIL import Image as im
 
 
sh = obs.obs_get_signal_handler()
 
expPath = "D:/Program Files/obs-studio/data/obs-plugins/frontend-tools/scripts/tmp/"
 
#obs.script_log(obs.LOG_DEBUG,str(imgs))
 
def onSrcCr(data):
    src = obs.calldata_source(data,"source")
    srcName = obs.obs_source_get_name(src)
    settings = obs.obs_source_get_settings(src)
 
    tmpPath = ""
    isFile = obs.obs_data_get_json(settings).find('"file":')
    if isFile > 0:
        tmpPath = json.loads(obs.obs_data_get_json(settings))['file']
    isTmp = tmpPath.find('AppData/Local/Temp')
 
    isImg = 0
    isImg += tmpPath.find('.png') + 1
    isImg += tmpPath.find('.jpg') + 1
    isImg += tmpPath.find('.bmp') + 1
    isImg += tmpPath.find('.gif') + 1
 
    if isTmp > -1 and isImg > 0 and not tmpPath == "":
        #obs.script_log(obs.LOG_DEBUG,'file is image and temporary!')
        bild = im.open(tmpPath)
        bild.save(expPath+srcName,"PNG")
 
        settings2 = obs.obs_data_create()
        obs.obs_data_set_string(settings, "file", expPath+srcName)
        obs.obs_source_update(src, settings)
 
    obs.obs_data_release(settings)
obs.signal_handler_connect(sh,"source_create",onSrcCr)
 
def climgBtn(props,prop):
    with os.scandir(expPath) as i:
        for entry in i:
            if not entry.name.startswith('.') and entry.is_file():
                os.remove(expPath+entry.name)
 
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, "button", "Empty tmp folder", climgBtn)
    return props