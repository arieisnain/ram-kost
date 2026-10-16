"""
RAM.AI.ID — Auto-Deploy SIMKOST Pro to Live Hosting via SFTP / FTP
Membaca konfigurasi dari .vscode/sftp.json dan mengunggah aplikasi SIMKOST Pro ke server hosting ram.ai.id.
"""

import os
import json
import ftplib
import io

LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))
SFTP_CONFIG_PATH = os.path.join(LOCAL_DIR, ".vscode", "sftp.json")
INDEX_PATH = os.path.join(LOCAL_DIR, "index.html")

def get_ftp_config():
    if not os.path.exists(SFTP_CONFIG_PATH):
        raise FileNotFoundError(f"Konfigurasi SFTP tidak ditemukan di {SFTP_CONFIG_PATH}")
    with open(SFTP_CONFIG_PATH, "r", encoding="utf-8") as f:
        configs = json.load(f)
    return configs[0] if isinstance(configs, list) else configs

def deploy_simkost():
    cfg = get_ftp_config()
    host = cfg.get("host")
    port = int(cfg.get("port", 21))
    user = cfg.get("username")
    passwd = cfg.get("password")

    print(f"[SFTP-DEPLOY] Menghubungkan ke {host}:{port} sebagai {user}...")
    ftp = ftplib.FTP()
    ftp.connect(host, port, timeout=30)
    ftp.login(user, passwd)
    ftp.set_pasv(True)
    print("[SFTP-DEPLOY] FTP / SFTP Berhasil terhubung.")

    targets = ["/kost", "/simkost"]
    file_size = os.path.getsize(INDEX_PATH)

    htaccess_content = (
        "DirectoryIndex index.html\n"
        "<IfModule mod_passenger.c>\n"
        "    PassengerEnabled off\n"
        "</IfModule>\n"
    )

    for target in targets:
        try:
            ftp.mkd(target)
        except Exception:
            pass

        ftp.cwd(target)
        ftp.storbinary("STOR .htaccess", io.BytesIO(htaccess_content.encode("utf-8")))

        with open(INDEX_PATH, "rb") as f:
            ftp.storbinary("STOR index.html", f)
        print(f"[SFTP-DEPLOY] index.html ({file_size:,} bytes) berhasil diunggah ke {target}/index.html")

    ftp.quit()
    print("[SELESAI] SIMKOST Pro berhasil live di https://ram.ai.id/kost/ dan https://ram.ai.id/simkost/!\n")

if __name__ == "__main__":
    deploy_simkost()
