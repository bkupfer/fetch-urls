# Autify Home Test: Fetch-URLs  

#### @author: Bernardo Küpfer 
#### @email:  bdokupferb@gmail.com

### Hello Autify team!


Thanks for this opportunity to take this Backend Engineer Take Home Test. 

This script implements all three Sections requirements, as per described on the assignment.  

As requested: "Please do not to link the text of assignment to your public repo.".

For further information on the requested requirements, please refer to the relevant assignment text.
 

## How to run the script:

There are two main ways of running this script, you can choose either.

### Run Locally with Python CLI
To run this script locally, you need to set up a Python 3 environment and install the dependencies in the 
requirements.txt file. 

`pip install -r requirements.txt`

Now you can run the file locally using the python CLI. 

`python fetch.py https://www.google.com/`

### Run Docker
To build the Docker image, run the following command in the same directory as the Dockerfile:

`docker build -t fetch .`

To run the Docker image, use the docker run command, passing the URL(s) as arguments:

`docker run fetch https://www.google.com/ https://www.jisho.org/`

You can also pass the --metadata flag to print the metadata:

`docker run fetch --metadata https://www.google.com/ https://www.jisho.org/`


## Inspecting the files

Depending on how you decided to run the script, where the downloaded files will be located.

### Locally

If you ran the code using python cli locally, then the downloaded .html file will be created 
in the same root folder as the fetch.py file, and a new "assets" folder will be created to store 
all the images and downloaded assets.   

### Docker

If you download the files through the Docker container, then the downloaded files will be 
stored inside this docker container. So in case you want to inspect them and view them locally, 
you could copy the contents of the docker container to your local machine. 
You can do this using the following line. 

`docker cp <container_id>:app ./docker-app`

Now you can inspect locally the contents of the .html files and assets for the requested urls with help 
of your favorite browser. 
