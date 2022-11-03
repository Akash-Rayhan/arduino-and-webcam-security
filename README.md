# arduino-and-webcam-security

When the motion sensor is triggered through arduino the output will be sent to your application

Then the application will instruct the webcam to capture a picture.

Here comes the tricky part!!!

The captured picture will be uploaded to your google drive account.

We don't need to worry Pydrive has already made the solution.

How can we use Pydrive to solve this problem?

We will need some basic authentications. No sweat

Drive API requires OAuth2.0 for authentication. PyDrive makes your life much easier by handling complex authentication steps for you.

1.Go to https://console.cloud.google.com/cloud-resource-manager and make your own project.

2.Search for ‘Google Drive API’, select the entry, and click ‘Enable’.

3.Select ‘Credentials’ from the left menu, click ‘Create Credentials’, select ‘OAuth client ID’.

4.Now, the product name and consent screen need to be set -> click ‘Configure consent screen’ and follow the instructions. Once finished:

  a.Select ‘Application type’ to be Web application.
  
  b.Enter an appropriate name.
  
  c.Input http://localhost:8080 for ‘Authorized JavaScript origins’.
  
  d.Input http://localhost:8080/ for ‘Authorized redirect URIs’.
  
  e.Click ‘Save’.
  
5. Click ‘Download JSON’ on the right side of Client ID to download client_secret_<really long ID>.json.

The downloaded file has all authentication information of your application. Rename the file to “client_secrets.json” and place it in your working directory.

you will see a web browser asking you for authentication. Click Accept and you are done with authentication.

## Automatic and custom authentication with settings.yaml

Read this section if you need a custom authentication flow, such as silent authentication on a remote machine. For an example of such a setup have a look at Sample settings.yaml.

At first complete the 5 steps above download the json file

On this file "Sample settings.yaml" edit the "client_id" and "client_secret" from your downloaded json file

Now you won't be asked  for authentication again and again. You don't have to click Accept everytime

Fully Automated!!!
