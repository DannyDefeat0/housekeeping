import os
import shutil
import fileinput

# Specify the replacement

clients = ['Videon Dodge',	'Bosak Motors',	'Normandin Dodge',	'Bill Luke Dodge',	'Bill Snethkamp Dodge',	'Sea View Auto',	'Salerno Duane Dodge',	'Westbury Dodge',	'Brown\'s Dodge',	'Huntington Dodge',	'Kelly Dodge',	'Farrish Dodge',	'Fields Dodge',	'Liberty Dodge',	'Ancira Dodge',	'Ron Carter Dodge',	'Don Davis Dodge',	'Firkins Dodge',	'Tuttle-Click Dodge',	'Huntington Beach Dodge',	'Dodge of Ontario',	'Shaver Dodge',	'Keffer Dodge',	'Bob Howard Dodge',	'Snethkamp Dodge',	'Fred Martin Superstore',	'Champion Cueter',	'Cronic Dodge',	'Ferman Dodge',	'Douglas Dodge',	'Croton Auto Park',	'Finnegan Dodge',	'Planet Dodge of Flagstaff',	'Sansone Dodge',	'Haasz Automall',	'Zeigler Dodge',	'Marino Dodge',	'Dulles Dodge',	'Franklin Dodge',	'Route 18 Dodge',	'Nielsen Dodge',	'Precision Dodge',	'Clay Cooley Dodge',	'Lindsay Dodge',	'Newnan Peachtree Dodge',	'Winnie Dodge',	'Countryside Dodge',	'Victory Dodge',	'Route 1 Dodge',	'Premier Dodge',	'Folsom Lake Dodge',	'Frisco Dodge',	'Lake Elsinore Dodge',	'Murray Dodge of Starke',	'Landers Dodge',	'Bonham Dodge',	'Greenville Dodge',	'San Leandro Dodge',	'South Point Dodge',	'Jason Lewis Dodge',	'Dupage Dodge',	'Turnersville Dodge',	'Landmark Dodge Atlanta',	'AutoNation Dodge Valencia',	'Shottenkirk Dodge',	'Island Dodge',	'M & L Dodge',	'J Star Dodge',	'Mac Haik Dodge',	'Lodi Dodge',	'Landers Dodge of Norman',	'Bravo Dodge of Alhambra',	'Gurnee Dodge',	'Criswell Dodge',	'Bayway Dodge',	'Classic Dodge',	'Reed Dodge',	'Red River Dodge',	'Kunes Dodge of Woodstock',	'Los Angeles Dodge',	'Capital Dodge',	'Campbell Dodge',	'Nyle Maxwell Dodge',	'Max Belton Dodge',	'Cavender Dodge',	'Joe Cooper Dodge',	'Route 130 Dodge',	'Monrovia Dodge',	'Coastline Dodge',	'Future Dodge of Concord',	'Matt Bowers Dodge',	'Jerry Seiner Dodge',	'Wischnewsky Dodge',	'Jacksonsville Dodge',	'Envision Dodge',	'Prestige Dodge',	'Payne Dodge',	'Dodge of Seminole County',	'Calavan Dodge',	'Joe Cooper Dodge of Yukon',	'Forest Lane Dodge',	'Tutton Dodge of Jasper',	'Prosper Dodge',	'Castle Dodge',	'Orange Coast Dodge',	'Szott I-96 Dodge',	'Crystal Lake Dodge',	'World Dodge',	'Southfork Dodge',	'Berman Dodge',	'Sacramento Dodge',	'Fox Dodge Southfield',	'Fox Dodge Taylor',	'Castle Dodge',	'Steele North Star Dodge',	'Nielsen Dodge',	'Brooksville Dodge',	'Fontana Dodge',	'Burns Mission',	'Safford Brown Dodge',	'Meador Dodge',	'Lax Dodge',	'Elk Grove Dodge',	'Gastonia Dodge',	'Valley Motor City',	'Simi Valley Dodge',	'Crossroads Dodge',	'Kramer Dodge',	'Randy Marion Dodge',	'Covert Dodge Bee Cave',	'Horne Dodge Show Low',	'Gengras Dodge Fairfield',	'Gunn Dodge',	'Dodge City',	'Park Cities Dodge',	'Bob Sight Dodge',	'Larry Roesch Dodge',	'Burns Motors',	'Suresky Dodge',	'Buhler Dodge',	'Fred Frederick Dodge',	'Rothrock Dodge',	'North Olmsted Dodge',	'AutoNation Dodge',	'Ourisman Dodge',	'Thomas Dodge',	'Boniface-Hiers Dodge',	'Dutchess Dodge',	'Ken Ganley Dodge Bedford',	'Crown Dodge',	'Daytona Dodge',	'Fred Beans Dodge',	'Dayton Andrews Dodge',	'Johnson Dodge',	'Landmark Dodge',	'Steve White Dodge',	'Kindle Dodge',	'Dick Scott Dodge',	'Security Dodge',	'AutoNation Dodge',	'Cerritos Dodge',	'Tuttle-Click\'s Dodge',	'Jeff D\'Ambrosio Dodge',	'Huffines Dodge Lewisville',	'Earnhardt Dodge',	'Gladstone Dodge',	'AutoNation Dodge',	'Vance Dodge Guthrie',	'Moss Bros. Dodge',	'DARCARS Orange Park Dodge',	'South Oak Dodge',	'Safford Dodge',	'Brown Dodge',	'Chapman Las Vegas Dodge',	'All Star Dodge',	'Don Davis Dodge',	'Sawyer Motors',	'Dodge of Winter Haven',	'DeMontrond Dodge',	'Dover Dodge',	'Palmer Dodge',	'Kernersville Dodge',	'Hunt Chrysler Center',	'Taylor Dodge',	'Landmark Dodge',	'Tempe Dodge',	'Hendrick Dodge',	'Athens Dodge',	'Cummins Dodge',	'AutoNation Dodge Houston',	'Chapman Dodge Scottsdale',	'Larry H. Miller Dodge',	'Sherman Dodge',	'San Marcos Dodge',	'David Stanley Dodge',	'Frank Fletcher Dodge',	'Glenn Polk Dodge',	'Antioch Dodge',	'Ryburn Motor Company',	'Scott Evans Dodge',	'Dodge of Paramus',	'Brown-Daub Dodge',	'Danbury Dodge',	'Smith Haven Dodge',	'Hoblit Dodge',	'Szott M-59 Dodge',	'Progressive Dodge',	'AutoNation Dodge',	'AutoNation Dodge Katy',	'Rockwall Dodge',	'Bluebonnet Dodge',	'Garavel Dodge',	'Safford Dodge',	'Savage 61 Dodge',	'Port Lavaca Dodge',	'Helfman Dodge',	'Gulfgate Dodge',	'AutoNation Dodge',	'Fowler Dodge',	'Greenway Dodge',	'Dallas Dodge',	'Dodge City of McKinney',	'Hawk Dodge',	'Jacksonville Dodge',	'Napleton\'s Dodge',	'Jim Riehl\'s Friendly CDJR',	'Mac Haik Dodge',	'DCH Dodge of Temecula',	'David Dodge',	'Carman Dodge',	'Bill Harris Dodge',	'Capital Dodge',	'Olathe Dodge',	'Moss Bros. Dodge',	'Robert Loehr Dodge',	'University Dodge',	'Stevens Creek Dodge',	'Champion Dodge',	'Tomball Dodge',	'Jim Browne Dodge',	'Medina Auto Mall',	'Big Star Dodge',	'Courtesy Dodge',	'Northwest Dodge',	'Route 46 Dodge',	'Wickstrom Dodge',	'Lone Star Dodge',	'Jack Phelan Dodge',	'Zeigler Dodge',	'Nyle Maxwell Dodge',	'Nyle Maxwell Dodge',	'Grapevine Dodge',	'Gillman Dodge',	'Westgate Dodge',	'Napleton\'s Clermont Dodge',	'Safford Dodge',	'Ray Laethem Dodge',	'Hendrick Dodge of Concord',	'Ganley Village Dodge',	'Covert Dodge',	'Empire Dodge',	'Turlock Dodge',	'Jacksonville Dodge',	'Richardson Dodge',	'Courtesy Dodge',	'Texan Dodge',	'Larry H. Miller Dodge',	'Rydell Dodge',	'Paulding Dodge',	'Rick Hendrick Dodge',	'Thunder Dodge',	'Freeland Dodge',	'Jerry Ulm Dodge',	'Platinum Dodge',	'LaLonde Dodge',	'Freedom Dodge by Ed Morse',	'Moran Blue Water Dodge',	'Southwest Dodge',	'Boggus Tipton Dodge',	'Randy Marion Dodge',	'Arrigo Dodge at Sawgrass',	'Beaman Dodge',	'Feldman Dodge',	'Merrick Dodge',	'Pegasus Dodge',	'Towbin Dodge',	'Suburban Dodge',	'Sarasota Dodge',	'Dodge of Woodstock',	'Shottenkirk Dodge',	'Denton Dodge',	'Dodge of Princeton',	'Aaron Dodge',	'Orlando Dodge',	'Ourisman Dodge',	'Hunter Dodge',	'Tasca Dodge White Plains',	'Matt Blatt Dodge',	'Mt. Juliet Dodge',	'Greensboro Dodge',	'Fayetteville Dodge',	'Cable Dahmer Dodge',	'Tasca Dodge Kingston',	'Dodge of Leesburg',	'McCarthy Dodge',	'Crossroads Dodge',	'McSweeney Dodge Clanton',	'Bomnin Dodge Doral',	'Ed Payne Motors',	'Junction Auto Sales',	'Sliman\'s Sales & Service',	'Glenn E. Thomas Dodge',	'Spitzer Motors',	'Bettenhausen Dodge',	'Dadeland Dodge',	'Galeana\'s Van Dyke Dodge',	'Grieger\'s Motor Sales',	'Cherry Hill Dodge',	'Monroe Dodge Superstore',	'Massey Yardley Dodge',	'Moss Bros. Dodge',	'Glendale Dodge',	'Sterling Heights Dodge',	'Airpark Dodge',	'John Hiester Dodge',	'Reedman Toll Auto World',	'Fair Oaks Dodge',	'St. Clair Dodge',	'Mac Haik Dodge',	'Bill Volz Westchester',	'Garden City Dodge',	'Riverdale Dodge',	'Lakeland Dodge',	'Stateline Dodge',	'DARCARS Dodge',	'Airport Dodge',	'Ferman Dodge',	'Chapman Dodge',	'Ginn Dodge',	'Safford Dodge',	'Stoneridge Dodge',	'Boerne Dodge',	'Sport Durst Dodge',	'Criswell Dodge',	'St. Charles Dodge',	'Hudson Dodge',	'Joey Accardi Dodge',	'Waxahachie Dodge',	'Bayshore Dodge',	'Lester Glenn Dodge',	'Redlands Dodge',	'Eastchester Dodge',	'Miami Lakes Dodge',	'Puente Hills Dodge',	'Spitzer Dodge Cleveland',	'Arlington Heights Dodge',	'Barbera\'s Autoland',	'Walker-Jones Dodge',	'Columbia Dodge',	'Hendrick Dodge',	'Hemet Dodge',	'San Antonio Dodge',	'Stewart Dodge',	'Jones Dodge',	'Posner Park Dodge',	'York Dodge',	'Kendall Dodge',	'Seth Wadley Dodge',	'Aventura Dodge',	'Gwinnett Dodge',	'Scott Robinson Dodge',	'Bert Ogden Dodge',	'Larry H. Miller Dodge',	'Ourisman Dodge of Bowie',	'Ken Ganley Dodge',	'AutoNation Dodge Spring',	'Deacon\'s Dodge',	'Orr Dodge of Russellville',	'Van Nuys Dodge',	'Norristown Dodge',	'Elgin Dodge',	'Classic Dodge',	'Autoland Dodge',	'Brooklyn Dodge',	'McSweeney Dodge',	'Key West Dodge',	'Lake City Dodge',	'Earnhardt Dodge',	'Ken Ganley Dodge',	'Northland Dodge',	'Central Florida Dodge',	'Rockland Dodge',	'Dodge of Englewood Cliffs',	'Bedford Dodge',	'Feldman Dodge',	'Courtesy Dodge',	'Hudson Valley Dodge',	'Don Jackson Dodge North',	'Jim Riehl\'s Friendly CDJR',	'Rhythm Dodge',	'Golling Dodge',	'Rossi Dodge',	'Voyles Dodge',	'Champion Dodge',	'Arrigo Dodge Margate',	'LaFontaine Dodge',	'Morgan Hill Dodge',	'Union City Dodge',	'Future Dodge of Fairfield',	'Suburban Dodge',	'Suburban Dodge',	'Suburban Dodge of Troy',	'United Dodge',	'Victorville Motors',	'Dodge of Manhattan',	'Desert 215 Superstore',	'Sahara Dodge',	'Bridgeton Dodge',	'Dodge of Tampa Bay',	'Ciocca CDJR of Flemington',	'Lake Norman Dodge',	'Koons Tysons Dodge',	'South Shore Dodge',	'Serra Dodge Lake Orion',	'McPeek\'s Dodge of Anaheim',	'Tri County Dodge',	'Westborn Dodge',	'Teterboro Dodge',	'Central Ave. Dodge',	'Dayton Andrews Dodge',	'Johnsons of Kingfisher',	'Meadowland of Carmel',	'Lansdale Dodge',	'Central Valley Dodge',	'Gupton Motors',	'DARCARS Dodge',	'Gator Dodge',	'Hayes Dodge',	'Atlantic Dodge',	'Helfman River Oaks Dodge',	'Ingram Park Dodge',	'Rochester Hills Dodge',	'Manahawkin Dodge',	'Suncoast Dodge',	'East Hills Dodge',	'Ed Tomko Dodge',	'Tate Dodge Frederick',	'Dick Huvaere\'s Dodge',	'Pinckney Dodge',	'Bayside Dodge',	'Bergey\'s Dodge',	'Akins Dodge',	'Robert Green Dodge',	'Fullerton Dodge',	'Ed Voyles Dodge',	'Anderson Dodge',	'Golling Dodge',	'Ramsey Dodge',	'Ralph Sellers Dodge',	'Ram Country Del Rio',	'Deacon Jones Dodge',	'Pettijohn Auto Center',	'Wally Armour Dodge',	'Huffines Dodge Plano',	'Tyson Motor Dodge',	'Scott Wood Dodge',	'Troncalli Dodge',	'River Front Dodge',	'Deland Dodge',	'Brunswick Auto Mart',	'Port Jeff Dodge',	'North Point Dodge',	'Klaben Dodge',	'Mall of Georgia Dodge',	'Frontier Dodge',	'Mike Patton Dodge',	'Town & Country Dodge',	'Moritz Dodge',	'Williams Dodge',	'Allways Atascosa Dodge',	'i.g. Burton Dodge',	'Franklin Sussex Auto Mall',	'Garber Dodge',	'Phillips Dodge',	'Healey Dodge',	'Hilltop Dodge',	'Parkway Dodge',	'Pine Belt Dodge',	'Classic Dodge',	'New Smyrna Dodge',	'Tubbs Brothers Dodge',	'Brown-Daub Dodge',	'DARCARS Dodge',	'Cabral Dodge',	'Bob Moore Dodge',	'Walnut Creek Dodge',	'Horne Dodge',	'Asheboro Dodge',	'Ancira Dodge Eagle Pass',	'Myers Dodge',	'Mount Airy Dodge',	'Southern Dodge',	'Major World Dodge',	'Mojave Dodge of Barstow',	'Jacky Jones Dodge',	'Golling Dodge of Chelsea',	'Santa Monica Dodge',	'Tri State Dodge',	'Thurston Dodge',	'Bayer Dodge',	'Plaza Dodge',	'Cuero Dodge',	'Williams Brothers Dodge',	'Sterling Dodge',	'Hanlees Dodge of Napa',	'Ray Dodge',	'Patriot Dodge of Chandler',	'Riser Dodge',	'Hillsborough Dodge',	'Fieldhouse Dodge',	'A.J. Dohmann Dodge',	'Southwest Dodge',	'Red River Dodge',	'Boardwalk Dodge',	'Parks Dodge Space Coast',	'Victory Dodge of Ottawa',	'Elder Dodge Cedar Creek',	'Countryside Dodge',	'John Hiester Dodge',	'Brady Dodge',	'Fitzgerald Dodge',	'Sunnyvale Dodge',	'James Dodge of Cedar Lake',	'Cox Dodge',	'Mainstreet Dodge',	'Dodge of Willoughby',	'Price Dodge',	'Yaklin Dodge of Angleton',	'Firelands Dodge',	'Ron Carter Dodge',	'Huston Dodge',	'Steele Dodge Gonzales',	'Steele Dodge Lockhart',	'Montrose Dodge',	'Momentum Dodge',	'CMA\'s Dodge',	'Team Dodge of Morganton',	'Kunes Dodge of Sycamore',	'White\'s Auto Mall Dodge',	'John L. Sullivan Dodge',	'CardinaleWay Dodge',	'Gerry Lane Dodge',	'Knight Claremont Dodge',	'Dodge of Chicago',	'Joshua Tree Dodge',	'Vance Auto Group',	'Sarchione Dodge',	'Horne Dodge Safford',	'Kalidy Dodge',	'Healdsburg Dodge',	'Mt. Ephraim Dodge',	'Daystar Dodge',	'Sharp Dodge',	'Glendora Dodge',	'Bruner Motors',	'Elder Dodge',	'Martin Swanty Dodge',	'Flagler Dodge',	'Oxendale Dodge',	'Village Dodge',	'Karl Klement Dodge',	'Chapman Payson Dodge',	'Don Davis Motor Company',	'Dick Scott Motor Mall',	'Performance Dodge',	'Perris Valley Dodge',	'Milford Chrysler Sales',	'Marlow Motor Company',	'Midway Dodge',	'Country Dodge',	'Jim Burke Dodge',	'South Chicago Dodge',	'Advantage Dodge',	'Dodge of Vacaville',	'Waldorf Dodge',	'Dodge of Culpeper',	'Port Jervis Auto Mall',	'Petrus Auto Sales',	'Bennett Dodge',	'A.J. Dohmann Dodge',	'Jacky Jones Dodge',	'Russell Barnett Dodge',	'Savage L&B Dodge',	'Sport Dodge',	'Cecil Atkission Motors',	'Antioch Dodge',	'Lucas Dodge',	'Abernethy Dodge',	'Dodge of Warwick',	'Rio Vista Dodge',	'Outten Dodge',	'Superior Dodge of Conway',	'Wooster Dodge',	'Pearl Dodge',	'Martin Dodge',	'New Century Dodge',	'Buckeye Superstore',	'Orr Dodge',	'Max Dodge of Butler',	'Oviedo Dodge',	'Napleton River Oaks Dodge',	'Woody\'s Dodge',	'Barry Sanders Supercenter',	'Smart Dodge',	'Black Dodge',	'Spitzer Dodge Homestead',	'Greenway Dodge',	'Team One Dodge of Gadsden',	'Greenway Dodge of Rome',	'Classic Dodge',	'Ram Country Mineral Wells',	'Lee Dodge',	'Lake Wales Dodge',	'Performance Dodge',	'Joe Ricci Marlette Dodge',	'I20 Dodge',	'Auburn Dodge',	'Elliott Dodge Palestine',	'Albemarle Dodge',	'Heartland Dodge',	'Reliance Dodge',	'Westgate Dodge',	'Family Dodge',	'i.g. Burton Dodge',	'Davis Dodge of Yulee',	'Airport Dodge',	'Sulphur Springs Dodge',	'Brinson Dodge',	'Miracle Dodge',	'Universal Dodge',	'Jenkins Dodge',	'Meadows Dodge',	'W-K Dodge of Sedalia',	'Burlington Dodge',	'Ram Country Wharton',	'Clay Maxey Dodge',	'Genthe Dodge',	'Freedom Dodge',	'Max Dodge Clinton',	'Sierra Motors',	'Quigley Dodge',	'Freehold Dodge',	'Schaffer Danhoff Dodge',	'Sunnyside Company',	'Reagle Dodge',	'Cullman Dodge',	'Stockton Dodge',	'Parkway Dodge',	'Dependable Dodge',	'Coronet Dodge',	'White Dodge',	'Marshall Dodge',	'Prince Frederick Dodge',	'Brenham Dodge',	'Putnam Dodge',	'Alan Jay Dodge',	'Leith Dodge',	'Reedman Toll Dodge',	'Liccardi Dodge',	'Duvall Dodge',	'Rocky Mount Dodge',	'Fremont Dodge',	'Payne Rio Dodge',	'Thompsons Dodge',	'Reedman Toll Dodge',	'Sames Bastrop Dodge',	'Dodge Southampton',	'Steve Jones Dodge',	'Boyd Dodge of South Hill',	'Hanlees Davis Dodge',	'Matt Mazzei Dodge',	'Michigan City Dodge',	'James Dodge',	'Timbrook Dodge',	'Sonora Dodge',	'Weimer Dodge of Keyser',	'All American Dodge',	'Bayside Dodge',	'Tracy Dodge',	'Bill Penney Dodge',	'Gilroy Dodge',	'Criswell Dodge',	'Auto Gallery Dodge',	'Riverhead Dodge',	'Tuscaloosa Dodge',	'Preston Dodge',	'Finn Dodge',	'Boone Dodge',	'i.g. Burton Dodge',	'Preston Dodge of Dover',	'Skyway Dodge',	'Lipscomb Dodge',	'Weekley Dodge',	'Mullen Motors',	'Ruge\'s Dodge',	'Crenwelge Motor Sales',	'Rentschler Dodge',	'La Porte Dodge',	'Greenway Dodge',	'Prescott Brothers',	'DARCARS Dodge',	'Crenwelge Motors',	'Hagans Dodge',	'Gary Mathews Dodge',	'Pamby Motors',	'Larchmont Dodge',	'Tri-City Dodge',	'Sands Dodge',	'Hayes Dodge',	'DeCozen Dodge',	'Beck Dodge',	'Lilliston Dodge',	'Peppers Dodge',	'Autoworld Dodge',	'Stan McNabb Dodge',	'Mountain Valley Dodge',	'James O\'Neal Dodge',	'Swanty\'s Dodge',	'Atlantic Dodge',	'Star Dodge',	'Spirit Dodge',	'Cumberland Dodge',	'Dempsey Dodge',	'Jay Hodge Dodge of Paris',	'Jackson Dodge',	'Miracle Dodge',	'Cecil Atkission Motors',	'Marburger Dodge',	'Bleecker Dodge',	'Warrensburg Dodge',	'Griffin Dodge',	'Fitzgerald Dodge',	'Vann Dodge',	'Leith Dodge Wendell',	'Weimer Dodge',	'Saitta Trudeau Dodge']

# Set the path to the folder containing the client folders
#FUTURE DAMON READ THIS
# Do not copy and paste directly, we need forward slashes in python for this to work.
parent_folder = "C:/Users/damon.melton/Documents/Display Ads/Power Days Promo"
source = "C:/Users/damon.melton/Documents/Display Ads/Power Days Promo/Default"

#make client folders

completed = []

for client in clients:
    if client in completed:
        continue
    destination = parent_folder + "/" + client
    shutil.copytree(source, destination)
#edit and zip index files
    for folder in os.listdir(destination):
        filename = "index.html"
        dealer_name = "Descriptive Dealership Name of City and State"
        file_path = os.path.join(destination, folder, filename)
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                print(line.replace(dealer_name, client), end='')
        shutil.make_archive(os.path.join(destination, f'{folder}'),'zip',destination,folder)
    completed.append(client)