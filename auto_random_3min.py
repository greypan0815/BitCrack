import os
import subprocess
import time
import secrets
import signal

# ================= 設定區 =================
FOUND_FILE = "FOUND_KEYS.txt"
RUN_TIME = 180  # 每次空投的執行時間 (秒)，180秒 = 3分鐘
# ==========================================

def generate_random_start_key():
    """產生一個加密級別的隨機 256-bit 整數"""
    return secrets.randbits(256)

def main():
    print("=======================================")
    print("  BitCrack 時間刺客空投流 (Mac M晶片專屬)")
    print("=======================================")
    print(f"[提示] Apple M5 算力發動中 (~65 MKey/s)。")
    print(f"[提示] 每 {RUN_TIME} 秒強制重置宇宙座標一次。\n")

    try:
        while True:
            # 檢查是否已經中大獎了！
            if os.path.exists(FOUND_FILE) and os.path.getsize(FOUND_FILE) > 0:
                print(f"\n[!!! 奇蹟發生 !!!] 系統偵測到 {FOUND_FILE} 內有資料！")
                print("程式已自動停止，快去看看你是不是解開了中本聰的錢包！")
                break

            current_key = generate_random_start_key()
            start_hex = f"{current_key:064X}"
            
            print(f"--------------------------------------------------")
            print(f"[系統] 正在空投到全新宇宙座標...")
            print(f"-> 起點: {start_hex[:16]}...{start_hex[-16:]}")
            
            # Mac 專屬指令：拔掉 END，只給 START，讓它以為要跑一輩子
            command = [
                "./bin/clBitCrack",
                "-u",
                "-i", "satoshi.txt",
                "-o", FOUND_FILE,
                "--keyspace", start_hex
            ]
            
            print(f"[系統] 發動 M 晶片！計時 {RUN_TIME} 秒開始...\n")
            
            # 啟動 BitCrack
            process = subprocess.Popen(command)
            
            try:
                # Python 經理拿著碼表等待
                process.wait(timeout=RUN_TIME)
                
            except subprocess.TimeoutExpired:
                # 3 分鐘時間到！強制介入
                print(f"\n[系統] {RUN_TIME} 秒時間到！發送中斷訊號準備進行下一次空間跳躍...")
                # 發送 SIGINT 訊號 (等同於在鍵盤按下 Ctrl+C)
                process.send_signal(signal.SIGINT)
                process.wait() # 確保程式已安全將 VRAM 釋放
                
            # 給晶片稍微喘息降溫的時間 (2秒)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\n\n[系統] 收到玩家手動中斷 (Ctrl+C)！正在安全退出...")
        print("[提示] M5 晶片辛苦了，風扇可以休息了！")

if __name__ == "__main__":
    main()