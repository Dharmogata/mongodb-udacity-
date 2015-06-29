#Overview of the Data wrangling on openstreetmap data (second try)
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
Example:
There are many levels of containment in South Korea address format.
Country
도 (Admin1) = 광역시 (Metropolitan)
시 (City)
구 (Ward)
동(dong) (precinct of the city, town)
아파트, 읍, 면, 리 (neighborhood, townships, villages, apartment)
번지, 아파트 넘버 (address number, apartment number)
우편번호 (zipcode)
When I am conducting audit on osmfile for jeju. I found that there are some sort of
differences in Address Notation. Usually, we did not use street name addess
system(western style system) atually, we used to use subdivision named Dong.
But since last 3years, korean government tried to embrace road name address
system. But also dong style is still available.
In korea, there are different Address Notations which is quite distinguished with
western style.
 동: Dong(Subdivision ) , 로: ro -> road , but we do not use abbreviation for ro or
Dong, like St, Rd, Ave.
When I run audit.py, I could get the output below. As you can see it that the data
set that I choose does not contain any street notions like St, street, Ave, Rd, and
Road. So I can not expect any output like street → St, Rd ->Road.
{'1132)': set(['IL JU SEO-RO (Hwy 1132)']),
u'2\uae38': set([u'\ub0a8\uad11\ub85c2\uae38']),
'Highway)': set(['il Ju Seo-ro (1132 Highway)']),
'Seogui-dong': set(['Seogui-dong']),
'Seogwi-Dong': set(['Seogwi-Dong']),
u'Yeonbook-ro)': set([u'\uc5f0\ubd81\ub85c (Yeonbook-ro)']),
'fasdf': set(['fasdf'])}
Seogui-dong => Seogui-dong
il Ju Seo-ro (1132 Highway) => il Ju Seo-ro (1132 Highway)
IL JU SEO-RO (Hwy 1132) => IL JU SEO-RO (Hwy 1132)
남광로2길 => 남광로2길
fasdf => fasdf
연북로 (Yeonbook-ro) => 연북로 (Yeonbook-ro)
Seogwi-Dong => Seogwi-Dong
# Other ideas about the datasets
Openstreetmap dataset is awesome,and powerfull. it is open crowd sourcing
project. however, it is updated or edited by unspecified number of peple, so, there
are always errors in data set. And cultural differences in address naming. In the
north east asia like (korea, china, japan) may different address notation which is
distinct from western style. This should be audited or cleansed in each localized
project.
Example:
There are many levels of containment in South Korea address format.
Country
도 (Admin1) = 광역시 (Metropolitan)
시 (City)
구 (Ward)
동 (precinct of the city, town)
아파트, 읍, 면, 리 (neighborhood, townships, villages, apartment)
번지, 아파트 넘버 (address number, apartment number)
우편번호 (zipcode)
Similar to Korea and China, address format in Japan has dissimilar conventions depending on the
language.
ADDRESS TYPE EXAMPLE
#2 Japanese address in
Japanese (Japanese
convention)
{〒103-8260 東京都日本橋中央区１丁目-１２-１}
This is the predominant representation in native Japanese (using Kanji,
Katakana, Hiragana and roman or Kanji numerals)
Postcodes are represented by 3digit, dash, 4 digit numerals with the prefix 〒.
Detailed address sections contains digits and dashes, with 丁目 (cyoume)
qualifiers depending on the location)
#1 Japanese address in Latin
(western convention)
{1-12-1 Nihonbashi Chuo, Tokyo, 103-8260, Japan}
This convention only applies when Latin characters (Romaji : ローマ字) is used.
2. General hierarchy representation
See below for a general hierarchy representation of Japanese addresses:
ADDRESS PARTS (ENGLISH) ADDRESS PARTS
(JAPANESE)
EXAMPLES 1 EXAMPLE 2 EXAMPLE 3
Country 国 {日本}
Postcode 郵便番号 {168-0063}, {〒168-0063}
Prefecture (state) 都道府県 {東京都} {大阪府}
Sub-Admin (county) 郡 {西多摩郡}
Municipal (PopulatedPlace) 市区町村 {港区} {日の出町}
AddressLine (Locality)(Oaza) 町・大字 {港南} {大字平井｝
{平井}
AddressLine
(SubLocality1:Cyoume)
字・丁目 {2 丁目}, {16}
AddressLine (SubLocality2:Gaiku) 街区 {16 番}{16 番地
},{16}
{A 番}, {A}
AddressLine (SubLocality3:ChibanToban)
地番・戸番 {4295 番地}
AddressLine (SubLocality4:Edaban) 枝番 {3 号}, {3}
Building Name ビル名 {グランドセントラ
ルタワー}
Floor Number 階 {1F} {1F}
Room Number/Apartment Number 部屋番号 {104 号}
Officially, Chinese address format is similar with Korea and Japan, but there are multiple address
convention in China, the address from user query will be a little different from the official one in
different part of China.
ADDRESS TYPE EXAMPLE
Chinese address in Chinese
(Official Chinese convention)
{中国上海市浦东新区松林路357号 邮政编码: 200122 }
This is a typical address in China
Postcodes are represented by 6digit
Chinese address in Latin
(western convention)
{Room. 501, Block B2, Changyuantiandi plaza, Haidian district, Beijing, 100055,
China }
See below for a general hierarchy representation of Chinese addresses:
ADDRESS PARTS (ENGLISH) ADDRESS PARTS
(CHINESE )
EXAMPLES 1 EXAMPLE 2 EXAMPLE 3
Country 国家 {中国}
Postcode 邮政编码 {100055},
Province (Admin1) 省, 直辖市 {北京市}{上海市}
{天津市}{重庆市}
{江苏省} {新疆维吾尔族
自治区}
City (PopulatedPlacce) 市 {南京市}
District/County (Admin2) 区，县 {海淀区} {房山县} {管城回族区}
Village, Town (Admin3) 乡，村, 镇 {化龙乡} {南口镇}
Neighborhood 商圈 {中关村} {解放碑商圈}
AddressLine (SubLocality1: Street) 街道 {西便门外大街} {解放路} {海运仓胡同}
AddressLine (SubLocality2:
Residential )
小区 {7号院} {恒昌花园} {东花市北里}
AddressLine (SubLocality3: Lane) 弄/巷 {10弄}, {222巷} {穗花一巷}
Building Name 建筑名 {时代广场} {希格玛大厦} {5号楼}
Block 座/门/单元 {c座} {B1座}
{甲/乙/丙/丁}
3单元 5门
Floor Number 楼层 {11楼} {10层}
Room Number/Apartment Number 门牌号 {10号} {7室} 103房
Think about many difficulties that you might face with in auditing and cleansing on data set about some
cities from China, Korea, or Japan.
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
