# G.O.H
# Joe Jagger

# External Imports
from govee_api_ble import GoveeDevice
import json
from pathlib import Path
from socket import gethostname
from quart import Quart,request, jsonify,send_from_directory,redirect
from uvicorn import run


# Internal Imports
from core.utils import str2bool


app = Quart(__name__)

CONFIG = json.loads(Path("./config.json").read_text("utf-8"))



try:
    device = GoveeDevice(CONFIG.get("govee_mac"))
except Exception as e:
    print(f"[FATAL] Failed to initalize Govee BLE API Device: {e}")
    exit(1)



@app.get("/")
async def dash():
    return await send_from_directory(Path("./static"),"dash.html")

@app.get("/goh/api/set_power")
async def set_power():
    state = str2bool(request.args.get("state","false"))
    try:
        device.setPower(state)
        return jsonify({
            "message":f"Set lights to {state} successfully."
        })
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({
            "message":"Internal server error. Check STDOUT."
        })

@app.get("/goh/api/set_brightness")
async def set_brightness():
    percent = request.args.get("percent",None)

    if not percent:
        return jsonify({
            "message":"Please pass ?percent=0-100"
        })

    try:
        device.setBrightness(int(percent))

        return jsonify({
            "message":f"Set lights to {percent} successfully."
        })
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({
            "message":"Internal server error. Check STDOUT."
        })


@app.get("/goh/api/set_colour")
async def set_colour():
    rgb = request.args.get("rgb",None)
    segments = request.args.get("segments",None)

    if not rgb:
        return jsonify({
            "message":"Please pass ?rgb=rgb-values-here"
        })
    if segments:
        segments = [int(x) for x in segments.split("-")]

    rgb = [int(x) for x in rgb.split("-")]

    if len(rgb) != 3:
        return jsonify({
            "message":"Failed to split rgb internally. Ensure '000-000-000' layout."
        })

    try:
        if not segments:
            device.setColor(c=rgb)
        else:
            device.setColor(c=rgb,segment=segments)
        return jsonify({
            "message":f"Set lights to {rgb} successfully."
        })
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({
            "message":"Internal server error. Check STDOUT."
        })

if __name__ == "__main__":
    print("GOH ASGI Starting.")
    run("main:app",port=8585,host="0.0.0.0",workers=2)