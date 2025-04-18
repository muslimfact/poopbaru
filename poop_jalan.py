import subprocess


# Menjalankan poop_baru.py
print("Menjalankan poop_baru.py...")
proses3 = subprocess.run(["python3", "poop2_baru.py"], check=True)

# Menjalankan remote_upload.py setelah poop_baru.py selesai
print("Menjalankan remote_upload.py...")
proses4 = subprocess.run(["python3", "remote_upload.py"], check=True)

# Print jika kedua script sudah dijalankan
print("Semua script telah dijalankan!")
