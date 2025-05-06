import requests
import time

def spam_webhook():
    webhook_url = input("Enter webhook URL: ")
    message = input("Enter message to spam: ")
    count = int(input("Enter message count: "))
    delay = float(input("Enter delay between messages (seconds): "))

    for i in range(count):
        try:
            data = {"content": message}
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                print(f"[{i + 1}/{count}] Sent!")
            else:
                print(f"[{i + 1}/{count}] Error: {response.status_code}")
            time.sleep(delay)
        except Exception as e:
            print(f"[{i + 1}/{count}] Error: {e}")

    delete = input("Delete webhook? (y/n): ").lower()
    if delete == 'y':
        try:
            requests.delete(webhook_url)
            print("Webhook deleted!")
        except Exception as e:
            print(f"Delete failed: {e}")

if __name__ == "__main__":
    spam_webhook()