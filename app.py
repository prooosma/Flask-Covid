from flask import Flask, render_template, request, url_for, session
import requests
import pandas as pd
import folium

#########################Functions for Charts and WorldMap#########################
	


#########################Functions for Charts and WorldMap#########################

app = Flask(__name__)

country = 'Morocco'

@app.route("/", methods=['GET', 'POST'])
@app.route("/covid", methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		global country
		new_country = request.form.get('country')
		country = new_country


	url = "https://coronavirus-19-api.herokuapp.com/countries/{}"

	
	r = requests.get(url.format(country)).json()
	# print(r)
	covid = {
				'country': country.upper(),
				'confirmed': r['cases'],
				'recovered': r['recovered'],
				'critical': r['critical'],
				'deaths': r['deaths'],
				'todayCases': r['todayCases'],
				'todayDeaths': r['todayDeaths'],
				'active': r['active'],
				'totalTests': r['totalTests'],
			}
	

	url = "https://coronavirus-19-api.herokuapp.com/countries"

	response = requests.get(url).json()
	data = []

	for line in response:
		tmp = {}
		tmp['country'] = line['country']
		tmp['confirmed'] = line['cases']
		data.append(tmp)

	

	
	corona_map = pd.read_csv('https://raw.githubusercontent.com/prooosma/Covid-tracker-Flask/master/New_Data.csv')

	def top_confirmed( n = 14):
		
		by_country = corona_map.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
		byConf = by_country.nlargest(n, 'Confirmed')[['Confirmed']]

		return byConf



	corona_map.head()

	worldMap = folium.Map(width=895, height=536, location = [31.7917 , -7.0926 ], tiles = 'cartodbdark_matter', zoom_start = 4)

	# folium.Circle(location = [ 31.7917 , -7.0926 ], radius = 100*1000, color = 'yellow', fill = True, popup='Confirmed: {}'.format(20)).add_to(worldMap)

	def map_marker(x):
		folium.Circle(location= [x[0], x[1]],
		radius = float(x[2]*3),
		color = 'red', fill = True, 
		popup = '{} \n Confirmed: {}'.format(x[3] ,x[2])).add_to(worldMap)

	corona_map["Lat"].fillna(0, inplace = True) 
	corona_map["Long_"].fillna(0, inplace = True) 
	corona_map["Confirmed"].fillna(0, inplace = True) 
	corona_map["Combined_Key"].fillna("None", inplace = True)


	corona_map[['Lat', 'Long_', 'Confirmed', 'Combined_Key']].apply(lambda x: map_marker(x), axis  = 1)

	byConf = top_confirmed()#.to_html()
	html_map = worldMap._repr_html_()

	pairs = [(country, confirmed) for country, confirmed in zip(byConf.index, byConf['Confirmed'])]
	
	return render_template("index.html", covid=covid, data=data, byConf=byConf, wMap = html_map, pairs=pairs)



@app.route("/morocco")
def maroc():
	url = "https://opendata.arcgis.com/datasets/454f46db2cfd49fca37245541810d18b_0.geojson"

	answer = requests.get(url).json()
	
	
	daraa = {
		'Region': answer["features"][0]["properties"]["RegionFr"], 	
		'Cases': answer["features"][0]["properties"]["Cases"], 
		'Deaths': answer["features"][0]["properties"]["Deaths"],
		'Recovered': answer["features"][0]["properties"]["Recoveries"],

	 	}


	eddakhla = {
		'Region': answer["features"][1]["properties"]["RegionFr"], 	
		'Cases': answer["features"][1]["properties"]["Cases"], 
		'Deaths': answer["features"][1]["properties"]["Deaths"],
		'Recovered': answer["features"][1]["properties"]["Recoveries"],
	 	}

	guelmim = {
		'Region': answer["features"][2]["properties"]["RegionFr"], 	
		'Cases': answer["features"][2]["properties"]["Cases"], 
		'Deaths': answer["features"][2]["properties"]["Deaths"],
		'Recovered': answer["features"][2]["properties"]["Recoveries"],
	 	}

	laayoun = {
		'Region': answer["features"][3]["properties"]["RegionFr"], 	
		'Cases': answer["features"][3]["properties"]["Cases"], 
		'Deaths': answer["features"][3]["properties"]["Deaths"],
		'Recovered': answer["features"][3]["properties"]["Recoveries"],
	 	}

	bennimellal = {
		'Region': answer["features"][4]["properties"]["RegionFr"], 	
		'Cases': answer["features"][4]["properties"]["Cases"], 
		'Deaths': answer["features"][4]["properties"]["Deaths"],
		'Recovered': answer["features"][4]["properties"]["Recoveries"],
	 	}

	marrakech = {
		'Region': answer["features"][5]["properties"]["RegionFr"], 	
		'Cases': answer["features"][5]["properties"]["Cases"], 
		'Deaths': answer["features"][5]["properties"]["Deaths"],
		'Recovered': answer["features"][5]["properties"]["Recoveries"],
	 	}
	
	oriental = {
		'Region': answer["features"][6]["properties"]["RegionFr"], 	
		'Cases': answer["features"][6]["properties"]["Cases"], 
		'Deaths': answer["features"][6]["properties"]["Deaths"],
		'Recovered': answer["features"][6]["properties"]["Recoveries"],
	 	}

	rabat = {
		'Region': answer["features"][7]["properties"]["RegionFr"], 	
		'Cases': answer["features"][7]["properties"]["Cases"], 
		'Deaths': answer["features"][7]["properties"]["Deaths"],
		'Recovered': answer["features"][7]["properties"]["Recoveries"],
	 	}

	souss = {
		'Region': answer["features"][8]["properties"]["RegionFr"], 	
		'Cases': answer["features"][8]["properties"]["Cases"], 
		'Deaths': answer["features"][8]["properties"]["Deaths"],
		'Recovered': answer["features"][8]["properties"]["Recoveries"],
	 	}

	casablanca = {
		'Region': answer["features"][9]["properties"]["RegionFr"], 	
		'Cases': answer["features"][9]["properties"]["Cases"], 
		'Deaths': answer["features"][9]["properties"]["Deaths"],
		'Recovered': answer["features"][9]["properties"]["Recoveries"],
	 	}

	fes = {
		'Region': answer["features"][10]["properties"]["RegionFr"], 	
		'Cases': answer["features"][10]["properties"]["Cases"], 
		'Deaths': answer["features"][10]["properties"]["Deaths"],
		'Recovered': answer["features"][10]["properties"]["Recoveries"],
	 	}

	tanger = {
		'Region': answer["features"][11]["properties"]["RegionFr"], 	
		'Cases': answer["features"][11]["properties"]["Cases"], 
		'Deaths': answer["features"][11]["properties"]["Deaths"],
		'Recovered': answer["features"][11]["properties"]["Recoveries"],
	 	}
		 	 	 
		  

	

	return render_template("maroc.html", 
	daraa=daraa, 
	souss=souss, 
	casablanca=casablanca, 
	marrakech=marrakech,
	tanger=tanger,
	laayoun=laayoun,
	bennimellal=bennimellal,
	eddakhla=eddakhla,
	fes=fes,
	oriental=oriental,
	guelmim=guelmim,
	rabat=rabat)







@app.route("/protect")
def protect():
	return render_template("protect.html")



if __name__ == "__main__":
	app.run(debug=True)


