@echo off
if not exist "C:\Users\%USERNAME%\.ssh" mkdir C:\Users\%USERNAME%\.ssh
echo KEY >> C:\Users\%USERNAME%\.ssh\authorized_keys
ngrok tcp 22
curl http://127.0.0.1:4040/api/tunnels > tunnel.json