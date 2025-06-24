import asyncio
import websockets

clients = {}  # Maps websocket -> username

async def notify_user_list():
    usernames = list(clients.values())
    message = f"USERS::{','.join(usernames)}"
    for client in clients:
        await client.send(message)

async def handler(websocket):
    try:
        async for message in websocket:
            print(f"[MESSAGE RECEIVED] {message}")

            if message.startswith("SETNAME::"):
                username = message.split("::", 1)[1]
                clients[websocket] = username
                print(f"[CONNECTED] {username}")
                await notify_user_list()

            elif message.startswith("PRIVATE::"):
                _, recipient, content = message.split("::", 2)
                sender = clients.get(websocket, "Unknown")
                for client, uname in clients.items():
                    if uname == recipient:
                        await client.send(f"[PRIVATE] {sender} → You: {content}")
                        break

            elif message.startswith("PRIVATE_FILE::"):
                parts = message.split("::", 4)
                if len(parts) == 5:
                    _, recipient, filename, filedata, filetype = parts
                    sender = clients.get(websocket, "Unknown")
                    for client, uname in clients.items():
                        if uname == recipient:
                            await client.send(
                                f"PRIVATE_FILE::{sender}::{filename}::{filedata}::{filetype}"
                            )
                            break

            elif message.startswith("FILE::"):
                parts = message.split("::", 3)
                if len(parts) == 4:
                    _, filename, filedata, filetype = parts
                    for client in clients:
                        if client != websocket:
                            await client.send(
                                f"FILE::{filename}::{filedata}::{filetype}"
                            )

            else:
                sender = clients.get(websocket, "Unknown")
                for client in clients:
                    if client != websocket:
                        await client.send(f"{sender}: {message}")

    except websockets.ConnectionClosed:
        username = clients.get(websocket, "Unknown")
        print(f"[DISCONNECTED] {username}")
    finally:
        if websocket in clients:
            del clients[websocket]
        await notify_user_list()

async def main():
    print("[STARTED] WebSocket server on ws://localhost:8080")
    async with websockets.serve(handler, "localhost", 8080):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
