import sys
import os
import json

# 确保能找到 src/python 下的代码
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def main():
    print("=== Neural-Nexus System Starting ===")
    
    # 检查配置文件是否存在
    if not os.path.exists('config/config.json'):
        print("[!] 警告: 找不到 config/config.json")
        print("    请复制 config/config_template.json 并重命名为 config.json，然后填入你的密钥。")
        return

    print("[*] 系统初始化完成。等待指令...")

if __name__ == "__main__":
    main()