import os
import requests

def test_api_endpoint(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"Success: {url} returned status code 200\n"
        else:
            return f"Failure: {url} returned status code {response.status_code}\n"
    except requests.exceptions.RequestException as e:
        return f"Error: Could not connect to {url}\nException: {e}\n"

def test_endpoints_from_file(file_path):
    results = ""
    with open(file_path, 'r') as file:
        urls = file.readlines()
        for url in urls:
            url = url.strip()  # Remove any surrounding whitespace or newlines
            if url:
                results += test_api_endpoint(url)
    return results

if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), "endpoint_list.txt")
    test_results = test_endpoints_from_file(file_path)

    # Save the output to a text file
    output_file = os.path.join(os.getcwd(), "test_results.txt")
    with open(output_file, 'w') as file:
        file.write(test_results)

    print(f"Test results saved to {output_file}")
