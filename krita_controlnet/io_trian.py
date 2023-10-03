import json
import io
import os
plugin_dir = os.path.dirname(__file__)
default_json_path = os.path.join(plugin_dir, "autosave_config.json")
print(default_json_path)
with open("autosave_config.json","r") as f:
    js = json.load(f)
with open("autosave_config.json","w") as f:
    js["auto save"] = False
    f.write(json.dumps(js))
    

    