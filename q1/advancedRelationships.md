# Advanced Class Relationships
## Previous Activities
[classAttrib](https://github.com/ntzenarosa-ui/9magnesiumcs3/blob/main/q1/classAttributesMethods.md)    
[classRel](https://github.com/ntzenarosa-ui/9magnesiumcs3/blob/main/q1/classRelationships.md)
## Existing System Description:
This system represents a volleyball management setup consisting of a "Team" and individual "Player". In the previous activity, a " Team" maintained a 1 or more association with "Player" by storing them in a roster list.
## Inheritance Relationship   
Parent: Person   
Child: Player   
Explanation: A "Player" IS-A "Person". Every player naturally possesses personal traits such as a name and age, while also having some sports properties like a jersey number, court position, and starter status.   
## Inheritance UML

```text
+-----------------------------------+   
|              Person               |   
+-----------------------------------+   
| + name : string                   |   
| + age : int                       |   
+-----------------------------------+   
| + display_person_info()           |   
+-----------------------------------+   
                  ^
                  |
                  |  (IS-A / Inherits)                                        Parent
+-----------------------------------+
|              Player               |
+-----------------------------------+
| + jerseyNumber : int              |
| - __position : string             |
| - __isStarter : bool              |
+-----------------------------------+
| + get_position()                  |
| + set_starter_status(status)      |
| + display_info()                  |
+-----------------------------------+
```
## Composition/Aggregation

Relationship: Aggregation (Team HAS-A Player)   
Explanation: The Team class contains Player/s objects in its roster, but this is an Aggregation relationship. The Player objects exist independently of the team, so if a Team object is deleted, the Player instances still exist in memory.

## Advanced UML Diagram
![Advanced UML](https://github.com/ntzenarosa-ui/9magnesiumcs3/blob/main/q1/images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](images/advancedTestRun.png)
## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflections
### 1. Why did you choose your inheritance relationship?
I chose Person as the parent class and Player as the child class because a player is a type of person (Player IS-A Person). Inheriting from Person allows the Player class to adopt basic personal attributes while keeping somr specific sports details separated.

### 2. How did inheritance reduce duplicate code?
Inheritance reduced duplicate code by allowing the Player class to reuse general attributes like name and age directly from Person.s
### 3. Why is your HAS-A relationship Composition or Aggregation? 

My HAS-A relationship is Aggregation because Player objects is independent from the Team. If the Team object is removed or deleted, the individual Player objects continue to exist independently in memory.

### 4. What is the difference between Association from Part III and the advanced relationship you implemented?
Association in Part III was just a basic connection showing that Team stores and uses Player instances. In Part IV, I made Inheritance(Player IS-A Person) and defined the HAS-A connection as Aggregation based on object lifecycles. 

### 5. How does your design follow the DRY principle?
By centralizing shared personal attributes in the Person class instead of duplicating them.