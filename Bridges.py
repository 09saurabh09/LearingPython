#Script to store bridges up UP and MP
import urllib2
import xml.dom.minidom
import psycopg2
import math

conn = psycopg2.connect(database="Thesis", user="postgres", password="******",
host="127.0.0.1", port="5432")
print "Opened database successfully"


R=6384000
node_id=[]
row=[]
data=[]
ndid=[]

x=22
y=74
while(x<24):
    
    
    while(y<78):
        del ndid[0:len(ndid)]
        ndid=[]

        ln=str(x)
        lg=str(y)
        lnn=str(x+0.5)
        lgn=str(y+0.5)
        #url='http://api.openstreetmap.org/api/0.6/map?bbox=78.44,28.04,78.843,28.545'
        url='http://api.openstreetmap.org/api/0.6/map?bbox='+lg+','+ln+','+lgn+','+lnn
        #url='http://overpass.osm.rambler.ru/cgi/xapi?*[bbox=75.0818,22.061653,78.07396,26.5051908]'
        print url
        dom = xml.dom.minidom.parse(urllib2.urlopen(url))
        #dom = xml.dom.minidom.parse("bridge.osm")
        way=dom.getElementsByTagName('way')
        node=dom.getElementsByTagName('node')


        l= len(way)

        for i in range(l):
            tag=way[i].getElementsByTagName("tag")
            
            #print tag[0].attributes["k"].value
            
            if(len(tag)>0):
                
                if(tag[0].attributes["k"].value=="bridge"):
                    print "yes"
                    nd=way[i].getElementsByTagName("nd")
                    nl=len(nd)
                    brd_id=[]
                    #range is updated to 2 as we need only 2 point but this may cause error
                    for j in range(2):
                        brd_id.append(nd[j].attributes["ref"].value)

                    ndid.append(brd_id)

        n_brd=len(ndid)            

        n_node=len(node)
        del node_id[0:len(node_id)]
        node_id=[]

        for z in range(n_node):
            node_id.append(node[z].attributes["id"].value)

        for i in range(n_brd):
            
            p_brd=len(ndid[i])

           
            
            row=[]
            for j in range(p_brd):
                index=node_id.index(ndid[i][j])
                idd=node[index].attributes["id"].value
                lat=node[index].attributes["lat"].value
                lon=node[index].attributes["lon"].value
                row.append(int(idd))
                row.append(float(lat))
                row.append(float(lon))

            dlat= math.radians(row[1]-row[4])
            dlon= math.radians(row[2]-row[5])
            lat1= math.radians(row[1])
            lat2= math.radians(row[4])
            a= math.sin(dlat/2)*math.sin(dlat/2)+math.sin(dlon/2)*math.sin(dlon/2)*math.cos(lat1)*math.cos(lat2)
            c= 2*math.atan2(math.pow(a,0.5),math.pow((1-a),0.5))
            dist=R*c
            #X1= R * math.cos(row[1])*math.cos(row[2])
            #X2= R * math.cos(row[4])*math.cos(row[5])
            #Y1= R * math.cos(row[1])*math.sin(row[2])
            #Y2= R * math.cos(row[4])*math.sin(row[5])
            #Z1= R * math.sin(row[1])
            #Z2= R * math.sin(row[4])

            #sqd = math.pow((X2-X1),2)+math.pow((Y2-Y1),2)+math.pow((Z2-Z1),2)
            #dist = math.pow(sqd,0.5)

            row.append(dist)
            data.append(row)    

        y=y+0.5
    x=x+0.5    
         
length=len(data)

cur = conn.cursor()
kk = 1 

if ( kk == 0):
    
    cur.execute('''CREATE TABLE Bridges_UP
    (ID SERIAL PRIMARY KEY,
    OSM1_id BIGINT NOT NULL,
    LATITUDE FLOAT NOT NULL,
    LONGITUDE FLOAT NOT NULL,
    OSM2_ID BIGINT NOT NULL,
    LATITUDE1 FLOAT NOT NULL,
    LONGITUDE1 FLOAT NOT NULL,
    LENGTH FLOAT);''')
    print "Table created successfully"
    kk=kk+1

for i in range(length):
    
    cur.execute("INSERT INTO Bridges_UP (OSM1_id, LATITUDE, LONGITUDE, OSM2_ID, LATITUDE1, LONGITUDE1, LENGTH) VALUES (%s,%s,%s,%s,%s,%s,%s )",(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],))
    #To delete duplicate records
    cur.execute("DELETE FROM bridges_up WHERE id NOT IN (SELECT min(id) --or max(id) FROM bridges_upGROUP BY osm1_id)")
conn.commit()
conn.close()



        
        






