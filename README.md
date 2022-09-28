# WhatsApp Chatbot

## Steps to run the bot locally
* Install your desired version of Python on your local system if not installed already.
* Install PIP(Preferred Installer Program). Though in newer versions, PIP is already installed.
* Install Python Virtual Environment by using the below command:
    > pip install virtualenv
* Open command prompt (or terminal) and change the current working directory to location where you want to clone the repository and clone the current branch of this repository
* If the clone was successfully completed then a new sub directory may appear with the same name as the repository. Now change the current directory to the new sub directory.
* Create and activate a virtualenv by using the following commands:
    > virtualenv venv  
    > venv/Scripts/activate
* Install all the dependencies required to run the app:
    > pip install -r requirements.txt
* Create a `.env` file in the root directory and copy the contents of `.env.sample` file to the newly created .env file. Add the required values of API keys and tokens required to run the bot
* Run the flask web server using the following command:
    > flask run
* Run ngrok to get the temporary https public URL of our web server
    > ngrok http <port-number>
* Create a service account from Dialogflow settings and create a key and export it in JSON file. Reanme it to dialogflow_private_key.json and add it to the root directory.
* Now we need to connect the webhook with WhatsApp by adding the temporary https public URL with `/reply` in the end in the `When a message comes in` in the Twilio Sandbox for WhatsApp.
* Now you can chat with the WhatsApp bot using the number provided by the Sandbox.