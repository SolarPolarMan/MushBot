import os
import settings
import _util

async def run(client, msg, args):
    if msg.author.id in serverinfo.modList or serverinfo.codererList:
        _util.makeBlankFile("ascii.txt")
        if settings.divider not in msg.content:
            if len(args) > 2:
                call = args[0]
                response = " ".join(args[1:])
                with open("ascii.txt", "ab") as a:
                    a.write((call+settings.divider+response+os.linesep).encode('utf-8'))
                    await client.send_message(msg.channel, "Added command:`"+call+"`")
            else:
                await client.send_message(msg.channel, "Example: `" + settings.activator + "addcommand lenny ( ͡° ͜ʖ ͡°)`")
        else:
            #if they're trying to break it.
            await client.send_message(msg.channel, settings.malicous)
