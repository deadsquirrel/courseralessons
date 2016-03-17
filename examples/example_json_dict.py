import json
data = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
    },
    "email" : {
       "hide" : "yes"
    }
  }'''

info = json.loads(data)
print 'Name:', info["name"]
print 'Hide:', info["email"]["hide"]


#midgardr(courseralessons:master)% python example_lesson_json.py 
#Name: Chuck
#Hide: yes
