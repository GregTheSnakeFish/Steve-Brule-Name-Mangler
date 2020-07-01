# Steve-Brule-Name-Mangler
This program gives you a new mangled name based on John C. Reily's hilarious Steve Brule character: (https://www.youtube.com/watch?v=02iIN4n4y0A). The algorithm is ridiculous because the tool should seem to assign the mangled names randomly but actually be deterministic but tough to predict in order to be funniest. Also, canon names from the show should be preserved. Cindy Driscoll, for example, should become Cynthia Dangus. But I didn't just want to make too many of them one-to-one changes, so if you notice a canon name that I missed or that comes out wrong, please ping me so I can add it! I will credit you here for all eternity, unless you ask me not to.

topnames.txt is the file of 1000 male and 1000 female first names which are popular according to https://www.verywellfamily.com/top-1000-baby-boy-names-2757618 and https://www.verywellfamily.com/top-1000-baby-girl-names-2757832. They are skewed toward Western names but still include many of the most popular names worldwide. Reliable data for true worldwide average names was not readily available. I ran these 2000 names through the included filter namefilter.py of the algorithm to determine if any were missed, and adjusted appropriately until all 2,000 names passed. So, very few names should incur the built-in safeguard output. If a name does give the safeguard output (in which case it will be unchanged), ping me and I will adjust! Similar things apply to the last names, which were sourced from Wolfram Alpha and filtered with the file lastnamefilter.py.

NOTE: I uploaded the namefilter.py file that was used at the point when 30 of the 2000 first names still weren't getting changed, just to show the example. It also prints the total number of unchanged names at the end. You can look at brulename.py and see what needs to be changed in namefilter.py to get none of the names to come through, or use it to make your own filter.

In progress. (Beta version available)
