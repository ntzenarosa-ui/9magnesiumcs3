# Class Attributes and Methods
## Previous Design
Link to my previous activity:[classObjectUML.md](https://github.com/ntzenarosa-ui/9magnesiumcs3/blob/main/q1/classObjectUML.md)
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
+-------------------------------------------------+
|                    Player                       |
+-------------------------------------------------+
| + name: String                                  |
| + jerseyNumber: Integer                         |
| - position: String                              |
| - isStarter: Boolean                            |
+-------------------------------------------------+
| + get_position(): String                        |
| + set_starter_status(status: Boolean)           |
| + display_info()                                |
+-------------------------------------------------+
## Python Implementation [View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)

## Object Diagram
![Object Diagram](images/objectDiagram.png)

## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?