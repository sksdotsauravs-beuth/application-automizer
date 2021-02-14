# application-automizer
A simple command line application that automates the online reservation of available rooms/apartments in \
[House of Nations](https://www.house-of-nations.de/) website.

![alt Application Artwork](images/aa-artwork.png)

Help can be found about how to use the tool using (after going to project root directory in shell):
```PowerShell
python app.py --help
```
![alt Application Artwork](images/output-help-command.png)

### 01. UML
The Unified Modeling Language is a set of notation elements that can be used to develop models for software systems. 
This concerns the analysis, design and in general the presentation and documentation of the software elements or the 
software behavior. I have used [PlantUML](https://plantuml.com/) to design the UML diagrams of my project. PlantUML 
uses simple and intuitive language to design the diagrams. The sources are stored in *.puml* files which I continue 
to update as I make changes in the project to reflect visually in diagrams. 

**Use Case Diagram**

Use Case Diagram presents the actors and their cases of application. I have depicted my project's use cases marking 
also the actors in my program. The source can be found in [plant-uml/use_case_diagram.puml](plant-uml/use_case_diagram.puml). 

![alt Use Case Diagram](images/use_case_diagram.svg)

**Activity Diagram**

Activity Diagram shows how the program works by using actions, transitions and branches. In this diagram I have tried 
to visualize the total actions flow of my program with important actions and the branches. The source can be found in 
[plant-uml/activity_diagram.puml](plant-uml/activity_diagram.puml).

![alt Activity Diagram](images/activity_diagram.svg)

**Class Diagram**

Class Diagram represents the classes of the respective programming language and their relationships. All the fields 
and functions that I defined in the classes for the project, the relationships, visibility and package structure can 
be visualized through this diagram. The source can be found in [plant-uml/class_diagram.puml](plant-uml/class_diagram.puml).

![alt Class Diagram](images/class_diagram.svg)

### Metrics (Code Quality)

[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/dashboard?id=sksdotsauravs-beuth_application-automizer)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=sksdotsauravs-beuth_application-automizer&metric=bugs)](https://sonarcloud.io/dashboard?id=sksdotsauravs-beuth_application-automizer) [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=sksdotsauravs-beuth_application-automizer&metric=code_smells)](https://sonarcloud.io/dashboard?id=sksdotsauravs-beuth_application-automizer) [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=sksdotsauravs-beuth_application-automizer&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=sksdotsauravs-beuth_application-automizer) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=sksdotsauravs-beuth_application-automizer&metric=alert_status)](https://sonarcloud.io/dashboard?id=sksdotsauravs-beuth_application-automizer)

