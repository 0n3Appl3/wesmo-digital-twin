from dotenv.main import load_dotenv
import os
import mysql.connector
import requests

def main():
    # Testing mysql library (not relevant to requests library)
    mydb = mysql.connector.connect(
        host=os.environ.get('VITE_DB_HOST'),
        user=os.environ.get('VITE_DB_USER'),
        password=os.environ.get('VITE_DB_PASSWORD'),
    )
    print(mydb)

    # Testing requests library
    new_data = {
        "id": 13,
        "name": "Test",
    }
    url_post = os.environ.get('VITE_BACKEND_URL') + "/api/v1/rest-test-3"
    headers = {
        "content-type": "application/json",
    }
    post_response = requests.post(url_post, json=new_data, headers=headers)
    post_response_json = post_response.json()
    print(post_response_json)

if __name__ == "__main__":
    load_dotenv()
    main()