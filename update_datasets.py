import json
import os

def main():
    if not os.path.exists( "./text_to_insert.txt" ):
        raise Exception( "text_to_insert.txt not found" )
    
    jsonFile = None
    write_target = ""
    
    with open( "./text_to_insert.txt" , 'r' , encoding = 'utf-8' ) as rFile:
        while True:
            this_line = rFile.readline()
            if not this_line:
                break
            this_line = this_line[:-1]
            
            if this_line[:1].isdigit():
                if jsonFile is not None:
                    jsonFile.close()
                    jsonFile = open( write_target , 'w' , encoding = 'utf-8' )
                    print( f"writing to { write_target }..." )
                    json.dump( json_data , jsonFile , ensure_ascii = False , indent = 4 )
                    jsonFile.close()
                category = this_line[this_line.find( "**" )+2:this_line.find( ":" )].replace( " " , "-" ).lower()
                write_target = f"./datasets/{ category }_en.json"
                jsonFile = open( write_target , 'r' , encoding = 'utf-8' )
                json_data = json.load( jsonFile )
            else:
                if this_line != "":
                    json_data.append( this_line[this_line.find( "-" )+2:] )

        jsonFile.close()
        jsonFile = open( write_target , 'w' , encoding = 'utf-8' )
        print( f"writing to { write_target }..." )
        json.dump( json_data , jsonFile , ensure_ascii = True , indent = 4 )
        jsonFile.close()

if __name__ == "__main__":
    main()
