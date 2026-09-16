# Class Attributes and Methods
## Previous Design
Link to my previous activity: [classObjectUML.md](https://github.com/ntzenarosa-ui/9magnesiumcs3/blob/main/q1/classObjectUML.md)
## Design Revision
Describe any changes made to your original class.
No major changes were needed from my original design.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| name | string | + | Identifies the player and can be freely accessed for display. |
| JerseyNumber | int | + | Basic player identifier. |
| position | string | - | Position updates should be confirmed through methods rather than modified directly.  |
| isStarter | boolean | - | Lineup status affects team rotation, so it must be safely managed. |
## Updated UML Class Diagram
+---------------------------------------+     
|         VolleyballPlayer              |     
+---------------------------------------+     
| + name: String                        |     
| + jerseyNumber: Integer               |     
| - position: String                    |     
| - isStarter: Boolean                  |     
+---------------------------------------+     
| + get_position(): String              |     
| + set_starter_status(status: Boolean) |     
| + display_info()                      |     
+---------------------------------------+     
## Python Implementation [View Python Source](classImplementation.py)
## Test Run
![Test Run](https://github.com/ntzenarosa-ui/9magnesiumcs3/blob/main/q1/images/classTestRun.jpg)

## Object Diagram
+-----------------------------+      
| player1: VolleyballPlayer   |      
+-----------------------------+      
| name = "Alyssa"             |      
| jerseyNumber = 2            |      
| position = "Outside Hitter" |      
| isStarter = False           |      
+-----------------------------+      

+-----------------------------+      
| player2: VolleyballPlayer   |      
+-----------------------------+      
| name = "Jia"                |      
| jerseyNumber = 12           |      
| position = "Setter"         |      
| isStarter = True            |      
+-----------------------------+      

## Analysis
### Why did you make your chosen attribute private?
Position and isStarter are essential informations and should be private as it can significantly affect the teams performance. Additionally, it is private so the other won't know their strategy.

### Which method changes the state of your object?
set_starter_status(status: Boolean). It modifies the state of the _isStarter attribute from False to True and vice versa.

### How did your two objects demonstrate that instances are independent?
player1.set_starter_status(True) was called, only Alyssa's role updated from Substitute to Starter. Jia's (player2) attributes remained completely unchanged, showing that each object holds its own separate memory space and state.


### What is the difference between your class diagram and your object diagram?

The class diagram acts as the blueprint. It defines the structure like attributes and methods, data types (str, int, bool), and visibility (+ for public, - for private) without specific data values. While object diagram represents the actual instances created from that blueprint at a specific point in time, showing real values, for example: _name = "Alyssa", _jerseyNumber = 2.
