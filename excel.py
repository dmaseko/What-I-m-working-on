import pandas as pd 
import tkinter as tk

#read data from the separate spreadsheet

data = pd.read_excel('estimatedRegistration.xlsx')
data1 = pd.read_excel('pipelineTesting.xlsx')

#create a variable to pull the specific columns

f = data1[['Domicile_Province', 'HMAT_ATRNY_NAME_X', 'HMLN_ACNT_N','ACNT_HOLDR_X',
     'APLCN_CHANL_X','HMLN_SOURC_M', 'LOAN_A', 'PROD_DESC_X','BULDG_LOAN_Y','Loan_Type', 'Sectional_Title_Ind', 'Balance_Amount',
'Tat', 'EDR', 'Development Name', 'Delay Reason', 'Other Comments']]

d = data[['Client Reference', 'ID78Reason', 'Estimated Date Of Registration']]


#rename account column
f = f.rename(columns = {'HMLN_ACNT_N' : 'Client Reference' })

#merge the two workbooks
final = pd.merge(f,d,on='Client Reference', how= 'outer')



if __name__ == "__main__":

#print(d)
#print(f)
	print(final)

	final.to_excel('test.xlsx')