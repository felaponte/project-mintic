{"filter":false,"title":"db.py","tooltip":"/database/db.py","undoManager":{"mark":48,"position":48,"stack":[[{"start":{"row":0,"column":0},"end":{"row":34,"column":35},"action":"insert","lines":["import pymysql","","db_host = 'instance-cym.cdyc0ucs6ghp.us-east-1.rds.amazonaws.com'","db_user = 'felaponte'","db_password = 'pandora0706'","db_database = 'db_cym'","db_table = 'users'","","def connectionSQL():","    try:","        connection_sql = pymysql.connect(","            host = db_host,","            user = db_user,","            password = db_password,","            database = db_database","        )","        print('succesfull connection to database')","        return connection_sql","    except:","        print('Error connecting to database')","        return None ","","def add_user(id, name, lastname, birthday):","    instruction_sql =  \"INSERT INTO \" + db_table + \" (id, name, lastname, birthday) Values (\"+id+\", '\"+name+\"', '\"+lastname+\"', '\"+birthday+\"')\" ","    connection_sql = connectionSQL()","    try:","        if connection_sql != None:","           cursor = connection_sql.cursor()","           cursor.execute(instruction_sql)","           connection_sql.commit()","           print(\"user added\")","        else:","            print('Error connecting to database')","    except:","        print(\"error creting user\")"],"id":1}],[{"start":{"row":2,"column":11},"end":{"row":2,"column":64},"action":"remove","lines":["instance-cym.cdyc0ucs6ghp.us-east-1.rds.amazonaws.com"],"id":2},{"start":{"row":2,"column":11},"end":{"row":2,"column":64},"action":"insert","lines":["instance-cym.cdyc0ucs6ghp.us-east-1.rds.amazonaws.com"]}],[{"start":{"row":2,"column":11},"end":{"row":2,"column":64},"action":"remove","lines":["instance-cym.cdyc0ucs6ghp.us-east-1.rds.amazonaws.com"],"id":3},{"start":{"row":2,"column":11},"end":{"row":2,"column":75},"action":"insert","lines":["instance-proyect-mintic.cdyc0ucs6ghp.us-east-1.rds.amazonaws.com"]}],[{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"remove","lines":["m"],"id":4},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"remove","lines":["y"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"remove","lines":["c"]}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["p"],"id":5},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["r"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["o"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["y"]}],[{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["_"],"id":6},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["m"]},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["i"]},{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"insert","lines":["n"]},{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"insert","lines":["t"]},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"insert","lines":["c"]},{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"insert","lines":["i"]}],[{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"remove","lines":["i"],"id":7},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"remove","lines":["c"]}],[{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"insert","lines":["i"],"id":8},{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"insert","lines":["c"]}],[{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"remove","lines":["c"],"id":9},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"remove","lines":["i"]},{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"remove","lines":["t"]},{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"remove","lines":["n"]},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"remove","lines":["i"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"remove","lines":["m"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"remove","lines":["_"]}],[{"start":{"row":22,"column":12},"end":{"row":22,"column":41},"action":"remove","lines":["(id, name, lastname, birthday"],"id":10},{"start":{"row":22,"column":12},"end":{"row":22,"column":71},"action":"insert","lines":["id, name, ownername, ownerlastname, birthday, animal, breed"]}],[{"start":{"row":23,"column":54},"end":{"row":23,"column":82},"action":"remove","lines":["id, name, lastname, birthday"],"id":11},{"start":{"row":23,"column":54},"end":{"row":23,"column":113},"action":"insert","lines":["id, name, ownername, ownerlastname, birthday, animal, breed"]}],[{"start":{"row":23,"column":142},"end":{"row":23,"column":143},"action":"insert","lines":[" "],"id":12}],[{"start":{"row":23,"column":143},"end":{"row":23,"column":144},"action":"insert","lines":["'"],"id":13}],[{"start":{"row":23,"column":144},"end":{"row":23,"column":145},"action":"insert","lines":["\""],"id":14}],[{"start":{"row":23,"column":145},"end":{"row":23,"column":146},"action":"insert","lines":["+"],"id":15},{"start":{"row":23,"column":146},"end":{"row":23,"column":147},"action":"insert","lines":["o"]},{"start":{"row":23,"column":147},"end":{"row":23,"column":148},"action":"insert","lines":["w"]},{"start":{"row":23,"column":148},"end":{"row":23,"column":149},"action":"insert","lines":["n"]},{"start":{"row":23,"column":149},"end":{"row":23,"column":150},"action":"insert","lines":["e"]},{"start":{"row":23,"column":150},"end":{"row":23,"column":151},"action":"insert","lines":["r"]}],[{"start":{"row":23,"column":151},"end":{"row":23,"column":152},"action":"insert","lines":["n"],"id":16},{"start":{"row":23,"column":152},"end":{"row":23,"column":153},"action":"insert","lines":["a"]},{"start":{"row":23,"column":153},"end":{"row":23,"column":154},"action":"insert","lines":["m"]},{"start":{"row":23,"column":154},"end":{"row":23,"column":155},"action":"insert","lines":["e"]},{"start":{"row":23,"column":155},"end":{"row":23,"column":156},"action":"insert","lines":["\""]}],[{"start":{"row":23,"column":155},"end":{"row":23,"column":156},"action":"remove","lines":["\""],"id":17}],[{"start":{"row":23,"column":155},"end":{"row":23,"column":156},"action":"insert","lines":["+"],"id":18}],[{"start":{"row":23,"column":156},"end":{"row":23,"column":158},"action":"insert","lines":["\"\""],"id":19}],[{"start":{"row":23,"column":157},"end":{"row":23,"column":158},"action":"insert","lines":["'"],"id":20},{"start":{"row":23,"column":158},"end":{"row":23,"column":159},"action":"insert","lines":["."]}],[{"start":{"row":23,"column":158},"end":{"row":23,"column":159},"action":"remove","lines":["."],"id":21}],[{"start":{"row":23,"column":158},"end":{"row":23,"column":159},"action":"insert","lines":[","],"id":22}],[{"start":{"row":23,"column":159},"end":{"row":23,"column":160},"action":"insert","lines":[" "],"id":23}],[{"start":{"row":23,"column":160},"end":{"row":23,"column":161},"action":"remove","lines":["\""],"id":24},{"start":{"row":23,"column":160},"end":{"row":23,"column":161},"action":"remove","lines":[" "]}],[{"start":{"row":23,"column":163},"end":{"row":23,"column":164},"action":"insert","lines":["o"],"id":25},{"start":{"row":23,"column":164},"end":{"row":23,"column":165},"action":"insert","lines":["w"]},{"start":{"row":23,"column":165},"end":{"row":23,"column":166},"action":"insert","lines":["n"]},{"start":{"row":23,"column":166},"end":{"row":23,"column":167},"action":"insert","lines":["e"]},{"start":{"row":23,"column":167},"end":{"row":23,"column":168},"action":"insert","lines":["r"]}],[{"start":{"row":23,"column":195},"end":{"row":23,"column":196},"action":"insert","lines":[","],"id":28}],[{"start":{"row":23,"column":196},"end":{"row":23,"column":197},"action":"insert","lines":[" "],"id":29},{"start":{"row":23,"column":197},"end":{"row":23,"column":198},"action":"insert","lines":["'"]}],[{"start":{"row":23,"column":198},"end":{"row":23,"column":199},"action":"insert","lines":["\""],"id":30}],[{"start":{"row":23,"column":199},"end":{"row":23,"column":200},"action":"insert","lines":["+"],"id":31},{"start":{"row":23,"column":200},"end":{"row":23,"column":201},"action":"insert","lines":["a"]},{"start":{"row":23,"column":201},"end":{"row":23,"column":202},"action":"insert","lines":["n"]},{"start":{"row":23,"column":202},"end":{"row":23,"column":203},"action":"insert","lines":["i"]}],[{"start":{"row":23,"column":203},"end":{"row":23,"column":204},"action":"insert","lines":["m"],"id":32},{"start":{"row":23,"column":204},"end":{"row":23,"column":205},"action":"insert","lines":["a"]},{"start":{"row":23,"column":205},"end":{"row":23,"column":206},"action":"insert","lines":["l"]}],[{"start":{"row":23,"column":206},"end":{"row":23,"column":207},"action":"insert","lines":["+"],"id":33}],[{"start":{"row":23,"column":207},"end":{"row":23,"column":209},"action":"insert","lines":["\"\""],"id":34}],[{"start":{"row":23,"column":208},"end":{"row":23,"column":209},"action":"insert","lines":["'"],"id":35}],[{"start":{"row":23,"column":209},"end":{"row":23,"column":210},"action":"insert","lines":[","],"id":36}],[{"start":{"row":23,"column":210},"end":{"row":23,"column":211},"action":"insert","lines":[" "],"id":37}],[{"start":{"row":23,"column":211},"end":{"row":23,"column":212},"action":"insert","lines":["'"],"id":38}],[{"start":{"row":23,"column":213},"end":{"row":23,"column":214},"action":"insert","lines":["b"],"id":39},{"start":{"row":23,"column":214},"end":{"row":23,"column":215},"action":"insert","lines":["r"]},{"start":{"row":23,"column":215},"end":{"row":23,"column":216},"action":"insert","lines":["e"]},{"start":{"row":23,"column":216},"end":{"row":23,"column":217},"action":"insert","lines":["e"]},{"start":{"row":23,"column":217},"end":{"row":23,"column":218},"action":"insert","lines":["d"]}],[{"start":{"row":23,"column":213},"end":{"row":23,"column":214},"action":"insert","lines":["+"],"id":40}],[{"start":{"row":23,"column":219},"end":{"row":23,"column":220},"action":"insert","lines":["+"],"id":41}],[{"start":{"row":23,"column":220},"end":{"row":23,"column":222},"action":"insert","lines":["\"\""],"id":42}],[{"start":{"row":23,"column":221},"end":{"row":23,"column":222},"action":"remove","lines":["\""],"id":43}],[{"start":{"row":23,"column":221},"end":{"row":23,"column":222},"action":"insert","lines":["'"],"id":44},{"start":{"row":23,"column":222},"end":{"row":23,"column":223},"action":"insert","lines":[","]}],[{"start":{"row":23,"column":222},"end":{"row":23,"column":223},"action":"remove","lines":[","],"id":45}],[{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":[" "],"id":46},{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["("]}],[{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"remove","lines":[" "],"id":47}],[{"start":{"row":23,"column":51},"end":{"row":23,"column":52},"action":"insert","lines":["\\"],"id":53}],[{"start":{"row":23,"column":52},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":54},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":77},"end":{"row":24,"column":78},"action":"insert","lines":["\\"],"id":55}],[{"start":{"row":24,"column":78},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":56},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":66.66666666666667,"scrollleft":0,"selection":{"start":{"row":21,"column":0},"end":{"row":21,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":4,"state":"start","mode":"ace/mode/python"}},"timestamp":1718741032040,"hash":"c7c730620e41c42a1c06577d4aa05a1955ed3440"}