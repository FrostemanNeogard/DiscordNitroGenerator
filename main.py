import os
import json
import requests

DESIRED_ITERATIONS = 3

BASE_URL = "https://api.discord.gx.games/v1/direct-fulfillment"
PAYLOAD = {
    "partnerUserId": "2df0165dc6654f768a1f5fc8e2d8d732cf49beb01c3cbcded769a130594fc1cf",
}

OUTPUT_DIR = "./outputs"
OUTPUT_PREFIX = "output"

def generate_nitro_trial_url():
    try:
        response = requests.post(BASE_URL, json=PAYLOAD)

        response.raise_for_status()

        data = response.json()
        activation_url = f"https://discord.com/billing/partner-promotions/1180231712274387115/{data['token']}"
        return activation_url
    except Exception as e:
        print(f"An error occurred when fetching nitro activation URL: {e}")
        raise


def main():
    print("Starting generator...")
    output = []

    try:
        for i in range(DESIRED_ITERATIONS):
            url = generate_nitro_trial_url()
            output.append(url)
            print(f"\rURLs generated: {i + 1}/{DESIRED_ITERATIONS}", end="", flush=True)

        output_dir_path = os.path.abspath(OUTPUT_DIR)
        os.makedirs(output_dir_path, exist_ok=True)

        existing_files = [file for file in os.listdir(output_dir_path) if file.startswith(OUTPUT_PREFIX)]
        file_index = len(existing_files)
        output_file_name = f"{OUTPUT_PREFIX}" if file_index == 0 else f"{OUTPUT_PREFIX}_{file_index}"

        output_path = os.path.join(output_dir_path, f"{output_file_name}.txt")
        with open(output_path, "w") as file:
            file.write("\n".join(output))

        print(f"\nGeneration complete. URLs saved to: {output_path}")
    except Exception as e:
        print("\nGenerator encountered an error:", e)


if __name__ == '__main__':
  main()
