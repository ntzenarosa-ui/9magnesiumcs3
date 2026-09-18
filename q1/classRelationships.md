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
Multiplicity: Team 1 -> 0..* VolleyballPlayer    
Explanation: A team requires a list of players to compete, so it can contain multiple VolleyballPlayer objects or none (0..*). A player, in this scenario, belongs to exactly one specific team (1).
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
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
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?