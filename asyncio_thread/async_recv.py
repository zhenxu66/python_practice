import asyncio
import time

start_time = time.perf_counter()


def handle_command(command):
    command = command.decode()
    splitcommand = command.split(':')
    current_time = time.perf_counter()
    print(current_time - start_time)
    if splitcommand[1] == 'a':
        send_string = 'Test a'
        print("message a is received")
        return send_string.encode('ascii')
    elif splitcommand[1] == 'b':
        send_string = 'Test b'
        print("message b is received")
        return send_string.encode('ascii')


async def handle_request(reader, writer):
    while True:
        command = await reader.readline()
        command = command.strip()
        if not command:
            break
        response = handle_command(command)

        writer.write(response)
        await writer.drain()
    writer.close()


async def main():
    server = await asyncio.start_server(handle_request, '127.0.0.1', 25800)
    while True:
        async with server:
            print("Server started on 127.0.0.1:25800")
            await server.serve_forever()
            
# must use if __name__
if __name__ == "__main__":
    asyncio.run(main())

