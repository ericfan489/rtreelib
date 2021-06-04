from rtreelib import RStarTree, Rect
from unittest import TestCase
from rtreelib.diagram import create_rtree_diagram
import psycopg2


class Test_friction(TestCase):

    def test_10_points(self):
        params = {  
        'dbname': 'nsf_roadtraffic_friction_v2',
        'user': 'efan',
        'password': '26May2021',
        'host': '10.91.224.230',
        'port': 5432
        }
        try:
            conn = psycopg2.connect(**params)
            cursor = conn.cursor()
            #cursor.execute('SELECT contact_point_east, contact_point_north, friction_measurement_noisy FROM tmp_page_caches FETCH FIRST 10 ROWS ONLY')
            cursor.execute('SELECT contact_point_east, contact_point_north, friction_measurement_noisy FROM tmp_page_caches LIMIT 10')
            data = list(cursor.fetchall())
            conn.close()
        except:
            print( "I am unable to connect to the database")
        
        print('We have {} columns'.format(len(data)))
        t = RStarTree(max_entries = 4,min_entries = 2)
        for x in data:
            t.insert(x[2],Rect(x[0],x[1],x[0],x[1]))
        create_rtree_diagram(t)
    
        

    def test_1000_points(self):
        params = {  
        'dbname': 'nsf_roadtraffic_friction_v2',
        'user': 'efan',
        'password': '26May2021',
        'host': '10.91.224.230',
        'port': 5432
        }
        try:
            conn = psycopg2.connect(**params)
            cursor = conn.cursor()
            #cursor.execute('SELECT contact_point_east, contact_point_north, friction_measurement_noisy FROM tmp_page_caches FETCH FIRST 1000 ROWS ONLY')
            cursor.execute('SELECT contact_point_east, contact_point_north, friction_measurement_noisy FROM tmp_page_caches LIMIT 60')
            data = list(cursor.fetchall())
            conn.close()
        except:
            print( "I am unable to connect to the database")

        print('We have {} columns'.format(len(data)))
        t = RStarTree(max_entries = 4,min_entries = 2)
        for x in data:
            t.insert(x[2],Rect(x[0],x[1],x[0],x[1]))
        #create_rtree_diagram(t)

    #def test_all_points(self):
        #params = {  
        #'dbname': 'nsf_roadtraffic_friction_v2',
        #'user': 'efan',
        #'password': '26May2021',
        #'host': '10.91.224.230',
        #'port': 5432
        #}
        #try:
            #conn = psycopg2.connect(**params)
            #cursor = conn.cursor()
            #cursor.execute('SELECT contact_point_east, contact_point_north, friction_measurement_noisy FROM tmp_page_caches')
            #data = list(cursor.fetchall())
            #print('We have {} columns'.format(len(data)))
            #t = RStarTree(max_entries = 4,min_entries = 2)
            #print(type(data[0][2]))
            #for x in data:
                #t.insert(x[2],Rect(x[0],x[1],x[0],x[1]))
            #nodes = t.get_nodes()
            #for y in nodes:
                #print(y.lin_sum)
            #create_rtree_diagram(t)
            #except:
        #print( "I am unable to connect to the database")

