
 📦 Multi-Threaded Chat Application
A real-time chat application built using Python WebSocket server and a React frontend with support for:
✅ Public and private messaging
📁 File sharing
😀 Emoji picker
🔄 Real-time user list
🎨 WhatsApp-style modern UI


🚀 Features
🔗 Real-time chat via WebSockets
👥 Multi-client support (each client has a unique username)
🗨️ Public chat messages (broadcasted to all)
🔒 Private messages to selected users
📎 File sharing (both public and private)
😀 Emoji picker integration
🧭 Live user list (updates as users join/leave)
🎨 Beautiful UI using React + Tailwind CSS

📁 Project Structure
multi_threading_chat_app/
├── server.py                  # Python WebSocket server
├── client_launcher.py         # GUI script to launch clients
├── gui_client.py              # Tkinter client window (if using Python GUI)
├── /frontend                  # React frontend
│   ├── public/
│   └── src/
│       ├── components/
│       ├── ChatRoom.js
│       └── ...


🖥️ How to Run Locally

✅ Backend (WebSocket Server)
# Navigate to backend folder
cd multi_threading_chat_app
# Install dependencies
pip install websockets
# Start the WebSocket server
python server.py


✅ Frontend (React Client)
# Navigate to frontend folder
cd frontend
# Install dependencies
npm install
# Start the development server
npm start

