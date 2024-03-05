# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:52:08 2024

@author: s2820
"""

import random
from flask import Flask, request, redirect

app = Flask(__name__)

# 9個網站的URL
websites = [
    "https://www.surveycake.com/admin/tw/templates?type=studies",
    "https://stdb.org/t/topic/31218",
    "https://www.surveycake.com/zh-tw/help-center/survey/api-verification",
    "https://chat.openai.com/c/35cf2748-7a5d-499e-aa0a-1936b3c93011",
]

@app.route('/')
def index():
    # 從查詢參數中讀取分配的網站，如果不存在則隨機選擇一個
    assigned_website = request.args.get('website', random.choice(websites))
    
    # 直接使用網站的完整 URL 進行重定向
    return redirect(assigned_website)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0')
    


import os

# 獲取當前檔案的絕對路徑
current_file_path = os.path.abspath(__file__)

# 獲取專案目錄的絕對路徑
project_dir = os.path.dirname(current_file_path)

print("專案目錄:", project_dir)