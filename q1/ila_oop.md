# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation means bundling an item's data inside a class and restricting direct access to those variables by making them private. External code can only interact  or update these variables using certain methods. This makes the program organized by protecting data from invalid changes. For instance, a method can check and prevent a user from setting a negative quantity or accidentally changing a price directly.

### 2. Abstraction
Abstraction means hiding the complex inner workings and showing only the simple controls you actually need to use. This can help reduce confusion and increase effiency by only showing the necessary part the user needs to use. This makes the program organized by not showing unecessary mechanics and easy to read.

### 3. Inheritance
Inheritance means a child class automatically gets/inherits the properties and functions of a parent class. This improves code organization by eliminating redundant code, allowing us to define shared inventory behavior once while easily adding unique features for specific sari-sari store items.

### 4. Polymorphism
Polymorphism means giving the exact same command to different objects, and each object performs it in its own special way. This makes the system easier because the main inventory loop can simply call something like displayinfo() on a list containing all store items without needing long if-else statements to check the exact type of each item before giving the output.

Class Representation & Pseudocode Example

## Reflection
Among the four pillars of Object-Oriented Programming, Inheritance would be the most useful in improving the sari-sari store system. A sari-sari store has hundreds of different types of product, from canned goods and breads to beverages and  snacks. Instead of writing super long conditional "if-else" statements for every item type, Inheritance allows us to create a base item class with common properties like price and stock.