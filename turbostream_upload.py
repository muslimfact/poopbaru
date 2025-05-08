import httpx
import urllib.parse


turbostream_api_key = "98a5744ffbd3c2a63e0f61a37b3661f0f73b16b281da8fda8ade989dd93e76fe"
turbostream_api_endpoint  = "https://turbostream.tv/api/remote_upload.php"


try:
      headers = {
         "Authorization": f"Bearer {turbostream_api_key}",
          "Content-Type": "application/json"
      }
  
      payload = {
          "url": url  # gunakan original URL bukan encrypted
      }
  
      response_turbostream = httpx.post(turbostream_api_endpoint, headers=headers, json=payload)
      if response_turbostream.status_code == 200:
          success_count += 1
      else:
          print(f"Failed turbostream: {url} - Turbostream Response: {response_turbostream.status_code} - {response_turbostream.text}")
  except Exception as e:
    print(f"Error during Turbostream request for {url}: {e}")

