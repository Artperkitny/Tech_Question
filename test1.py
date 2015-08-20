
import json

def getQuarter(x):
	if x>0: 
		year = int(x[:4])
		month = int(x[5:7])
		quarter = ""
		if month<4:
			quarter = 1
		elif month<7:
			quarter = 2
		elif month<10:
			quarter = 3
		else:
			quarter = 4
		return str(quarter)+str(year)
	else: 
		return "null" 

def calcCost(source,listLeads,listLease):
	cost = []

	if source == "Apartment Guide":
		if listLeads>0:
			cost.append([495*3,(495*3)/listLeads])
		else:
			cost.append([495*3,(495*3)/1])
	elif source == "Resident Referral":
		if listLeads>0:
			cost.append([listLease*500,(listLease*500)/listLeads])
		else:
			cost.append([listLease*500,(listLease*500)/1])
	elif source == "Apartments.com":
		if listLeads>0:
			cost.append([listLease*295,(listLease*295)/listLeads])
		else:
			cost.append([listLease*295,(listLease*295)/1])
	else:
		cost.append([0,0])

	return cost

def test():
	jsonData = json.loads(open("guest_cards.json").read())
	data = []
	quarters = []
	sources = []
	for i in jsonData:
		dateSeen = i["first_seen"]
		marketingSource = i["marketing_source"]
		leaseSigned = i["lease_signed"]
		sources.append(marketingSource)
		data.append([getQuarter(dateSeen),getQuarter(leaseSigned),marketingSource])
		quarters.append(getQuarter(dateSeen))

	for x in set(quarters):
		quarter = x[0]
		year = x[1:]
		print "Q%s %s:" % (quarter,year)
		for source in set(sources):
			listLeads = 0
			listLease = 0
			for x2 in data:
				if x2[0]==x and x2[2]==source:
					listLeads+=1
				if x2[1]==x and x2[2]==source:
					listLease+=1

			cost = calcCost(source,listLeads,listLease) 
			print "%s - total leads: %d, signed leases: %d, total cost: $%d, avg cost per lead: $%d" % (source,listLeads,listLease,cost[0][0],cost[0][1])
		print "\n"
		
	


		



		




	


test()