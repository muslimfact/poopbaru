

import base64
import httpx

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import urllib.parse

# Lanjutkan eksekusi kode
def encrypt_url(url, key):
    # Pastikan kunci adalah 16-byte
    key = key.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)

    # Pad URL menggunakan PKCS7
    padded_url = pad(url.encode('utf-8'), AES.block_size)

    # Enkripsi data
    encrypted = cipher.encrypt(padded_url)

    # Encode hasil enkripsi ke Base64 URL-safe
    encrypted_base64 = base64.urlsafe_b64encode(encrypted).decode('utf-8')
    return encrypted_base64

# API Keys
lulustream_api_key = '936yclje4cl5mud6kcw'  # Lulustream API Key
streamhg_api_key = "2426evezy9bm5xz0uzzy"
veev_api_key = "81wfq1eryrdlombkfrej2ldx08p092x1rw"
vinovo_api_key = "8b857a827319ed70f22e4d0668853f"
dropload_api_key = "6228dp9snugc6viw066i"
bigwarp_api_key = "1185roh927m637ogi3lv"
abstream_api_key = "23vj7x7uk12znfyaxc"
doodstream_api_key = "219725bbkborbourrp2cd4"
savefiles_api_key = "474xuktpmwclm1eu97m"
streamup_api_key = "3974a8ac0e4743c4dc6f624a1afed12d"
easyvidplay_api_key = "1a9f2e28183ebfe2f5551066"
up4stream_api_key = "43kigck2sugds800uo"

easyvidplay_api_endpoint = "https://easyvidplay.com/api/v1/video/advance-upload"
up4stream_api_key = "43kigck2sugds800uo"


voesx_api_key = "Wr7fjmWTBp6EY0XGYJZwleaMJiJ2cuf21c3UvSpDd7GtPLAVnQTGiY9RNtwCyCbK"

key = "mysecretkey12345"  # Kunci AES untuk enkripsi
lulustream_api_endpoint = "https://api.lulustream.com/api/upload/url"
streamhg_api_endpoint = "https://streamhgapi.com/api/upload/url"
veev_api_endpoint  = "https://veev.to/api/upload/url"
vinovo_api_endpoint  = "https://api.vinovo.si/api/upload/url"
dropload_endpoint = "https://dropload.io/api/upload/url"
bigwarp_api_endpoint  = "https://bigwarp.io/api/upload/url"
abstream_api_endpoint  = "https://abstream.to/api/upload/url"
doodstream_api_endpoint  = "https://doodapi.co/api/upload/url"
savefiles_api_endpoint  = "https://savefiles.com/api/upload/url"
streamup_api_endpoint  = "https://api.streamup.cc/v1/remote"
up4stream_api_key = "43kigck2sugds800uo"

easyvidplay_api_endpoint = "https://easyvidplay.com/api/v1/video/advance-upload"
up4stream_api_endpoint = "https://up4stream.com/api/upload/url"


voesx_api_endpoint = "https://voe.sx/api/upload/url"

# Variabel untuk menghitung jumlah sukses
success_count = 0



# Read URLs from output.txt
try:
    with open('output_link.txt', 'r') as file:
        urls = file.readlines()
        urls = [url.strip() for url in urls if url.strip()]  # Remove empty lines and whitespace

    total_urls = len(urls)  # Total link yang akan diproses

    # Encrypt each URL and send GET requests to both APIs
    for index, url in enumerate(urls, start=1):
        # Enkripsi URL
        encrypted = encrypt_url(url, key)
        new_url = f"https://darenx-upbkafe.hf.space/ex/{encrypted}"

        print(f"**=> Processing {index} of {total_urls}...")  # Menampilkan progress

        try:
            # doodstream request
            response_doodstream= httpx.get(doodstream_api_endpoint, params={"key": doodstream_api_key, "url": new_url})
            if response_doodstream.status_code == 200:
                success_count += 1
            else:
                print(f"Failed doodstream: {url} - doodstream Response: {response_doodstream.status_code} - {response_doodstream.text}")
        except Exception as e:
            print(f"Error during Lulustream request for {new_url}: {e}")

        try:
            # Lulustream request
            response_lulustream = httpx.get(lulustream_api_endpoint, params={"key": lulustream_api_key, "url": new_url})
            if response_lulustream.status_code == 200:
                success_count += 1
            else:
                print(f"Failed lulustream: {url} - Lulustream Response: {response_lulustream.status_code} - {response_lulustream.text}")
        except Exception as e:
            print(f"Error during Lulustream request for {new_url}: {e}")

        
        try:
            # streamhg request
            response_streamhg = httpx.get(streamhg_api_endpoint, params={"key": streamhg_api_key, "url": new_url})
            if response_streamhg.status_code == 200:
                success_count += 1
            else:
                print(f"Failed streamhg: {url} - StreamHG Response: {response_streamhg.status_code} - {response_streamhg.text}")
        except Exception as e :
            print(f"Error during StreamHG request for {new_url}: {e}")

        
        

        try:
            # vinovo request
            response_vinovo = httpx.get(vinovo_api_endpoint, params={"key": vinovo_api_key, "url": url})
            if response_vinovo.status_code == 200:
                success_count += 1
            else:
                print(f"Failed vinovo : {url} - Vinovo Response: {response_vinovo.status_code} - {response_vinovo.text}")
        except Exception as e:
            print(f"Error during Vinovo request for {url}: {e}")

        

        try:
            url_to_upload = f"{bigwarp_api_endpoint}?key={bigwarp_api_key}&url={new_url}"

            # bigwarp request
            response_bigwarp = httpx.get(url_to_upload)
            if response_bigwarp.status_code == 200:
                success_count += 1
            else:
                print(f"Failed bigwarp: {url} - bigwarp Response: {response_bigwarp.status_code} - {response_bigwarp.text}")
        except Exception as e:
            print(f"Error during bigwarp request for {url}: {e}")

        try:
            url_to_upload = f"{abstream_api_endpoint}?key={abstream_api_key}&url={new_url}"

            # abstream request
            response_abstream = httpx.get(url_to_upload)
            if response_abstream.status_code == 200:
                success_count += 1
            else:
                print(f"Failed abstream: {url} - response_abstream Response: {response_abstream.status_code} - {response_abstream.text}")
        except Exception as e:
            print(f"Error during response_abstream request for {url}: {e}")

        try:
            url_to_upload = f"{savefiles_api_endpoint}?key={savefiles_api_key}&url={new_url}"

            # savefiles request
            response_savefiles = httpx.get(url_to_upload)
            if response_savefiles.status_code == 200:
                success_count += 1
            else:
                print(f"Failed savefiles: {url} - response_savefiles Response: {response_savefiles.status_code} - {response_savefiles.text}")
        except Exception as e:
            print(f"Error during response_savefiles request for {url}: {e}")

        try:
            url_to_upload = f"{up4stream_api_endpoint}?key={up4stream_api_key}&url={new_url}&file_adult=1"

            # savefiles request
            response_up4stream = httpx.get(url_to_upload)
            if response_up4stream.status_code == 200:
                success_count += 1
            else:
                print(f"Failed response_up4stream: {url} - response_up4stream Response: {response_savefiles.status_code} - {response_up4stream.text}")
        except Exception as e:
            print(f"Error during response_up4stream request for {url}: {e}")

        
        try:
            encoded_url = urllib.parse.quote(url, safe='')
            url_to_upload = f"{streamup_api_endpoint}?api_key={streamup_api_key}&url={encoded_url}&action=add_remote_url"

            # streamup request
            response_streamup = httpx.get(url_to_upload)
            if response_streamup.status_code == 200:
                success_count += 1
            else:
                print(f"Failed: {url} - streamup_api_endpoint Response: {response_streamup.status_code} - {response_streamup.text}")
        except Exception as e:
            print(f"Error during streamup_api_endpoint request for {url}: {e}")

        try:
            # encode URL untuk jaga-jaga (opsional, tergantung API)
            encoded_url = urllib.parse.quote(url, safe=':/?&=%')  # biar format URL tetap valid
            payload = {
                "url": encoded_url
               
            }
    
            headers = {
                "accept": "application/json",
                "api-token": easyvidplay_api_key,
                "Content-Type": "application/json"
            }
    
            response_easyvidplay = httpx.post(easyvidplay_api_endpoint, json=payload, headers=headers)
            if response_easyvidplay.status_code == 200:
                success_count += 1
            else:
                print(f"Status: {response_easyvidplay.status_code} - {response_easyvidplay.text} - {url} ")
    
        except Exception as e:
            print(f"Error during easyvidplay request for {url}: {e}")
        

        print(f"==>  {index} of {total_urls} SUCCESS UPLOAD KE DropLOAD & Lulustream  <=====")

    # Tampilkan total jumlah sukses
    print("\n=========================================")
    print(f"Total Successful Uploads: {success_count}")
    print("=========================================")

except FileNotFoundError:
    print("The file 'output_link.txt' was not found. Please ensure it exists in the same directory.")
