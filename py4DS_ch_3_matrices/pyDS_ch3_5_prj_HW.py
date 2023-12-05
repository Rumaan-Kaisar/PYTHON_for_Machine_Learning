
################# 4.11: full, 4.12 : 5:0
# copy:  
#        
#        
################# (3-dec-23 for 5-dec-23)

# Courses: A-Z PY for Data-Science    4.10, 4.11, 4.12


# --------    Import following Data    --------

# Copyright: Kirill Eremenko, www.superdatascience.com
""" 
    Instructions for this dataset:
        Simply copy ALL the lines in this script by pressing CTRL+A on Windows or CMND+A on Mac and  run the Jupyter cell.
    
        Once you have executed the commands the following objects will be created:
            
            Matrices:
                    - Salary
                    - Games
                    - MinutesPlayed
                    - FieldGoals
                    - FieldGoalAttempts
                    - Points
            
            Lists:
                    - Players
                    - Seasons
            
            Dictionaries:
                    - Sdict
                    - Pdict
    


    Comments:
            Seasons are labeled based on the first year in the season
            E.g. the 2012-2013 season is preseneted as simply 2012

    Notes and Corrections to the data:
            Kevin Durant: 2006 - College Data Used
            Kevin Durant: 2005 - Proxied With 2006 Data
            Derrick Rose: 2012 - Did Not Play
            Derrick Rose: 2007 - College Data Used
            Derrick Rose: 2006 - Proxied With 2007 Data
            Derrick Rose: 2005 - Proxied With 2007 Data
"""

# Import numpy & Other modules
import numpy as np      # numpy for matrix calculation
import matplotlib.pyplot as plt     # for visualization

# Ignore Error-warnings "divide by zero"
import warnings
warnings.filterwarnings('ignore')

%matplotlib inline
plt.rcParams['figure.figsize'] = 8, 4


# --------    Seasons    --------
Seasons = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]
Sdict = {"2005":0,"2006":1,"2007":2,"2008":3,"2009":4,"2010":5,"2011":6,"2012":7,"2013":8,"2014":9}

# --------    Players    --------
Players = ["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"]
Pdict = {"KobeBryant":0,"JoeJohnson":1,"LeBronJames":2,"CarmeloAnthony":3,"DwightHoward":4,"ChrisBosh":5,"ChrisPaul":6,"KevinDurant":7,"DerrickRose":8,"DwayneWade":9}

# --------    Salaries    --------
KobeBryant_Salary = [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000]
JoeJohnson_Salary = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790]
LeBronJames_Salary = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
CarmeloAnthony_Salary = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000]
DwightHoward_Salary = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271]
ChrisBosh_Salary = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
ChrisPaul_Salary = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563]
KevinDurant_Salary = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624]
DerrickRose_Salary = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875]
DwayneWade_Salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]
# Matrix
Salary = np.array([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary, ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])

# --------    Games     --------
KobeBryant_G = [80,77,82,82,73,82,58,78,6,35]
JoeJohnson_G = [82,57,82,79,76,72,60,72,79,80]
LeBronJames_G = [79,78,75,81,76,79,62,76,77,69]
CarmeloAnthony_G = [80,65,77,66,69,77,55,67,77,40]
DwightHoward_G = [82,82,82,79,82,78,54,76,71,41]
ChrisBosh_G = [70,69,67,77,70,77,57,74,79,44]
ChrisPaul_G = [78,64,80,78,45,80,60,70,62,82]
KevinDurant_G = [35,35,80,74,82,78,66,81,81,27]
DerrickRose_G = [40,40,40,81,78,81,39,0,10,51]
DwayneWade_G = [75,51,51,79,77,76,49,69,54,62]
# Matrix
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G, KevinDurant_G, DerrickRose_G, DwayneWade_G])

# --------    Minutes Played    --------
KobeBryant_MP = [3277,3140,3192,2960,2835,2779,2232,3013,177,1207]
JoeJohnson_MP = [3340,2359,3343,3124,2886,2554,2127,2642,2575,2791]
LeBronJames_MP = [3361,3190,3027,3054,2966,3063,2326,2877,2902,2493]
CarmeloAnthony_MP = [2941,2486,2806,2277,2634,2751,1876,2482,2982,1428]
DwightHoward_MP = [3021,3023,3088,2821,2843,2935,2070,2722,2396,1223]
ChrisBosh_MP = [2751,2658,2425,2928,2526,2795,2007,2454,2531,1556]
ChrisPaul_MP = [2808,2353,3006,3002,1712,2880,2181,2335,2171,2857]
KevinDurant_MP = [1255,1255,2768,2885,3239,3038,2546,3119,3122,913]
DerrickRose_MP = [1168,1168,1168,3000,2871,3026,1375,0,311,1530]
DwayneWade_MP = [2892,1931,1954,3048,2792,2823,1625,2391,1775,1971]
# Matrix
MinutesPlayed = np.array([KobeBryant_MP, JoeJohnson_MP, LeBronJames_MP, CarmeloAnthony_MP, DwightHoward_MP, ChrisBosh_MP, ChrisPaul_MP, KevinDurant_MP, DerrickRose_MP, DwayneWade_MP])

# --------    Field Goals    --------
KobeBryant_FG = [978,813,775,800,716,740,574,738,31,266]
JoeJohnson_FG = [632,536,647,620,635,514,423,445,462,446]
LeBronJames_FG = [875,772,794,789,768,758,621,765,767,624]
CarmeloAnthony_FG = [756,691,728,535,688,684,441,669,743,358]
DwightHoward_FG = [468,526,583,560,510,619,416,470,473,251]
ChrisBosh_FG = [549,543,507,615,600,524,393,485,492,343]
ChrisPaul_FG = [407,381,630,631,314,430,425,412,406,568]
KevinDurant_FG = [306,306,587,661,794,711,643,731,849,238]
DerrickRose_FG = [208,208,208,574,672,711,302,0,58,338]
DwayneWade_FG = [699,472,439,854,719,692,416,569,415,509]
# Matrix
FieldGoals  = np.array([KobeBryant_FG, JoeJohnson_FG, LeBronJames_FG, CarmeloAnthony_FG, DwightHoward_FG, ChrisBosh_FG, ChrisPaul_FG, KevinDurant_FG, DerrickRose_FG, DwayneWade_FG])

# --------    Field Goal Attempts    --------
KobeBryant_FGA = [2173,1757,1690,1712,1569,1639,1336,1595,73,713]
JoeJohnson_FGA = [1395,1139,1497,1420,1386,1161,931,1052,1018,1025]
LeBronJames_FGA = [1823,1621,1642,1613,1528,1485,1169,1354,1353,1279]
CarmeloAnthony_FGA = [1572,1453,1481,1207,1502,1503,1025,1489,1643,806]
DwightHoward_FGA = [881,873,974,979,834,1044,726,813,800,423]
ChrisBosh_FGA = [1087,1094,1027,1263,1158,1056,807,907,953,745]
ChrisPaul_FGA = [947,871,1291,1255,637,928,890,856,870,1170]
KevinDurant_FGA = [647,647,1366,1390,1668,1538,1297,1433,1688,467]
DerrickRose_FGA = [436,436,436,1208,1373,1597,695,0,164,835]
DwayneWade_FGA = [1413,962,937,1739,1511,1384,837,1093,761,1084]
# Matrix
FieldGoalAttempts = np.array([KobeBryant_FGA, JoeJohnson_FGA, LeBronJames_FGA, CarmeloAnthony_FGA, DwightHoward_FGA, ChrisBosh_FGA, ChrisPaul_FGA, KevinDurant_FGA, DerrickRose_FGA, DwayneWade_FGA])

# --------    Points    --------
KobeBryant_PTS = [2832,2430,2323,2201,1970,2078,1616,2133,83,782]
JoeJohnson_PTS = [1653,1426,1779,1688,1619,1312,1129,1170,1245,1154]
LeBronJames_PTS = [2478,2132,2250,2304,2258,2111,1683,2036,2089,1743]
CarmeloAnthony_PTS = [2122,1881,1978,1504,1943,1970,1245,1920,2112,966]
DwightHoward_PTS = [1292,1443,1695,1624,1503,1784,1113,1296,1297,646]
ChrisBosh_PTS = [1572,1561,1496,1746,1678,1438,1025,1232,1281,928]
ChrisPaul_PTS = [1258,1104,1684,1781,841,1268,1189,1186,1185,1564]
KevinDurant_PTS = [903,903,1624,1871,2472,2161,1850,2280,2593,686]
DerrickRose_PTS = [597,597,597,1361,1619,2026,852,0,159,904]
DwayneWade_PTS = [2040,1397,1254,2386,2045,1941,1082,1463,1028,1331]
# Matrix
Points = np.array([KobeBryant_PTS, JoeJohnson_PTS, LeBronJames_PTS, CarmeloAnthony_PTS, DwightHoward_PTS, ChrisBosh_PTS, ChrisPaul_PTS, KevinDurant_PTS, DerrickRose_PTS, DwayneWade_PTS])             
                  




# --------    Project : BASKETBALL INSIGHTS    --------
# In this section we'll analyze the 'NBA'-data for Different "Basketball-players"
# We'll use our previous function (it takes Data as paramters, also uses 'Default Values')
def myPlot(data, list_of_player_name = Players):
    col_r = {"KobeBryant":"Black","JoeJohnson":"Red","LeBronJames":"Green","CarmeloAnthony":"Blue","DwightHoward":"Magenta","ChrisBosh":"Black","ChrisPaul":"Red","KevinDurant":"Green","DerrickRose":"Blue","DwayneWade":"Magenta"}
    mr_kr = {"KobeBryant":"s","JoeJohnson":"o","LeBronJames":"^","CarmeloAnthony":"D","DwightHoward":"s","ChrisBosh":"o","ChrisPaul":"^","KevinDurant":"D","DerrickRose":"s","DwayneWade":"o"}
    for name in list_of_player_name:
        plt.plot(data[Pdict[name]], ls='-.', c=col_r[name], marker = mr_kr[name], ms=7, label = name)
    # legend positioning
    plt.legend(loc='lower left', bbox_to_anchor=(.5,.5))
    plt.legend(loc='upper left', bbox_to_anchor=(1,1))
    plt.xticks(list(range(0, len(Seasons))), Seasons, rotation = 'vertical')


# -----------    We'll focus on "Analytics" and "Data-Science"    -----------
# Basically in this part we dont code anything new
    # But we'll try to understand the data in the "Data-Analysis" prespective
        # Well try to figure-out 'Anomalies/Irregularities '
        # correlations between different data




# Games Insights : Visualization of Game Played by world's top 10 BASKETBALL-players
myPlot(Games)


# --------    Visualization 1: Salary Metrices (salary vs in-game statistics)    --------
# Salary
myPlot(Salary)
# notice 'KobeBryant' has over $30 million salary, second is 'JoeJohnson'

# Salary-per game
myPlot(Salary/Games)    # Matrix Division
# Notice Anomalies for 'KobeBryant' and 'DerrickRose'
    # are they getting paid 'Very high' per the games they played?
    # the reason is: They were injured during that season 2013-2014, but they fuly paid
    # so they 'played very-few game' due to the injury but 'fully paid'
    # that's why the salary per-game is so high

    # This same Anomalies also happen to 'Salary-per FieldGoals' for the same reason

# Salary-per FieldGoals
myPlot(Salary/FieldGoals)    # Matrix Division
# However, we could remove these anomalies in 'Data-analytics-point of view'


# Coclusion:
    #  "salary vs in-game statistics" might not be a good option
    # Salary is not effected by injuries due to their COTRACTS
    # but "in-game statistics" is effected by injuries
    # so should not visualize "salary & in-game statistics" togather



 
# --------    Visualization 2: In-game Metrices (in-game statistics only)    --------
# Minuets Played
myPlot(MinutesPlayed)

# points
myPlot(Points)

# Notice for both case 'MinutesPlayed' and 'Points' the anomalies appear again
    # The value decrease for 'KobeBryant' and 'DerrickRose'
    # INJURIES affecting our visualization again


# The Question is: how do we fix these anomalies?
    # How do we avoid 'injuries' type anomaly (irregularity) from our visualization?




# --------    Normalization : To avoid anomalies    --------
# Since all game-statistics are affected by the injuries, we can normalize 'in-game-matrix by in-game-matrix'

# --------    Visualization 3: In-Game Metrics Normalized    --------
# 'FieldGoals' without normalization
myPlot(FieldGoals)

# ----    Following are comarable now    ----

# NORMALIZE 'FieldGoals' dividing it by 'Games'
    # The 'injuries' of 'KobeBryant' and 'DerrickRose' are also visible but comparable to other players
myPlot(FieldGoals/Games)

# NORMALIZE 'FieldGoals' dividing it by 'FieldGoalAttempts' (Success rate)
    # It is kind of accuracy of the player
    # notice 'DwightHoward' is above all and more accurate (60% accuracy)
        # But he's 5th highest paid player. Why? we'll get the answer in the next plot.
myPlot(FieldGoals/FieldGoalAttempts)

# normalized 'FieldGoalAttempts' (Attempt rate)
    # notice 'DwightHoward' is now at the bottom
    # we know from previous plot 'DwightHoward' is more accurate but he makes 'less attempts than others'
    # this makes him 5th paid player
    # It also says that he doesn't score many points in a game (next plot)
myPlot(FieldGoalAttempts/Games)

myPlot(Points/Games) # normalized 'Points'




# --------    Interest±ng Observation    --------
# notice 'MinutesPlayed/Games' are decreasing  for the players
    # They're playing less minutes per game
    # However, they are playing same amount of games (more or less), notice the 'Games' plot
myPlot(MinutesPlayed/Games) 

myPlot(Games)




# --------    Time is valuable    --------
# Find out the playes who 'spend times efficiently'
# Scored most 'FieldGoals' per 'MinutesPlayed'

# Notice 'KevinDurant' is increasing, he's young and he uses time more efficiently
# also notice there are 'two group of players' appears in the plot
    # according to their time usage efficiency

        # KevinDurant
        # LeBronJames
        # CarmeloAnthony
        # DwayneWade


        # JoeJohnson
        # DwightHoward
        # ChrisBosh
        # ChrisPaul

myPlot(FieldGoals/MinutesPlayed)




# --------    Player Style    --------
# we plot the 'Points' per 'FieldGoals'
# 2-point-goal or 3-point-goal

# BUT some of our data is above 3-points, because there are 'free-shots'
# We notice that the player-style of some player is changing
    # Eg: 'KevinDurant', at the beginniong he used 2-point-goal but later he changed to 3-point-goal
    # also notice the chanhe of 'KobeBryant' and 'ChrisBosh'
myPlot(Points/FieldGoals)

# conclusion:
# we can observe many things/insights from plotting those data: 
    # Whats the cause of these changes
    # Trainers tell them to changes their styles
    # other trends in basketball that change over time




# --------    Section recap    --------

# In this section we learned:
# 1.	Matrices
# 2.	Building matrices: 
            # np.reshape
                # (*,*,'C') : C-like 'row-by-row'
                # (...'F') : Fortran-like 'column-by-column'
            
            # np.array()
                # combining differnt types of lists


# 3.	Dictionaries in Python
# 4.	Matrix Operations
# 5.	Visualizing with Pyplot
# 6.	Creating your first function
# 7.	Advanced function design (using dictionary)
# 8.	Deriving insights




# --------    Basketball free throws    --------
# we'll investigate the trends of free throws
    # free-throw is a kind of penalty (for making a fawl)
    # Each Free Throw is worth 1 point

# we'll work for two more game statistics


# You have been supplied data for two more additional in-game statistics:
    # Free Throws
    # Free Throw Attempts

# Data will be in vector form, first cretae matrices before start calculations
    # The data has been supplied in the form of vectors. 
    # You will have to create the two matrices before you proceed with the analysis
    # also use previous data 'Games' and 'Points' matrices
    # to investigate further also visialize 'FieldGoals'  and 'FieldGoalAttempts'

# You need to create three plots that portray the following insights:
    # Free Throw Attempts per game
    # Accuracy of Free Throws
    # Player playing style (2 vs 3 points preference) excluding Free Throws*



# --------    Hints    --------
# The matrix calculation for part 3 is:
    # (Points - FreeThrows)/FieldGoals

# Steps:
# ----  Prepare Data  ----
# library import
# Seasons & Season-dictionary
# Players & Players-dictionary
# Free Throws (Matrix Data)
# Free Throws Atempts (Matrix Data)
# Check matices FreeThrows, FreeThrowAttempts
# Define function


# ----  Visualize 1  ----
# Visualize 'FreeThrows'
# Visualize 'FreeThrowAttempts'


# ----  Visualize 2 : Free Throw Attempts per Games  ----
# Games (Matrix Data)
# Visualize 'FreeThrowAttempts / Games'
    # Notice how Chris Paul gets few attempts per game


# ----  Visualize 3 : Free Throw Accuracy  ----
# Visualize 'Free Throw Accuracy = FreeThrows / FreeThrowAttempts'
    # And yet Chris Paul's accuracy is one of the highest Chances are his team would get more points if he had more FTA's.
    # Also notice that Dwight Howard's FT Accuracy is extremely poor compared to other players. If you recall, Dwight Howard's Field Goal Accuracy was exceptional:


# ----  Visualize 4 : Field Goal Accuracy  ----
# FieldGoals (Matrix Data)
# FieldGoalattempts (Matrix Data)
# Visualize 'Field Goal Accuracy = FieldGoals / FieldGoalattempts'
    # How could this be? Why is there such a drastic difference?
    # We will see just now...


# ----  Visualize 5 : Points excluding FreeThrows  ----
# Points (Matrix Data)
# Visualize Player Style Patterns Excluding Free Throws '(Points - FreeThrows)/FieldGoals'

""" 
Because we have excluded free throws, this plot now shows us 
the true representation of player style change. We can verify
that this is the case because all the marks without exception
on this plot are between 2 and 3. That is because Field Goals
can only be for either 2 points or 3 points.

Insights:
1. You can see how players' preference for 2 or 3 point shots
   changes throughout their career. We can see that almost all
   players in this dataset experiment with their style throughout
   their careers. Perhaps, the most drastic change in style has
   been experienced by Joe Johnson.

2. There is one exception. You can see that one player has not
   changed his style at all - almost always scoring only 2-pointers.
   Who is this mystert player? It's Dwight Howard! 
   Now that explains a lot. The reason that Dwight Howard's
   Field Goal accuracy is so good is because he almost always
   scores 2-pointers only. That means he can be close to the basket
   or even in contact with it. Free throws, on the other hand require
   the player to stand 15ft (4.57m) away from the hoop. That's 
   probably why Dwight Howard's Free Throw Accuracy is poor.
 """




# --------  Prepare Data  --------

# ----  library import  ----
# Import numpy & Other modules
import numpy as np      # numpy for matrix calculation
import matplotlib.pyplot as plt     # for visualization

# Ignore Error-warnings "divide by zero"
import warnings
warnings.filterwarnings('ignore')

%matplotlib inline
plt.rcParams['figure.figsize'] = 8, 4


# --------    Seasons & Season-dictionary    --------
Seasons = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]
Sdict = {"2005":0,"2006":1,"2007":2,"2008":3,"2009":4,"2010":5,"2011":6,"2012":7,"2013":8,"2014":9}

# --------    Players & Players-dictionary    --------
Players = ["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"]
Pdict = {"KobeBryant":0,"JoeJohnson":1,"LeBronJames":2,"CarmeloAnthony":3,"DwightHoward":4,"ChrisBosh":5,"ChrisPaul":6,"KevinDurant":7,"DerrickRose":8,"DwayneWade":9}


# --------    Check matices FreeThrows, FreeThrowAttempts    --------
# --------    Define function    --------




# --------    HW data    --------

# --------    Free Throws (Matrix Data)    --------
KobeBryant_FT = [696,667,623,483,439,483,381,525,18,196]
JoeJohnson_FT = [261,235,316,299,220,195,158,132,159,141]
LeBronJames_FT = [601,489,549,594,593,503,387,403,439,375]
CarmeloAnthony_FT = [573,459,464,371,508,507,295,425,459,189]
DwightHoward_FT = [356,390,529,504,483,546,281,355,349,143]
ChrisBosh_FT = [474,463,472,504,470,384,229,241,223,179]
ChrisPaul_FT = [394,292,332,455,161,337,260,286,295,289]
KevinDurant_FT = [209,209,391,452,756,594,431,679,703,146]
DerrickRose_FT = [146,146,146,197,259,476,194,0,27,152]
DwayneWade_FT = [629,432,354,590,534,494,235,308,189,284]
# Matrix
FreeThrows = np.array([KobeBryant_FT, JoeJohnson_FT, LeBronJames_FT, CarmeloAnthony_FT, DwightHoward_FT, ChrisBosh_FT, ChrisPaul_FT, KevinDurant_FT, DerrickRose_FT, DwayneWade_FT])


# --------    Free Throws Atempts (Matrix Data)    --------
KobeBryant_FTA = [819,768,742,564,541,583,451,626,21,241]
JoeJohnson_FTA = [330,314,379,362,269,243,186,161,195,176]
LeBronJames_FTA = [814,701,771,762,773,663,502,535,585,528]
CarmeloAnthony_FTA = [709,568,590,468,612,605,367,512,541,237]
DwightHoward_FTA = [598,666,897,849,816,916,572,721,638,271]
ChrisBosh_FTA = [581,590,559,617,590,471,279,302,272,232]
ChrisPaul_FTA = [465,357,390,524,190,384,302,323,345,321]
KevinDurant_FTA = [256,256,448,524,840,675,501,750,805,171]
DerrickRose_FTA = [205,205,205,250,338,555,239,0,32,187]
DwayneWade_FTA = [803,535,467,771,702,652,297,425,258,370]
# Matrix
FreeThrowAttempts = np.array([KobeBryant_FTA, JoeJohnson_FTA, LeBronJames_FTA, CarmeloAnthony_FTA, DwightHoward_FTA, ChrisBosh_FTA, ChrisPaul_FTA, KevinDurant_FTA, DerrickRose_FTA, DwayneWade_FTA])


# Check matices FreeThrows, FreeThrowAttempts
FreeThrows
FreeThrowAttempts


# Define PLOT function
def myPlot(data, list_of_player_name = Players):
    col_r = {"KobeBryant":"Black","JoeJohnson":"Red","LeBronJames":"Green","CarmeloAnthony":"Blue","DwightHoward":"Magenta","ChrisBosh":"Black","ChrisPaul":"Red","KevinDurant":"Green","DerrickRose":"Blue","DwayneWade":"Magenta"}
    mr_kr = {"KobeBryant":"s","JoeJohnson":"o","LeBronJames":"^","CarmeloAnthony":"D","DwightHoward":"s","ChrisBosh":"o","ChrisPaul":"^","KevinDurant":"D","DerrickRose":"s","DwayneWade":"o"}
    for name in list_of_player_name:
        plt.plot(data[Pdict[name]], ls='-.', c=col_r[name], marker = mr_kr[name], ms=7, label = name)
    # legend positioning
    plt.legend(loc='lower left', bbox_to_anchor=(.5,.5))
    plt.legend(loc='upper left', bbox_to_anchor=(1,1))
    plt.xticks(list(range(0, len(Seasons))), Seasons, rotation = 'vertical')




# ----  Visualize 1  ----
# Visualize 'FreeThrows'
myPlot(FreeThrows)

# Visualize 'FreeThrowAttempts'
myPlot(FreeThrowAttempts)




# ----  Visualize 2 : Free Throw Attempts per Games  ----
# --------    Games (Matrix Data)     --------
KobeBryant_G = [80,77,82,82,73,82,58,78,6,35]
JoeJohnson_G = [82,57,82,79,76,72,60,72,79,80]
LeBronJames_G = [79,78,75,81,76,79,62,76,77,69]
CarmeloAnthony_G = [80,65,77,66,69,77,55,67,77,40]
DwightHoward_G = [82,82,82,79,82,78,54,76,71,41]
ChrisBosh_G = [70,69,67,77,70,77,57,74,79,44]
ChrisPaul_G = [78,64,80,78,45,80,60,70,62,82]
KevinDurant_G = [35,35,80,74,82,78,66,81,81,27]
DerrickRose_G = [40,40,40,81,78,81,39,0,10,51]
DwayneWade_G = [75,51,51,79,77,76,49,69,54,62]
# Matrix
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G, KevinDurant_G, DerrickRose_G, DwayneWade_G])

# Visualize 'FreeThrowAttempts / Games'
    # Notice how Chris Paul gets few attempts per game
myPlot(FreeThrowAttempts/Games)




# ----  Visualize 3 : Free Throw Accuracy  ----
# Visualize 'Free Throw Accuracy = FreeThrows / FreeThrowAttempts'
    # And yet Chris Paul's accuracy is one of the highest Chances are his team would get more points if he had more FTA's.
    # Also notice that Dwight Howard's FT Accuracy is extremely poor compared to other players. If you recall, Dwight Howard's Field Goal Accuracy was exceptional:
myPlot(FreeThrows/FreeThrowAttempts)




# ----  Visualize 4 : Field Goal Accuracy  ----
# --------    FieldGoals (Matrix Data)    --------
KobeBryant_FG = [978,813,775,800,716,740,574,738,31,266]
JoeJohnson_FG = [632,536,647,620,635,514,423,445,462,446]
LeBronJames_FG = [875,772,794,789,768,758,621,765,767,624]
CarmeloAnthony_FG = [756,691,728,535,688,684,441,669,743,358]
DwightHoward_FG = [468,526,583,560,510,619,416,470,473,251]
ChrisBosh_FG = [549,543,507,615,600,524,393,485,492,343]
ChrisPaul_FG = [407,381,630,631,314,430,425,412,406,568]
KevinDurant_FG = [306,306,587,661,794,711,643,731,849,238]
DerrickRose_FG = [208,208,208,574,672,711,302,0,58,338]
DwayneWade_FG = [699,472,439,854,719,692,416,569,415,509]
# Matrix
FieldGoals  = np.array([KobeBryant_FG, JoeJohnson_FG, LeBronJames_FG, CarmeloAnthony_FG, DwightHoward_FG, ChrisBosh_FG, ChrisPaul_FG, KevinDurant_FG, DerrickRose_FG, DwayneWade_FG])

# --------    FieldGoalattempts (Matrix Data)    --------
KobeBryant_FGA = [2173,1757,1690,1712,1569,1639,1336,1595,73,713]
JoeJohnson_FGA = [1395,1139,1497,1420,1386,1161,931,1052,1018,1025]
LeBronJames_FGA = [1823,1621,1642,1613,1528,1485,1169,1354,1353,1279]
CarmeloAnthony_FGA = [1572,1453,1481,1207,1502,1503,1025,1489,1643,806]
DwightHoward_FGA = [881,873,974,979,834,1044,726,813,800,423]
ChrisBosh_FGA = [1087,1094,1027,1263,1158,1056,807,907,953,745]
ChrisPaul_FGA = [947,871,1291,1255,637,928,890,856,870,1170]
KevinDurant_FGA = [647,647,1366,1390,1668,1538,1297,1433,1688,467]
DerrickRose_FGA = [436,436,436,1208,1373,1597,695,0,164,835]
DwayneWade_FGA = [1413,962,937,1739,1511,1384,837,1093,761,1084]
# Matrix
FieldGoalAttempts = np.array([KobeBryant_FGA, JoeJohnson_FGA, LeBronJames_FGA, CarmeloAnthony_FGA, DwightHoward_FGA, ChrisBosh_FGA, ChrisPaul_FGA, KevinDurant_FGA, DerrickRose_FGA, DwayneWade_FGA])

# Visualize 'Field Goal Accuracy = FieldGoals / FieldGoalattempts'
    # How could this be? Why is there such a drastic difference?
    # We will see just now...
myPlot(FieldGoals/FieldGoalAttempts)




# ----  Visualize 5 : Points excluding FreeThrows  ----

# --------    Points (Matrix Data)    --------
KobeBryant_PTS = [2832,2430,2323,2201,1970,2078,1616,2133,83,782]
JoeJohnson_PTS = [1653,1426,1779,1688,1619,1312,1129,1170,1245,1154]
LeBronJames_PTS = [2478,2132,2250,2304,2258,2111,1683,2036,2089,1743]
CarmeloAnthony_PTS = [2122,1881,1978,1504,1943,1970,1245,1920,2112,966]
DwightHoward_PTS = [1292,1443,1695,1624,1503,1784,1113,1296,1297,646]
ChrisBosh_PTS = [1572,1561,1496,1746,1678,1438,1025,1232,1281,928]
ChrisPaul_PTS = [1258,1104,1684,1781,841,1268,1189,1186,1185,1564]
KevinDurant_PTS = [903,903,1624,1871,2472,2161,1850,2280,2593,686]
DerrickRose_PTS = [597,597,597,1361,1619,2026,852,0,159,904]
DwayneWade_PTS = [2040,1397,1254,2386,2045,1941,1082,1463,1028,1331]
# Matrix
Points = np.array([KobeBryant_PTS, JoeJohnson_PTS, LeBronJames_PTS, CarmeloAnthony_PTS, DwightHoward_PTS, ChrisBosh_PTS, ChrisPaul_PTS, KevinDurant_PTS, DerrickRose_PTS, DwayneWade_PTS])             

# ---  Vizualizing Player Style  ---
# we plot the 'Points' per 'FieldGoals', there are 3-point and 2-point styles
myPlot(Points/FieldGoals)
# BUT some of our data is above 3-points, because there are 'FreeThrows'
# We notice that the player-style of some player is changing
    # Eg: 'KevinDurant', at the beginniong he used 2-point-goal but later he changed to 3-point-goal
    # also notice the chanhe of 'KobeBryant' and 'ChrisBosh'

# ---  Vizualizing Player Style (without FreeThrows)  ---
# Visualize Player Style Patterns Excluding Free Throws '(Points - FreeThrows)/FieldGoals'
myPlot((Points - FreeThrows)/FieldGoals)



""" 
Because we have excluded free throws, this plot now shows us 
the true representation of player style change. We can verify
that this is the case because all the marks without exception
on this plot are between 2 and 3. That is because Field Goals
can only be for either 2 points or 3 points.

Insights:
1. You can see how players' preference for 2 or 3 point shots
   changes throughout their career. We can see that almost all
   players in this dataset experiment with their style throughout
   their careers. Perhaps, the most drastic change in style has
   been experienced by Joe Johnson.

2. There is one exception. You can see that one player has not
   changed his style at all - almost always scoring only 2-pointers.
   Who is this mystert player? It's Dwight Howard! 
   Now that explains a lot. The reason that Dwight Howard's
   Field Goal accuracy is so good is because he almost always
   scores 2-pointers only. That means he can be close to the basket
   or even in contact with it. Free throws, on the other hand require
   the player to stand 15ft (4.57m) away from the hoop. That's 
   probably why Dwight Howard's Free Throw Accuracy is poor.
 """
