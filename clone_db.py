import urllib.request
import json

base_url = "https://worldcup2026-263c9-default-rtdb.asia-southeast1.firebasedatabase.app"
try:
    print("Fetching data from wc2026.json...")
    req = urllib.request.Request(f"{base_url}/wc2026.json")
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
    
    print("Uploading data to wc2026_v2.json...")
    req2 = urllib.request.Request(f"{base_url}/wc2026_v2.json", data=json.dumps(data).encode(), method="PUT")
    req2.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req2) as response2:
        print("Successfully cloned DB to wc2026_v2")
except Exception as e:
    print("Error:", e)
