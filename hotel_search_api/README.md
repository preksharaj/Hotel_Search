#Hotel Search API

# Setup
	Run "setup.sh" in order to setup the environment before starting the API, 
this script installs Fabric - Fabric is a Python library and command-line tool for 
streamlining the use of SSH for application deployment or systems administration tasks.
This enables easy usage of this API

	Once this is installed fab setup command is called this activates the virtual environment, 
and installs the necessary requirements mentioned in the "requirements.txt" file.
tornado==4.3
requests==2.9.1
simplejson==3.11.1

# Starting the API
	In the project root folder execute the command `fab test`, this starts the required 
web services for the API, runs a test script on the server to successfully access all providers 
via httpand obtains the results in json format and sorts them based on ecstasy, and provides 
a sorted oputput of the obtained results.
	`fab cleanup` executes a cleanup to remove the env folder and delete any .pyc files 
that are generated during execution

# Explanation
	Logic behind the hotel search API can be understood by taking a look at the two key files 
located in hotel_search folder namely hotel_search.py and hotel_search_server.py

	hotel_search_server.py consists of a dictionary called servers, this contains the providers 
mainly 'orbitz','expedia','priceline','travelocity','hilton' which act as our endpoints and it also 
contains the port number where the server is listening namely port:8000. This script creates a 
hotelSearch object by passing the servers dictionary. hotelSearch class is imported from hotel_search.py, 
it does the task of fetching the results from the endpoints using a http fetch on the different endpoints 
and merges the results by sorting them based on ecstasy

	Finally we call the scraperapi_test.py which makes use of http get command to obtain thew results 
in json format and displays the results gracefully sorted by ecstasy
