# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](https://github.com/ntzenarosa-ui/9magnesiumcs3/blob/main/q1/classObjectUML.md)      
[Part II - Class Attributes and Methods](https://github.com/ntzenarosa-ui/9magnesiumcs3/blob/main/q1/classAttributesMethods.md)
## Existing Class
Class: VolleyballPlayer     
Description: Represents an individual athlete in a volleyball team, tracking their personal detaild, court position, and performance statistics.
## New Related Class
Class: Team   
Description: It represents the entire volleyball team, including its name, coach, and roster of players.
## Association
Relationship: Team contains players   
Explanation: A team or a volleyball team is composed of many individual volleyball players, and a group of volleyball players forms a team.
## Multiplicity
Multiplicity: Team 1 --- 0..* VolleyballPlayer    
Explanation: A team requires a list of players to compete, so it can contain multiple VolleyballPlayer objects or none (0..*). A player, in this scenario, belongs to exactly one specific team (1).
## UML Class Relationship Diagram   

+------------------------------+    
|               Team           |    
+------------------------------+    
| + team_name : string         |    
| + coach_name : string        |    
| + roster : list<Player>      |    
+------------------------------+    
| + add_player(player : Player)|    
| + display_roster()           |    
+------------------------------+    
    1   
    |   
    | contains  
    |   
    0..*    
+------------------------------+    
|              Player          |    
+------------------------------+    
| + name : string              |    
| + jerseyNumber : int         |    
| - __position : string        |    
| - __isStarter : bool         |    
+------------------------------+    
| + get_position()             |    
| + set_starter_status(status) |    
| + display_info()             |    
+------------------------------+    
## Python Implementation
[View Python Source](https://github.com/ntzenarosa-ui/9magnesiumcs3/blob/main/q1/classRelationship.py)
## Test Run
![Relationship Test Run](https://github.com/ntzenarosa-ui/9magnesiumcs3/blob/main/q1/images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?   
Team contains players, that means that a team or a volleyball team is composed of many individual volleyball players, and a group of volleyball players forms a team.
### What multiplicity did you choose and why?   
Team 1 -> 0..* VolleyballPlayer, that means that a team requires a list of players to compete, so it can contain multiple VolleyballPlayer objects or none (0..*). A player, in this scenario, belongs to exactly.
### How did you implement the relationship in Python?
By adding a list attribute called self.roster inside the Team class __init__() method.
### Why did you store an object reference instead of copying its data?
To keep the data updated across the entire system. So if I change an attribute later like updating player 1's starter status using set_starter_status(), the Team object automatically sees the updated info. Storing the actual reference points directly to the original object in memory instead of keeping an outdated copy.
### If your relationship uses many, why is a list appropriate?
A list is appropriate because it can dynamically hold multiple object references in a single variable. Since a team can have many players, a list allows me to add new Player objects easily.