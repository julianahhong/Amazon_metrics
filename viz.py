#Very liberal, very cons
#column index for political interests {'6015759997983': 947, '6015762142783': 868, '6015760532183': 2953, '6015760027783': 5360, '6015760036783': 3938}

import ast
import numpy as np
import csv
import pandas as pd

class Politics_Interests:
	def __init__(self):

		self.VL_COL = 947
		self.VC_COL = 868
		self.C_COL = 2953
		self.L_COL = 5360
		self.M_COL = 3938

		self.MALE_COL = 1449 #Gender [1]
		self.FEM_COL = 1525 #Gender [2]

		self.LIB_MALE_LABEL = "None/['6015759997983']/[1]/None/None/None/None"

		self.processFile()

		#None/None/[1]/None/None/None/None
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
		df = df.apply(pd.to_numeric,errors='ignore')


		df['VL_Proportions'] = df[self.VL_COL]/(df[self.VL_COL] + df[self.VC_COL])
		df['CL_Proportions'] = df[self.VC_COL]/(df[self.VL_COL] + df[self.VC_COL])

		#sort for liberal
		print('VERY LIBERAL INTERESTS')
		df.sort_values(['VL_Proportions'], ascending=False,inplace=True)
		#print(df.loc[:, [0, self.VC_COL, self.C_COL, self.M_COL, self.L_COL, self.VL_COL,'VL_Proportions']].head(100))
		print(df.loc[:, [0, self.VC_COL, self.VL_COL, self.MALE_COL, self.FEM_COL,'VL_Proportions']].head(100))

		print('VERY CONS INTERESTS')
		# # #sort for cons
		# df.sort_values(['CL_Proportions'], ascending=False,inplace=True)
		# print(df.loc[:, [0, self.VC_COL, self.C_COL, self.M_COL, self.L_COL, self.VL_COL,'CL_Proportions']].head(100))

		#df.to_csv('FB_Demographics.csv', sep=',', encoding='utf-8')

		"""
		[["Interest Id", "VC", "C", "M", "L", "VL"], ['6015760532183', 100, 200, 300, 200, 100], ...]
		"""
		def makeSpreadsheet(self):
			headers = ["Interest ID", "Interest Name", "VC", "C", "M", "L", "VL"]
			ids = self.liberal_rows
			ids.append(self.cons_rows)
			array = zip(ids)
			with open("updated_table.csv", 'wb') as myfile:
				wr = csv.writer(myfile)
				wr.writerow(headers)
				wr.writerow(array)

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

