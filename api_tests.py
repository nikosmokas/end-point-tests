import os
import requests
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def test_api_endpoint(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"Success: {url} returned status code 200<br>"
        else:
            return f"Failure: {url} returned status code {response.status_code}<br>"
    except requests.exceptions.RequestException as e:
        return f"Error: Could not connect to {url}<br>Exception: {e}<br>"

def test_endpoints_from_file(file_path):
    results = ""
    with open(file_path, 'r') as file:
        urls = file.readlines()
        for url in urls:
            url = url.strip() 
            if url:
                results += test_api_endpoint(url)
    return results

def send_email(subject, content):
    
    message = Mail(
        from_email='nikossmokas@gmail.com',
        to_emails='nikosmokas@hotmail.gr',
        subject='nmokas-dev.tech - API Tests report',
        html_content=content)
    try:
        sg=SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), "endpoint_list.txt")
    test_results = test_endpoints_from_file(file_path)

    # Save the output to a text file
    output_file = os.path.join(os.getcwd(), "test_results.txt")
    with open(output_file, 'w') as file:
        file.write(test_results)

    print(f"Test results saved to {output_file}")

    # Send the test results via email
    send_email("Daily API Test Results", test_results)
