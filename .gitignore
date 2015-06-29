#Overview of the Data wrangling on openstreetmap data
Name : SUH, KWANGSIK
OpenStreetMap is a good example of crowdsourcing project like Wikipedia. It is all
free and open to everyone so than anyone who are interested in can edit it and use
it. So, Openstreetmap is so powerful tool because it dose use the collective
intelligence.
In the meantime, in this final project, I was intending to select the data set of
Busan city where I was grown up. But unfortunately, the requirement volume for
this project was 50MB , the volume of data set for Busan was about 54MB, So, I
was searching for another options and finally I decided to download osm file for
Jeju-south korea from openstreetmap data and use it for this final project.
As the project Rubric request that students provide a statistical overview such as
size of the file, number of unique users, number of nodes and ways, and number of
chosen type of nodes, like cafes, shops etc. I have answering those.
a. file size : 42.5MB
As the output of “mapparser.py” is following
{'bounds': 1,
'member': 211,
'nd': 242763,
'node': 224336,
'osm': 1,
'relation': 46,
'tag': 56076,
'way': 12837}
b. The number of nodes and ways in Jeju : nodes => 224336, ways => 12837
As the output of “users.py” is following
set(['103253',
'103574',
'117699',
'1204597',
'….......
'888456',
'92274',
'939656'])
('Unique user count:', 89)
c. number of unique users: 89
After having run the code “audit.py”and “data.py”, I can parse and cleanse it. And
then Next step is loading it into MongoDB by running file name “loading_jeju.py”.
Now , it is time to get some staticstic with using MonogoDB queries
d. number of chosen type of nodes, like cafes, shops etc in Jeju , korea:
MongoDB queries →
pipeline = [ { "$project" : { "amenity" : "$amenity" }},
{ "$group" : { "_id" : "$amenity",
"count" : { "$sum" : 1 }}},
{ "$sort" : { "count" : 1}}]
Output:
[{u'_id': u'drinking_water', u'count': 8}, {u'_id': u'nightclub', u'count': 8}, {u'_id':
u'pub', u'count': 8},
{u'_id': u'shower', u'count': 8},
{u'_id': u'fast_food', u'count': 8},
{u'_id': u'fire_station', u'count': 8},
{u'_id': u'car_rental', u'count': 8},
{u'_id': u'bicycle_rental', u'count': 16},
{u'_id': u'bus_station', u'count': 16},
{u'_id': u'cinema', u'count': 16},
{u'_id': u'university', u'count': 32},
{u'_id': u'atm', u'count': 32},
{u'_id': u'shelter', u'count': 40},
{u'_id': u'arts_centre', u'count': 56},
{u'_id': u'cafe', u'count': 64},
{u'_id': u'ferry_terminal', u'count': 64},
{u'_id': u'townhall', u'count': 80},
{u'_id': u'sauna', u'count': 96},
{u'_id': u'post_office', u'count': 144},
{u'_id': u'toilets', u'count': 160},
{u'_id': u'place_of_worship', u'count': 184},
{u'_id': u'police', u'count': 224},
{u'_id': u'veterinary', u'count': 232},
{u'_id': u'kindergarten', u'count': 352},
{u'_id': u'library', u'count': 576},
{u'_id': u'parking', u'count': 928},
{u'_id': u'school', u'count': 1008},
{u'_id': u'fuel', u'count': 1040},
{u'_id': u'bank', u'count': 1064},
{u'_id': u'dentist', u'count': 1128},
{u'_id': u'restaurant', u'count': 1520},
{u'_id': u'hospital', u'count': 4264},
{u'_id': None, u'count': 1883992}]
# Problems encountered in your map
I want to mention about different Address Naming system in korea.
When I am conducting audit on osmfile for jeju. I found that there are some sort of
differences in Address Notation. Usually, we did not use road name addess system
atually, we used to use subdivision named Dong. But since last 3years, korean
government tried to embrace road name address system. But dong style is still
available.
In korea, there are different Address Notations which is quite distinguished with
western style.
Dong(Subdivision ) , ro -> road but we do not use abbreviation for ro or Dong,
like St, Rd, Ave.
# Other ideas about the datasets
Openstreetmap dataset is awesome,and powerfull. it is open crowd sourcing
project. however, it is updated or edited by unspecified number of peple, so, there
are always errors in data set. And cultural differences in address naming. In the
north east asia like (korea, china, japan) may different address notation which is
distinct from western style. This should be audited or cleansed in each localized
project.
What is your name?
SUH, KWANG SIK
What E-mail address do you use to sign in to Udacity?
spectacle2002@gmail.com
What area of the world you used for your project? Post a link to the map position
and write a short description. Note that the osm file of the map should be at least
50MB.
https://www.openstreetmap.org/search?query=%EC%A0%9C%EC%A3%BC%EB%8F
%84#map=11/33.4091/126.5694
I chose this particular place because its volume was 42.50MB, I intended to select
the Busan city where is my hometown, but it was 53MB.
Is there a list of Web sites, books, forums, blog posts, github repositories etc that you
referred to or used in this submission (Add N/A if you did not use such resources)?
MongoDB university: M101p;MongoDB for Python Developers->
https://university.mongodb.com/courses/M101P/about
M102: MongoDB for DBA ->
https://university.mongodb.com/courses/M102/about
MONGODB,Python TUTORIAL:
http://www.tutorialspoint.com/mongodb/index.htm
http://www.tutorialspoint.com/python/python_variable_types.htm
“I hereby confirm that this submission is my work. I have cited above the origins
of any parts of the submission that were taken from Websites, books, forums, blog posts,
github repositories, etc. By including this in my email, I understand that I will be expected
to explain my work in a video call with a Udacity coach before I can receive my verified
certificate.”
