import os
import google.cloud.dialogflow_v2 as dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='private_key.json'
DIALOGFLOW_PROJECT_ID ='firstagent-huvu'
DIALOGFLOW_LANGUAGE_CODE ='ko'
our_query ="안녕"
SESSION_ID ='me'    
session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID,SESSION_ID)
our_input = dialogflow.types.TextInput(text=our_query,language_code=DIALOGFLOW_LANGUAGE_CODE)
query = dialogflow.types.QueryInput(text=our_input)
response = session_client.detect_intent(session=session,query_input=query)

print("Our text:", response.query_result.query_text)
print("Dialogflow's response:",response.query_result.fulfillment_text)
print("Dialogflow's intent:",response.query_result.intent.display_name)