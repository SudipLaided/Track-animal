from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


import sqlite3


bot_left_lat  =28.25100
bot_left_lon  =83.97191
top_right_lat =28.25700
top_right_lon =83.98211

# create the map object, m
m = Basemap(resolution='i', projection='cyl', \
    llcrnrlon=bot_left_lon, llcrnrlat=bot_left_lat, \
    urcrnrlon=top_right_lon, urcrnrlat=top_right_lat)

# Note: You can define the resolution of the map you just created. Higher 
# resolutions take longer to create.
#    'c' - crude
#    'l' - low
#    'i' - intermediate
#    'h' - high
#    'f' - full

# Draw some map elements on the map
m.drawcoastlines()
m.drawstates()
m.drawcountries()
m.drawrivers(color='blue')

maps = ['ESRI_Imagery_World_2D',    # 0
        'ESRI_StreetMap_World_2D',  # 1
        'NatGeo_World_Map',         # 2
        'NGS_Topo_US_2D',           # 3
        'Ocean_Basemap',            # 4
        'USA_Topo_Maps',            # 5
        'World_Imagery',            # 6
        'World_Physical_Map',       # 7
        'World_Shaded_Relief',      # 8
        'World_Street_Map',         # 9
        'World_Terrain_Base',       # 10
        'World_Topo_Map'            # 11
        ]
print "drawing image from arcGIS server...",
m.arcgisimage(service=maps[6], xpixels=1000, verbose=False)
print "...finished"


conn = sqlite3.connect("dbs1.db")
cur = conn.cursor()
re = cur.execute("SELECT id FROM data where id = (select max(id) from data) ").fetchone()
mx = re[0]
print(mx)
cur.execute("select * from data ;")
results = cur.fetchall()

coords = cur.execute(""" select id, lon ,lat ,temp from data;""" \
                     ).fetchall()
idd  = [l[0] for l in coords]
lons = [l[1] for l in coords]
lats = [l[2] for l in coords]
temp = [l[3] for l in coords]

#m.plot(x, y, 'ro',markersize = 6, alpha =0.3)
def get_color(tmp):
    if tmp < 30.0:
        return ('b')
    elif tmp <= 39.0 and tmp>=30 :
        return ('y')
    else:
        return ('r')




# Plot a scatter point at WBB on the map object
#lon = [83.97493,83.97847]
#lat = [28.25281,28.25386]
for ide ,lon, lat, mag in zip(idd, lons, lats, temp): 
	x,y = (lon, lat)
	markerst = get_color(mag)
	if mx == ide:
		print(ide)
		magg = 50*5
		
		
	else:
		print(ide)
		magg = 50
		
		
	m.scatter(x,y,c=markerst,s=magg,alpha=0.8,marker="*")



plt.xlabel('this is the longitudes ')
plt.ylabel('this is the latitude ')

plt.show()
