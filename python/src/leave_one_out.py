#
# AUTO-GENERATED FILE. DO NOT EDIT
# CodeBuff 1.4.6 'Fri May 06 16:28:48 PDT 2016'
#
import matplotlib.pyplot as plt

java_dist = [4.7169812E-4, 0.009823889, 0.12066877, 0.027865317, 0.01860587, 0.019890131, 0.19616601, 0.009741731, 0.010863351, 0.08033514, 0.0018281536, 0.1814149, 0.044378698, 0.016532619, 0.051149, 0.0011129661, 0.0010976949, 0.030355593, 0.0059800665, 0.0069905003, 0.016758544, 0.147651, 0.17221382, 0.0042833607, 0.06533117, 7.5662043E-4, 0.0066193854, 0.0029644268, 0.0015841584, 0.020502307, 0.0020008003, 0.22231781, 0.036270823, 0.019587083, 0.008365019, 0.016022742, 0.0010116338, 0.13791044, 0.025106704, 0.028440667, 0.0031120332, 0.006274957, 0.0071138213, 9.3984965E-4, 4.6040516E-4, 0.04263655, 0.012590727, 0.0038828098, 5.3106743E-4, 8.1933633E-4, 0.046702947, 0.0022062878, 0.04665453, 0.04531127, 0.040865026, 0.011437909, 0.024615385, 0.040270075, 0.0029200956]
java_err = [0.0, 0.045657016, 0.17686425, 0.05303761, 0.027642276, 0.055841923, 0.051787015, 0.067729086, 0.11627907, 0.08095238, 0.01898734, 0.016393442, 0.22580644, 0.061068702, 0.12953368, 0.018867925, 0.015873017, 0.09090909, 0.02310231, 0.021791767, 0.032534245, 0.08978675, 0.05648478, 0.03773585, 0.056778442, 0.009345794, 0.046296295, 0.060240965, 0.015789473, 0.14925373, 0.01843318, 0.07540057, 0.1978022, 0.14925373, 0.036, 0.051372897, 0.009708738, 0.11896349, 0.046403714, 0.0375, 0.029411765, 0.05109489, 0.05376344, 0.009433962, 0.0, 0.041666668, 0.07008965, 0.036363635, 0.0, 0.0091743115, 0.037558686, 0.05263158, 0.03936494, 0.046153847, 0.03902439, 0.026894866, 0.024922118, 0.053097345, 0.08130081]
java8_dist = [4.7169812E-4, 0.015250804, 0.3180073, 0.019195763, 0.01860587, 0.026586216, 0.20859647, 0.009288627, 0.009163803, 0.06814288, 0.0018281536, 0.1814149, 0.03254438, 0.016517857, 0.06263899, 0.0011129661, 0.0010976949, 0.036860365, 0.0056459648, 0.0073463535, 0.015834076, 0.08202484, 0.16999164, 0.0039538713, 0.113877505, 7.5662043E-4, 0.0066193854, 0.0029644268, 0.001980198, 0.029456576, 0.0020008003, 0.21853815, 0.036270823, 0.028841112, 0.008365019, 0.031523418, 0.0010116338, 0.029928982, 0.03546627, 0.06767644, 0.0024204704, 0.005988024, 0.0071138213, 4.6992482E-4, 9.2081033E-4, 0.059488803, 0.040351637, 0.003529827, 5.3106743E-4, 8.1933633E-4, 0.05345315, 0.0022062878, 0.050153617, 0.03598634, 0.027293066, 0.011162537, 0.026666667, 0.013744876, 0.0018582427]
java8_err = [0.0, 0.043429844, 0.13193117, 0.051923078, 0.027642276, 0.050687287, 0.054864667, 0.06374502, 0.11627907, 0.06845537, 0.01898734, 0.016393442, 0.18478261, 0.061068702, 0.2010582, 0.018867925, 0.015873017, 0.1440678, 0.01980198, 0.024213076, 0.03259005, 0.074074075, 0.05435081, 0.031446543, 0.037786495, 0.009345794, 0.046296295, 0.060240965, 0.021052632, 0.19402985, 0.01843318, 0.06503299, 0.1923077, 0.19402985, 0.036, 0.053333335, 0.009708738, 0.10731132, 0.037037037, 0.025, 0.022058824, 0.048661802, 0.05376344, 0.0, 0.008474576, 0.026515152, 0.07334963, 0.036363635, 0.0, 0.0091743115, 0.03883495, 0.05263158, 0.037004787, 0.03897436, 0.036540803, 0.024449877, 0.037383176, 0.0372807, 0.048780486]
antlr_dist = [0.052896455, 0.10139211, 0.07959289, 0.03356345, 0.08396947, 0.10611605, 0.19760755, 0.124868356, 0.37931034, 0.16835722, 0.13942307, 0.02550091]
antlr_err = [0.11699271, 0.2316119, 0.1269559, 0.07600693, 0.16759777, 0.22465852, 0.25135136, 0.1725706, 0.42857143, 0.2172371, 0.41025642, 0.16101696]
sqlite_noisy_dist = [0.12526096, 0.17359285, 0.15837938, 0.10567823, 0.12290503, 0.23349437, 0.16381419, 0.056062583, 0.07368754, 0.20546266, 0.42246726, 0.18285714, 0.14087301, 0.16866566, 0.2931596, 0.37995824, 0.11001317, 0.098996945, 0.08035931, 0.25959545, 0.14122137, 0.26227424, 0.13682432, 0.1995114, 0.13027228, 0.09255898, 0.15476191, 0.14427313, 0.22183709, 0.19279854, 0.26659715, 0.29354048, 0.13705584, 0.1882219, 0.24772443, 0.41854495]
sqlite_noisy_err = [0.2948113, 0.19020173, 0.18629551, 0.17525773, 0.13043478, 0.15476191, 0.20689656, 0.22507122, 0.096296296, 0.110694185, 0.20238096, 0.18981482, 0.17883211, 0.30039525, 0.18881118, 0.1891892, 0.13513513, 0.124615386, 0.14540817, 0.20762712, 0.275, 0.077586204, 0.28795812, 0.26785713, 0.19322033, 0.17592593, 0.14092141, 0.20353982, 0.18316832, 0.22058824, 0.13793103, 0.20063694, 0.27479675, 0.1786543, 0.23489933, 0.16103896]
sqlite_dist = [0.13415655, 0.1614001, 0.08944954, 0.10557532, 0.051136363, 0.14839798, 0.13583139, 0.06731784, 0.10836857, 0.14498827, 0.29818437, 0.22536023, 0.045853, 0.063709676, 0.079766534, 0.17264791, 0.25191528, 0.105365224, 0.065593466, 0.195708, 0.14748785, 0.17460318, 0.02420701, 0.15830116, 0.1747159, 0.04639175, 0.1, 0.024242423, 0.12162162, 0.2425399, 0.22977114, 0.016393442, 0.07498087, 0.08328977, 0.23643349, 0.19242175]
sqlite_err = [0.20215054, 0.11956522, 0.095744684, 0.059322033, 0.02173913, 0.11904762, 0.12903225, 0.088932805, 0.11707317, 0.125, 0.09266409, 0.14814815, 0.074204944, 0.07224335, 0.06081081, 0.09615385, 0.13819095, 0.106351554, 0.07476635, 0.098787606, 0.0952381, 0.12357724, 0.04761905, 0.115384616, 0.125, 0.08695652, 0.114713214, 0.06818182, 0.13839285, 0.15039062, 0.1509121, 0.019607844, 0.0764526, 0.10973085, 0.14666666, 0.10617284]
tsql_noisy_dist = [0.1421747, 0.17591622, 0.1424954, 0.13808802, 0.06703911, 0.20933977, 0.19210526, 0.16527621, 0.21631964, 0.110548995, 0.099299066, 0.38618523, 0.13239247, 0.20014992, 0.257329, 0.22964509, 0.10869565, 0.15528324, 0.06919155, 0.26669955, 0.1259542, 0.3545552, 0.1402027, 0.29800308, 0.14542651, 0.08029197, 0.085073866, 0.1587473, 0.13061224, 0.23245214, 0.1719057, 0.19273984, 0.15014695, 0.09360854, 0.22220239, 0.16482583]
tsql_noisy_err = [0.25295508, 0.2464986, 0.164859, 0.15306123, 0.11111111, 0.18292683, 0.13636364, 0.18457301, 0.185559, 0.10099132, 0.26104417, 0.21004567, 0.18181819, 0.38247013, 0.20567375, 0.2147651, 0.15053764, 0.14592934, 0.117794484, 0.21877934, 0.2125, 0.07388316, 0.35911602, 0.2969697, 0.22789116, 0.1388889, 0.13720317, 0.18103448, 0.20588236, 0.21338913, 0.084048025, 0.275, 0.27243066, 0.15837105, 0.21072437, 0.15064935]
tsql_dist = [0.14629552, 0.04191033, 0.07594292, 0.107947804, 0.051136363, 0.11804385, 0.09558824, 0.054910243, 0.11210542, 0.1361884, 0.39315644, 0.1037464, 0.12970169, 0.06612903, 0.06225681, 0.109602325, 0.3328877, 0.092254885, 0.043488707, 0.14899005, 0.13452189, 0.14550264, 0.030603806, 0.17374517, 0.12231183, 0.04639175, 0.056470588, 0.012269938, 0.14742193, 0.23178348, 0.1169579, 0.089171976, 0.18736278, 0.06695279, 0.10453018, 0.2092257]
tsql_err = [0.14529915, 0.069518715, 0.08993576, 0.016806724, 0.02173913, 0.11764706, 0.10638298, 0.06903353, 0.11048951, 0.10578035, 0.0996016, 0.09016393, 0.08214286, 0.14068441, 0.053691275, 0.07594936, 0.13, 0.107669614, 0.06880734, 0.07622914, 0.071428575, 0.110032365, 0.14285715, 0.1160221, 0.13084112, 0.07826087, 0.07506053, 0.022727273, 0.13839285, 0.1492248, 0.0513245, 0.14739884, 0.078461535, 0.0739615, 0.13532513, 0.13333334]

language_data = [antlr_dist, antlr_err, java8_dist, java8_err, java_dist, java_err, sqlite_dist, sqlite_err, sqlite_noisy_dist, sqlite_noisy_err, tsql_dist, tsql_err, tsql_noisy_dist, tsql_noisy_err]
labels = ["antlr\nn=12", "antlr_err\nn=12", "java8\nn=59", "java8_err\nn=59", "java\nn=59", "java_err\nn=59", "sqlite\nn=36", "sqlite_err\nn=36", "sqlite_noisy\nn=36", "sqlite_noisy_err\nn=36", "tsql\nn=36", "tsql_err\nn=36", "tsql_noisy\nn=36", "tsql_noisy_err\nn=36"]
fig = plt.figure()
ax = plt.subplot(111)
ax.boxplot(language_data,
           whis=[10, 90], # 10 and 90 % whiskers
           widths=.35,
           labels=labels)
ax.set_xticklabels(labels, rotation=60, fontsize=8)
plt.xticks(range(1,len(labels)+1), labels, rotation=60)
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_xlabel("Grammar and corpus size")
ax.set_ylabel("Edit distance / size of file")
ax.set_title("Leave-one-out Validation Using Edit Distance / Error Rate\nBetween Formatted and Original File")
plt.tight_layout()
fig.savefig('images/leave_one_out.pdf', format='pdf')
plt.show()
