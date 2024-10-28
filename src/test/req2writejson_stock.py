import asyncio
import os
import aiofiles as aiof
import httpx
import requests
import json

from src.cfg.cfg_app import config

out_File=""
async def make_json_file():
    req_url=config['request_Server']['url'] #url="http://localhost:800/lisStock/"
    #out_json= requests.get(req_url).json()
    async with httpx.AsyncClient() as client:
        outr = await client.get(req_url)

    json_formatted_str =  json.dumps(outr.json(), indent=0)
    print(json_formatted_str)
    ## C:\Users\Public\py_dev\fastapi\test_SQLModel\src\test\req.py
    data_folder= config['data']['data_folder']
    print(f"Using Data Folder: {data_folder}")
    out_File= f"{data_folder}/josn_test.dat"

    async with aiof.open(out_File, "w") as out:
        await out.write(json_formatted_str)
        await out.flush()
    print(f"{out_File }  Created")

asyncio.run(make_json_file())
print(f"json file created path:{os.path.basename(out_File) }====>FQN= {os.path.abspath((out_File))}")
