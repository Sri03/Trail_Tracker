### Logic for making map:

* get location from phone every {interval}
  * if location is {margin} close to another node: combine nodes
  * else: make new node
* draw line from prev node to curr node
* update distance counter
* update adj list

### Logic for finding new path: 
* ask for starting location
* ask for total distance
* implement some type of graph search 

### things to add rn: 
* need to learn how to use database to store nodes

### future improvements:
* implement pyicloud library yourself, and use that
  * using your own crytography to send username/password
* implement own graph traversal algorithm 
