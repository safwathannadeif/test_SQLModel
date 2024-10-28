import asyncio
import httpx
import json

from src.cfg.cfg_app import config

out_File=""
async def select_from_json(symbol):
    req_url=config['request_Selec_from_json']['url'] ##'http://localhost:800/select_stock_json/test_stock_symb}'
    async with httpx.AsyncClient() as client:
        outr= await client.get(req_url+symbol)
    print(f"Response Status:{outr.status_code}")
    json_formatted_str =  json.dumps(outr.json(), indent=0)
    return json_formatted_str

select_symbol="CSCO1"
json_list_out= asyncio.run(select_from_json(select_symbol))       #
print(f"json file from select\n:{json_list_out }")