#!/usr/bin/env python3
"""
🚀 Bingo 遊戲本地伺服器啟動器
========================================

功能：
  - 自動檢測 IP 地址並顯示訪問 URL
  - 支持跨設備訪問（手機/平板/電腦）
  - 簡單易用

使用方法：
  1. Windows PowerShell: python start_server.py
  2. MacOS/Linux Terminal: python3 start_server.py
  3. 複製終端顯示的 URL 到手機瀏覽器

"""

import http.server
import socketserver
import socket
import os
import sys
import webbrowser
from pathlib import Path

PORT = 8000

def get_local_ip():
    """獲取本機 IP 地址"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def start_server():
    """啟動 HTTP 伺服器"""
    os.chdir(Path(__file__).parent)
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        local_ip = get_local_ip()
        
        print("\n" + "="*60)
        print("🎮 Bingo 遊戲伺服器已啟動！")
        print("="*60)
        print("\n📍 訪問地址：\n")
        print(f"  🖥️  本地電腦:  http://localhost:{PORT}")
        print(f"  📱 其他設備:  http://{local_ip}:{PORT}")
        print("\n" + "="*60)
        print("⌨️  按 Ctrl+C 停止伺服器")
        print("="*60 + "\n")
        
        # 自動打開瀏覽器
        try:
            webbrowser.open(f"http://localhost:{PORT}")
            print("✅ 已自動打開瀏覽器\n")
        except:
            pass
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 伺服器已停止")

if __name__ == "__main__":
    start_server()
