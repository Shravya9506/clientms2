# clientms2aThis application is a client management system for a car dealership. This application is built for the Acme auto company to ensure that employees of the company can easily share information about current customers to ensure they are satisfied with the car sales and services. The employees of the company can perform CRUD operations on the records of their clients, comment about the actions or requests made by the client, and the cars owned by the client
To use this application:
Create a new Pycharm Django Project using this folder for the source.
Answer 'Yes' when prompted to use the files from this folder for the new project.
Settings: Set up the project interpreter to reference your Python 3.7 installation.
Settings: Add a new Virtual Environment

Edit settings.py to add your gmail account and password for Django apps. Make sure to change the security settings in gmail account to allow Django send emails. This can be done by navigating to setting by clicking 'Manage your google account' and then select 'Security' and Turn on the 'Less secure app access'. 

Open the Terminal Window:

Install the required packages:
   pip install -r requirements.txt
This command will install the required packages to run the application.

Make the migrations for the database model:
   py manage.py migrate

Create a superuser:
   py manage.py createsuperuser
Enter the username and password for the superuser.

Run the server :
  py manage.py runserver

Click on the link that is displayed in the terminal window to launch the application.
