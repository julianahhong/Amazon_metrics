#Very liberal, very cons {VL, VC, C, L, M}
#column index for political interests 
#politics:
#VL: '6015759997983': 947
#VC: '6015762142783': 868
#C: '6015760532183': 2953
#L: '6015760027783': 5360
#M: 6015760036783': 3938
#race: 
#African American: 6018745176183
#Hispanic: 6003133212372
#Asian American 6021722613183

"""
Age: 
13-21
22-37
38-57
57-100
"""
import ast
import numpy as np
import csv
import pandas as pd

class Politics_Interests:
	def __init__(self):
		#None/['6015759997983']/None/None/13/21/None

		self.VL_AGE_1_COL = 2004
		self.L_AGE_1_COL = 3909
		self.VL_AGE_2_COL = 3687
		self.L_AGE_2_COL = 4950
		self.VL_AGE_3_COL = 4444
		self.L_AGE_3_COL = 1879
		self.VL_AGE_4_COL = 3705
		self.L_AGE_4_COL = 887
		self.VC_AGE_1_COL = 754
		self.C_AGE_1_COL = 190
		self.VC_AGE_2_COL = 4645
		self.C_AGE_2_COL = 807
		self.VC_AGE_3_COL = 5054
		self.C_AGE_3_COL = 3062
		self.VC_AGE_4_COL = 3631
		self.C_AGE_4_COL = 1466

		self.VL_COL = 947
		self.VC_COL = 868
		self.C_COL = 2953
		self.L_COL = 5360
		self.M_COL = 3938

		self.MALE_COL = 1449 #Gender [1]
		self.FEM_COL = 1525 #Gender [2]

		self.VL_MALE_COL = 2648
		self.VL_FEM_COL = 2456
		self.VC_MALE_COL = 3015
		self.VC_FEM_COL = 3492
		self.L_MALE_COL = 338
		self.L_FEM_COL = 3989
		self.C_MALE_COL = 3317
		self.C_FEM_COL = 2224

		self.VL_HISP_COL = 2021
		self.L_HISP_COL = 2540
		self.VL_AFR_AMER_COL = 2142
		self.L_AFR_AMER_COL = 1436
		self.VL_ASI_AMER_COL = 1194
		self.L_ASI_AMER_COL = 768
		self.VC_HISP_COL = 1051
		self.C_HISP_COL = 2408
		self.VC_AFR_AMER_COL = 937
		self.C_AFR_AMER_COL = 1188
		self.VC_ASI_AMER_COL = 1283
		self.C_ASI_AMER_COL = 3039

		self.ALL_COL = 1665
		self.processFile()

		#None/[]/None/None/13/21/None
		#None/None/None/None/None/None/

	def processFile(self):
		#income range/politics/gender/education statuses/min age/max age/race
		#race: 6018745176183: African American; 6003133212372: Hispanic; 6021722613183: Asian American
		#gender: [1], [2]
		#age: under 30/over 30

		# with open('FB_IxD_full.tsv') as csvDataFile:
		# 	csvReader = csv.reader(csvDataFile)
		# 	titles = list(next(csvReader))
		# 	ids = []
		# 	j = 0
		# 	for e in titles:
		# 		# e = e.replace('\t','')
		# 		index = e.find("\t" + self.LIB_MALE_LABEL + "\t")
		# 		if index != -1:
		# 			ids.append(e[index:])
		# 		j+=1
		# 	for i in ids:
		# 		print(i)
		# 		print(j)
				

		pd.options.display.max_rows = 6000

		pd.set_option('max_colwidth', 300)
		reader = csv.reader(open("FB_IxD_full.tsv", "rb"), delimiter="\t")
		titles = list(next(reader))
		df = pd.DataFrame(data = titles, columns=[1])
		df.to_csv('Titles.csv')


		reader = csv.reader(open("FB_IxD_full.tsv", "rb"), delimiter="\t")
		next(reader)
		pd.options.display.max_rows = 150
		#order is VC, C, M, L, VL
		df = pd.DataFrame(data = list(reader), columns=np.arange(5395))
		print(df[947])
		print(df[self.VL_COL])

		df = df.apply(pd.to_numeric,errors='ignore')
		# print(df[947])
		# print(df[self.VL_COL])
		df['L'] = df[self.VL_COL] + df[self.L_COL]
		df['C'] = df[self.VC_COL] + df[self.C_COL]
		df['MOD_LIB'] = df[self.L_COL]
		df['V_LIB'] = df[self.VL_COL]
		df['MOD'] = df[self.M_COL]
		df['MOD_C'] = df[self.C_COL]
		df['V_CON'] = df[self.VC_COL]
		# print(df['V_LIB'])
		df['VL_Proportions'] = df[self.VL_COL]/(df[self.VL_COL] + df[self.VC_COL])
		df['VC_Proportions'] = df[self.VC_COL]/(df[self.VL_COL] + df[self.VC_COL])

		df['L_M'] = df[self.VL_MALE_COL] + df[self.L_MALE_COL]
		df['C_M'] = df[self.VC_MALE_COL] + df[self.C_MALE_COL]
		df['L_F'] = df[self.VL_FEM_COL] + df[self.L_FEM_COL]
		df['C_F'] = df[self.VC_FEM_COL] + df[self.C_FEM_COL]

		#lib minority for asi-am, afr-amer, hisp
		df['L_N'] = df[self.VL_ASI_AMER_COL] + df[self.L_ASI_AMER_COL] + df[self.VL_AFR_AMER_COL] + df[self.L_AFR_AMER_COL] + df[self.VL_HISP_COL] + df[self.L_HISP_COL]
		df['C_N'] = df[self.VC_ASI_AMER_COL] + df[self.C_ASI_AMER_COL] + df[self.VC_AFR_AMER_COL] + df[self.C_AFR_AMER_COL] + df[self.VC_HISP_COL] + df[self.C_HISP_COL]
		df['L_W'] = (df['L']) - df['L_N']
		df['C_W'] = (df['C']) - df['C_N']

		df['VL_ASI_AMER'] = df[self.VL_ASI_AMER_COL]
		df['ML_ASI_AMER'] = df[self.L_ASI_AMER_COL]
		df['VL_HISP'] = df[self.VL_HISP_COL]
		df['ML_HISP'] = df[self.L_HISP_COL]
		df['VL_AFR'] = df[self.VL_AFR_AMER_COL]
		df['ML_AFR'] = df[self.L_AFR_AMER_COL]

		print('Min/ white')
		# print(df.loc[:, ['ML_ASI_AMER', 'ML_HISP','ML_AFR', 'M_LIB']])


		# print(df.loc[:, ['VL_ASI_AMER', 'L_ASI_AMER', 'VL_HISP', 'L_HISP','VL_AFR','L_AFR', 'LIB', 'V_LIB', 'L']])
		# #age
		# df['L_U_Age'] = df[self.VL_AGE_1_COL] + df[self.L_AGE_1_COL] + df[self.VL_AGE_2_COL] + df[self.L_AGE_2_COL]
		# df['L_O_Age'] = df[self.VL_AGE_3_COL] + df[self.L_AGE_3_COL]+ df[self.VL_AGE_4_COL] + df[self.L_AGE_4_COL]
		# df['C_U_Age'] = df[self.VC_AGE_1_COL] + df[self.C_AGE_1_COL] + df[self.VC_AGE_2_COL] + df[self.C_AGE_2_COL]
		# df['C_O_Age'] = df[self.VC_AGE_3_COL] + df[self.C_AGE_3_COL]+ df[self.VC_AGE_4_COL] + df[self.C_AGE_4_COL]


		# df['Male_Prop']  = df[self.MALE_COL]/(df[self.MALE_COL] + df[self.FEM_COL])
		# df['Fem_Prop'] = df[self.FEM_COL]/(df[self.MALE_COL] + df[self.FEM_COL])

		# df['Lib_Prop'] = (df[self.VL_COL] + df[self.L_COL])/ (df[self.VL_COL] + df[self.L_COL] + df[self.VC_COL] + df[self.C_COL])
		# df['Cons_Prop'] = (df[self.VC_COL] + df[self.C_COL])/(df[self.VL_COL] + df[self.L_COL] + df[self.VC_COL] + df[self.C_COL])


		# df['Minority_Prop'] = (df['L_N'] + df['C_N'])/ (df['L_N'] + df['C_N'] + df['L_W'] + df['C_W'])
		# df['White_Prop'] = (df['L_W'] + df['C_W'])/ (df['L_N'] + df['C_N'] + df['L_W'] + df['C_W'])

		# df['U_Age_Prop'] = (df['L_U_Age'] + df['C_U_Age']) / (df['C_O_Age'] + df['L_O_Age'] + df['L_U_Age'] + df['C_U_Age'])
		# df['O_Age_Prop'] = (df['L_O_Age'] + df['C_O_Age']) / (df['C_O_Age'] + df['L_O_Age'] + df['L_U_Age'] + df['C_U_Age'])

		# #sort for liberal
		# #print('VERY LIBERAL INTERESTS')
		df.sort_values(['VL_Proportions'], ascending=False,inplace=True)

		df1 = df.loc[:, ['V_LIB', 'MOD_LIB', 'MOD', 'MOD_C', 'V_CON']].head(100)
		df1.to_csv('5_categories_VL.csv', sep=',', encoding='utf-8')
		# #print(df.loc[:, [0, self.VC_COL, self.C_COL, self.M_COL, self.L_COL, self.VL_COL,'VL_Proportions']].head(100))
		# #print(df.loc[:, [0, 'L_M', 'C_M', 'L_F', 'C_F', 'L_N', 'C_N', 'VL_Proportions']].head(100))
		# df1 = df.loc[:, [0, 'L_U_Age', 'C_U_Age', 'L_O_Age', 'C_O_Age', 'L_F', 'C_F', 'L_M', 'C_M', 'L_N', 'C_N']].head(100)
		# #print(df1)

		# #print(df.loc[:, ['Male_Prop', 'Fem_Prop', 'Lib_Prop', 'Cons_Prop', 'Minority_Prop', 'White_Prop', 'U_Age_Prop', 'O_Age_Prop']].head(100))
		# df1.to_csv('LIBERAL_DEMOS.csv')

		# #print('VERY CONS INTERESTS')
		# # # #sort for cons
		df.sort_values(['VC_Proportions'], ascending=False,inplace=True)
		df2 = df.loc[:, ['V_LIB', 'MOD_LIB', 'MOD', 'MOD_C', 'V_CON']].head(100)
		df2.to_csv('5_categories_VC.csv', sep=',', encoding='utf-8')

		# # print(df.loc[:, [0, self.VC_COL, self.C_COL, self.M_COL, self.L_COL, self.VL_COL,'CL_Proportions']].head(100))
		# df2 = df.loc[:, [0, 'L_U_Age', 'C_U_Age', 'L_O_Age', 'C_O_Age', 'L_F', 'C_F', 'L_M', 'C_M', 'L_N', 'C_N']].head(100)
		# #print(df)
		# df2.to_csv('CONS_DEMOS.csv')

		#df.to_csv('FB_Demographics.csv', sep=',', encoding='utf-8')

		"""
		[["Interest Id", "VC", "C", "M", "L", "VL"], ['6015760532183', 100, 200, 300, 200, 100], ...]
		"""

		def findRaceCols(self):
			labels = {}
			#income range/politics/gender/education statuses/min age/max age/race

		#Very cons: '6015762142783'
		#Very lib: 6015759997983
		# pol_ids = ['6015762142783', '6015759997983', '6015760532183', '6015760036783', '6015760027783']

		# i = 0
		# for l in self.demo_labels:
		# 	if l == "None/['6015762142783']/None/None/None/None/None":
		# 		labels['6015762142783'] = i
		# 	elif l == "None/['6015759997983']/None/None/None/None/None":
		# 		labels['6015759997983'] = i
		# 	elif l == "None/['6015760532183']/None/None/None/None/None":
		# 		labels['6015760532183'] = i
		# 	elif l == "None/['6015760036783']/None/None/None/None/None":
		# 		labels['6015760036783'] = i
		# 	elif l == "None/['6015760027783']/None/None/None/None/None":
		# 		labels['6015760027783'] = i
		# 	i+=1

data = Politics_Interests()

