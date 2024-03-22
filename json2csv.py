#! /usr/bin/env python

import json
import csv
import sys

def flattenjson( b, delim ):
    val = {}
    for i in b.keys():
        if isinstance( b[i], dict ):
            get = flattenjson( b[i], delim )
            for j in get.keys():
                val[ i + delim + j ] = get[j]
        else:
            val[i] = b[i]

    return val

in_file = open(sys.argv[1])
input = json.load(in_file)
in_file.close()

fname = sys.argv[1] + '.csv'

#input = map( lambda x: x + "__" , input )
#input = flattenjson( input, "__" )
#input = map( lambda x: flattenjson( x, "__" ), input )

foo = []
for row in input:
 row = flattenjson(row, "__")
 foo.append(row) 

input = foo
columns = [ x for row in input for x in row.keys() ]
columns = list( set( columns ) )

with open( fname, 'w' ) as out_file:
    csv_w = csv.writer( out_file )
    csv_w.writerow( columns )

    for i_r in input:
        csv_w.writerow( map( lambda x: i_r.get( x, "" ), columns ) )

out_file.close()
