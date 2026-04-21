import requests
import sys

def main():
    print("="*50)
    print("🌍 Multilingual Translation Terminal 🌍")
    print("="*50)
    print("Type 'quit' at any time to exit.\n")

    while True:
        # 1. Get User Input
        text = input("\nEnter text to translate: ")
        if text.lower() == 'quit':
            break

        source_lang = input("Source Language (e.g., 'en'): ")
        if source_lang.lower() == 'quit': break

        target_lang = input("Target Language (e.g., 'fr', 'de', 'es'): ")
        if target_lang.lower() == 'quit': break

        print("\nTranslating...")

        # 2. Send to your local API
        try:
            response = requests.post(
                "http://localhost:5000/translate",
                json={
                    "text": text,
                    "source_lang": source_lang,
                    "target_lang": target_lang
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                print("-" * 30)
                print(f"🎯 Result: {result['translation']}")
                print("-" * 30)
            else:
                print(f"❌ Error: {response.json().get('error', 'Unknown error')}")

        except requests.exceptions.ConnectionError:
            print("❌ Error: Could not connect to the server. Is server.py running?")

if __name__ == "__main__":
    main()