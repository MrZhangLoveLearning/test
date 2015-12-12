#NCU Electric Crawling  API

----

#### using `flask` as the web frame and   `re`  to parse the html


###get api

- host : http://115.28.30.14:8000
- url  : /api/get/`buildingNum`
- buildingNum : the location of students' apartment
- return : {'balance': ..., 'currentUsed': ..., 'readTime': ...}
- balance : the left degree of electric
- currentUsed : the spending of electric nowadays
- readTime : the reading time of electric meter
- method : get 

###post api

- host : http://115.28.30.14:8000
- url  : /api/post/`buildingNum`
- buildingNum : the location of students' apartment
- return : {'balance': ..., 'currentUsed': ..., 'readTime': ...}
- balance : the left degree of electric
- currentUsed : the spending of electric nowadays
- readTime : the reading time of electric meter
- method : post 


