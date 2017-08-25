# The Touring Machines

This is the official repository of the Touring Machines: Daniel Cummins, Andrea Pignanelli, Shanming Li.
In this document it will be explained how to run the project and recreate it on any other compatible machine or server.

This project is the result of the summer of 2017 Research Practicum of UCD's MSc. in Computer science (conversion). The following is the original
project specification:

"Bus companies produce schedules which contain generic travel times. For example, in the
Dublin Bus Schedule, the estimated travel time from Dun Laoghaire to the Phoenix Park is 61
minutes (http://dublinbus.ie/Your-Journey1/Timetables/All-Timetables/46a-1/). Of course,
there are many variables which determine how long the actual journey will take. Traffic
conditions which are affected by the time of day, day of the week, month of the year and the
weather play an important role in determining how long the journey will take.
These factors along with the dynamic nature of the events on the road network make it
difficult to efficiently plan trips on public transport modes which interact with other traffic.
This project involves analysing historic Dublin Bus GPS data [1] and weather data [2] in
order to create dynamic travel time estimates.
Based on data analysis of historic Dublin bus GPS data, a system which when presented with
any bus route, departure time, day of the week, current weather condition, produces an
accurate estimate of travel time for thecomplete route.
Users should be able to interact with the system via a web-based interface which is optimised
for mobile devices.
When presented with any bus route, an origin stop and a destination stop, a time, a day of the
week, current weather, the system should produce and display via the interface an accurate
estimate of travel time for the selected journey"



#Instructions to run it

##Pre-requisites
python 3.5, pip installer, tmux or screen, and 20 GB of free space (or less if files are deleted after each passage)

##Links to the files
BUS info (download both): https://data.dublinked.ie/dataset/dublin-bus-gps-sample-data-from-dublin-city-council-insight-project
Weather info (daily weather from 06/11/12 to 30/11/12 and from 01/01/13 to 31/01/13): http://www.met.ie/climate-request/

TOTAL SIZE: 8 GB uncompressed


#Script to run on server or local machine (in this order)

TouringMachines/Bash Scripts/installPackages.sh      It installs all the necessary packages


##Data preparation

The only modifications that have to be done to the scripts is in the paths, as all the paths contained in the code
are our own. There are comments highlighting what needs to be changed.

TouringMachines/Python Scripts/SeparateLines.py   (after this operation the original files can be deleted)
TouringMachines/Python Scripts/alldatajson.py
TouringMachines/Python Scripts/newcsvs.py     (files of the previous operation can be deleted)
TouringMachines/Python Scripts/Weather.py     (files of the previous operation can be deleted)
TouringMachines/Python Scripts/PatternToIndex.py
TouringMachines/Python Scripts/RandomForest.py  (in case of errors, delete files that are too small <100Kb. The pickle
                                                 files are saved in the correct django folder)

##Files to run on tmux or screen
TouringMachines/Python Scripts/Weather_json.py (scraper for weather predictions)
TouringMachines/Python Scripts/AAtweets.py  (scraper for twitter feed)


#Deployment

To the deploy the application, changes have to be made to TouringMachines/DublinBus/DublinBus/settings.py to accomodate the changes.
The easiest way is to run the built-in deployer by adding the proper domain or IP address to the approved hosts. In case nginx+gunicorn,
or apache more changes have to be made.

When in  TheTouringMachines/DublinBus folder, the command "python manage.py domainname:portofchoice" will work.














