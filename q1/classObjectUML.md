# SG4 - Understanding Classes and Objects
## Class Name
VolleyballPlayer

## Class Description
Represents an individual athlete in a volleyball team, tracking their personal detaild, court position, and performance statistics.

## Properties
| Property | Data Type | Description |
|---|---|---|
| name | string | The name of the volleyball player. |
| JerseyNumber | int | The official shirt number of the player. |
| position | string | The player's role on the court (e.g., Setter, Outside Hitter, Libero). |
| isStarter | boolean | Indicates if the player is part of the starting line-up or not. |

## Methods
| Method | Description |
|---|---|
| service | Simulates the player doing a serve to start a rally. |
| updatePosition | Changes the court position or rotation role of the player. |
| displayStats | Prints the match performance and information of the player. |

## Class Diagram

+------------------------------------------+
| Jersey Number |
+------------------------------------------+
| name: string |
| JerseyNumber: int |
| position: string |
| isStart |
+------------------------------------------+
| service() |
| updatePosition(position: string) |
| displayStats() |
+------------------------------------------+

## Design Explanation

### Why did you choose this class?
Managing player roles, rotations, and line-ups is a crucial job in sports systems, and making this makes an athlete's attributes makes tracking the team's statistics much easier.

### Which property is the most important? Why?
The position property, because a player's role determines their specific responsibilities on the court, such as setting, attacking, or defending.

### Which method is the most useful? Why?
The updatePosition method, because player positions and rotations often need to be adjusted during training or match-ups.
