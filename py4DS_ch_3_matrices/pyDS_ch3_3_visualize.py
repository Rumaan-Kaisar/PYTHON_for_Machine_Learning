
################# 4.6: 5:29
# copy:  
#        
#        
################# (18-nov-23 for 19-nov-23)

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

from cProfile import label
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



