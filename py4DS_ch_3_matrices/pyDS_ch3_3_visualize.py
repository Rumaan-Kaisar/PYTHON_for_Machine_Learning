
# Courses: A-Z PY for Data-Science    4.6, 4.7


# -------    Visualization    -------
# we can't get much more insights by looking at just numbers
    # Thats why we need "Visual-Representation of Data/Result"

# Objective: 
    # Transform Tables of data into plots
    # Findout: Anomalies, Trends



# ----    Data    ----

# Salaries
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
#Matrix
Salary = np.array([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary, ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])



# ---------------------    MATPLOTLIB    ---------------------
# download the package 'matplotlib' if not available

import numpy as np
import matplotlib.pyplot as plt

# to display the plots inside "ipynb" file (otherwise it'll display in seperate window) use following
%matplotlib inline

# Create "salary" plot
# it plots each list as a '2D-line'
plt.plot(Salary)    # notice the Matrix-argument

# Create "first-row of salary" plot
plt.plot(Salary[0])    # notice the Matrix-argument with index
print(Salary[0])



# --------    plot STYLES & COLOR    --------
# ls : line-style,      c : color, marker = 's'   s-square, ms : marker-size
plt.plot(Salary[0], ls='--', c='Black', marker = 's', ms=17)

# Size of the figure, (there is also other ways)
plt.rcParams['figure.figsize'] = 8, 4   # note: a space is needed between the values

# Notice: [<matplotlib.lines.Line2D at 0x1dbfea6b7c0>], we're printing object
# insterad we can use plt.show(), to avoid "[<matplotlib.lines.Line2D at 0x1dbfea6b7c0>]" message
plt.show()




# --------    Ticks: values to display in X-axis in Y-axis    --------
# pick elements from a list
list_of_chars = ['a','b','c','d','e','f','g','h','i','j', 'k', 'l', 'm', 'n']

plt.plot(Salary[0], ls='--', c='Black', marker = 's', ms=17)
plt.rcParams['figure.figsize'] = 8, 4

plt.xticks(list(range(0, len(list_of_chars))), list_of_chars, rotation = 'vertical')
# Notice: Two lists are used (both need to be same size)
    # rotation applied to 'Ticks'
# Tow list must be same size: The number of FixedLocator locations (12), usually from a call to set_ticks, does not match the number of ticklabels (13)

plt.show()


# LABEL
plt.plot(Salary[0], ls=':', c='Red', marker = 's', ms=7, label = "Twinkle")

# different list styles: supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'




# ----------------    More Visualization    ----------------
# read more on "matplotlib - Documnetation"
    # different line-styles
    # different markers
import numpy as np
import matplotlib.pyplot as plt


%matplotlib inline
plt.rcParams['figure.figsize'] = 8, 4

# Salaries
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
#Matrix
Salary = np.array([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary, ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])

Seasons = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]

plt.plot(Salary[0], ls='--', c='Black', marker = 's', ms=7, label = "Twinkle")
plt.plot(Salary[1], ls=':', c='Red', marker = 'o', ms=7, label = "Twinkle")

plt.xticks(list(range(0, len(Seasons))), Seasons, rotation = 'vertical')
plt.show()



# --------    Legend    --------
Players = ["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"]

plt.plot(Salary[0], ls='--', c='Black', marker = 's', ms=7, label = Players[0])
plt.plot(Salary[1], ls=':', c='Red', marker = 'o', ms=7, label = Players[1])
plt.plot(Salary[2], ls='-', c='Green', marker = '^', ms=7, label = Players[2])
plt.plot(Salary[3], ls='-.', c='Cyan', marker = 'D', ms=7, label = Players[3])

# legend
# plt.legend()   # also works 
# loc : selects a corner of "legend-box"
# bbox_to_anchor : coordinate to move the "legend-box" relative to figure
    # ranges 0 to 1, "full length of an axis = 1"
    # (0,0) : origin, (1,1) : upper right
plt.legend(loc='lower left', bbox_to_anchor=(.5,.5))
plt.legend(loc='upper left', bbox_to_anchor=(1,1))

plt.xticks(list(range(0, len(Seasons))), Seasons, rotation = 'vertical')
plt.show()



# --------    Games : Visualize    -------- 
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
#Matrix
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G, KevinDurant_G, DerrickRose_G, DwayneWade_G])


plt.plot(Games[0], ls='--', c='Black', marker = 's', ms=7, label = Players[0])
plt.plot(Games[1], ls=':', c='Red', marker = 'o', ms=7, label = Players[1])
plt.plot(Games[2], ls='-', c='Green', marker = '^', ms=7, label = Players[2])
plt.plot(Games[3], ls='-.', c='Cyan', marker = 'D', ms=7, label = Players[3])

plt.legend(loc='lower left', bbox_to_anchor=(.5,.5))
plt.legend(loc='upper left', bbox_to_anchor=(1,1))

plt.xticks(list(range(0, len(Seasons))), Seasons, rotation = 'vertical')
plt.show()
