import psycopg2
import sys
import numpy as np
import csv 

conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

def ImportTable():
	query = '''
	DROP TABLE IF EXISTS public.housing;
	CREATE TABLE public.housing
	(
		"Id" int, 
		"MSSubClass" int, 
		"MSZoning" text, 
		"LotFrontage" text, 
		"LotArea" int, 
		"Street" text, 
		"Alley" text, 
		"LotShape" text, 
		"LandContour" text, 
		"Utilities" text, 
		"LotConfig" text, 
		"LandSlope" text, 
		"Neighborhood" text, 
		"Condition1" text, 
		"Condition2" text, 
		"BldgType" text, 
		"HouseStyle" text, 
		"OverallQual" int, 
		"OverallCond" int, 
		"YearBuilt" int, 
		"YearRemodAdd" int, 
		"RoofStyle" text, 
		"RoofMatl" text, 
		"Exterior1st" text, 
		"Exterior2nd" text, 
		"MasVnrType" text, 
		"MasVnrArea" text, 
		"ExterQual" text, 
		"ExterCond" text, 
		"Foundation" text, 
		"BsmtQual" text, 
		"BsmtCond" text, 
		"BsmtExposure" text, 
		"BsmtFinType1" text, 
		"BsmtFinSF1" int, 
		"BsmtFinType2" text, 
		"BsmtFinSF2" int, 
		"BsmtUnfSF" int, 
		"TotalBsmtSF" int, 
		"Heating" text, 
		"HeatingQC" text, 
		"CentralAir" text, 
		"Electrical" text, 
		"1stFlrSF" int, 
		"2ndFlrSF" int, 
		"LowQualFinSF" int, 
		"GrLivArea" int, 
		"BsmtFullBath" int, 
		"BsmtHalfBath" int, 
		"FullBath" int, 
		"HalfBath" int, 
		"BedroomAbvGr" int, 
		"KitchenAbvGr" int, 
		"KitchenQual" text, 
		"TotRmsAbvGrd" int, 
		"Functional" text, 
		"Fireplaces" int, 
		"FireplaceQu" text, 
		"GarageType" text, 
		"GarageYrBlt" text, 
		"GarageFinish" text, 
		"GarageCars" int, 
		"GarageArea" int, 
		"GarageQual" text, 
		"GarageCond" text, 
		"PavedDrive" text, 
		"WoodDeckSF" int, 
		"OpenPorchSF" int, 
		"EnclosedPorch" int, 
		"3SsnPorch" int, 
		"ScreenPorch" int, 
		"PoolArea" int, 
		"PoolQC" text, 
		"Fence" text, 
		"MiscFeature" text, 
		"MiscVal" int, 
		"MoSold" int, 
		"YrSold" int, 
		"SaleType" text, 
		"SaleCondition" text, 
		"SalePrice" int
	);'''

	cursor.execute(query)
	cursor.execute("COPY housing FROM '/home/alvin/Desktop/ecs163/proj2/data/housing_prices.csv' DELIMITER ',' CSV HEADER;")
	conn.commit()

# ImportTable()

years = [2006,2007,2008,2009,2010]
months = [x for x in range(1,13)]

f = csv.writer(open('data/heatmap.csv', 'w'), lineterminator='\n')
f.writerow(['YearSold','MonthSold','Count'])

for y in years:
	for m in months:
		query = 'SELECT COUNT(*) FROM housing WHERE "YrSold"=%s AND "MoSold"=%s' %(y,m)
		cursor.execute(query)
		# print '%s, %s: %s' %(s, str(b), cursor.fetchone()[0])		 
		f.writerow([y,m,cursor.fetchone()[0]])