import asyncio

async def hanle_asyncclient(reader,writer):
    print('Client : ',writer.get_extra_info('peername'))
    while True:
        data=await reader.read(8)
        if data==b'ping':
            writer.write(b'pong')
            await writer.drain()
            print('recv: ping -> send: pong')
        elif data == b'done':
            print('recv: done')
            break
        elif len(data)==0:
            break

    writer.close()
    await writer.wait_closed()
    print('connection was closed')

async def server_asyncmain():
    server=await asyncio.start_server(hanle_asyncclient,'localhost',8000)
    print('server started')
    await server.serve_forever()

if __name__=="__main__":
    asyncio.run(server_asyncmain())