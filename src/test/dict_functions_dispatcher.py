# Functions as dictionary values dispatcher

import asyncio


async def do_ping(arg):
    return 'Pong, {0}!'.format(arg)


async def do_sum(a: int, b: int):
    # await(0.01)
    return a + b


async def just_print(*args):
    return "This is Gfg's value"


dispatch = {
    'ping': do_ping,
    'sum': do_sum,
    'jprint': just_print

}


async def process_command(cmd_key, *arg):
    return (await dispatch[cmd_key](*arg))


out0 = asyncio.run(process_command("jprint"))
print(f"process_command just_print= {out0}")

out1 = asyncio.run(process_command("ping", "aaa"))
print(f"process_command ping= {out1}")

out2 = asyncio.run(process_command("sum", 10, 100))
print(f"process_command sum= {out2}")
#
