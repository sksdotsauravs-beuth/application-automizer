# application-automizer

### Table of Contents
*  [00. About Application](#about-application)
*  [01. UML](#uml)
*  [02. DDD](#ddd)
*  [03. Metrics](#metrics)
*  [04. Clean Code Development](#clean-code-development)
*  [05. Build Management](#build-management)
*  [06. Unit-Tests](#unit-tests)
*  [07. Continuous Delivery](#continuous-delivery)
*  [08. IDE](#ide)
*  [09. DSL](#dsl)
*  [10. Functional Programming](#functional-programming)

### <a name="about-application"></a>00. About Application

A simple command line application that automates the online reservation of available rooms/apartments in 
[House of Nations](https://www.house-of-nations.de/) website. I have used *Python* to develop the project and the 
required libraries are listed in [requirements.txt](requirements.txt). I have used selenium chrome webdriver for 
my project and this is only the external dependency. The latest chrome driver can be found [here](https://chromedriver.chromium.org/downloads).

![alt Application Artwork](images/aa-artwork.png)

Help can be found about how to use the tool using (after going to project root directory in shell):
```PowerShell
python app.py --help
```
![alt Application Artwork](images/output-help-command.png)

As it is a command line tool it is necessary to provide the configuration through the [config.yml](resource/config.yml).
```YAML
# set the log level to either "ERROR", "DEBUG" or "INFO"
# to set the precision of error messages
log_level: "INFO"

# set this property if you would only like to execute a dry run.
# If you don't want to submit the final form set this property to "yes".
# If you do not want to use dry run mode, just set this property to "no".
dry_run: "no"

# set this property to target driver executable path
driver_path: "C:\\Users\\saurav\\Downloads"

# set this property to target driver type
driver_type: "chrome"

# set this property to house_of_nations current Home Page url
hon_home_url: "https://www.house-of-nations.de/"

# set this property to start month tag
# valid options = ["Beginning of", "Middle of"]
step1.start_month_tag: "Middle of"

# set this property to start month
# valid options = [
#   "January", "February", "March", "April", "May", "June",
#   "July", "August", "September", "October", "November", "December"
# ]
step1.start_month: "March"

# set this property to start year
step1.start_year: "2021"

# set this property to end month tag
# valid options = ["End of", "Middle of"]
step1.end_month_tag: "Middle of"

# set this property to end month
# valid options similar as step1.start_month
step1.end_month: "January"

# set this property to end year
step1.end_year: "2022"

# set this property to preferred room choices separated by comma
# EZ  - Single Room
# EA  - Single Apartment
# EA2 - Single Apartment for 2 persons
# DA  - Double Apartment
# DAB - Double Apartment, handicapped accessible
# valid choices: "EZ,EA,EA2,DA,DAB"
step1.room_choices: "EZ,EA"
```   

### <a name="uml"></a>01. UML
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

### <a name="ddd"></a>02. DDD

#### Strategic Domain Design

1. **Configuration Management** to manage the configuration required to run the application. Reading config.yml file, 
parsing and validating, creating the value object to be passed around where this is required are some tasks in this 
strategic part.

2. **Executors** a core domain which is used to maintain the execution flow of the application. Command 
Line arguments parsing, creating main app instance, managing webdriver states and main actions in one place can be seen 
as parts of this domain.

3. **Pages** for managing page properties, components and functionalities of different webpages of the House of Nations 
website. This is also a core domain and specific to requirements of this particular application.

4. **Factories** for creating instance of configuration and webdriver. This is supporting domain.

5. **Validators** for validating inputs. This also falls in supporting domain.

6. **Utils** provides utility functions. This is a generic domain.

![alt Strategic Domain Design](images/strategic_domain_design.svg) 


### <a name="metrics"></a>03. Metrics

I have used SonarCloud and SonarLint plugin in my IDE to analyze and generate metrics of my project to get insights of 
code quality.

[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/dashboard?id=sksdotsauravs-beuth_application-automizer)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=sksdotsauravs-beuth_application-automizer&metric=bugs)](https://sonarcloud.io/dashboard?id=sksdotsauravs-beuth_application-automizer) [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=sksdotsauravs-beuth_application-automizer&metric=code_smells)](https://sonarcloud.io/dashboard?id=sksdotsauravs-beuth_application-automizer) [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=sksdotsauravs-beuth_application-automizer&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=sksdotsauravs-beuth_application-automizer) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=sksdotsauravs-beuth_application-automizer&metric=alert_status)](https://sonarcloud.io/dashboard?id=sksdotsauravs-beuth_application-automizer)

### <a name="clean-code-development"></a>04. Clean Code Development

The goal of clean code development is to develop sustainable code with good quality so that technical debts are minimal.

1. **Comments**: Useful comments to describe the tasks of functions and classes throughout the project by using docstring.

    [home_page.py](source/pages/house_of_nations/home_page.py)
    ```Python
    class HomePage(Page):
        """
            This class holds the information of home page, such as:
            it's url and other page elements.
        """
    ```
    ```Python
        def at(self) -> bool:
            """
                This method verifies if the browser is currently at page location
            """
    
            return self.__driver.title == self.__page_title
    ```
2. **Precise Naming**: Used self-explanatory and consistent naming for variables, functions, interfaces and classes.

    [application_submitter.py](source/executor/application_submitter.py)
    ```Python
    class ApplicationSubmitter:
        """
            This class holds the actual program functionality.
        """
    ```    
    ```Python
        def __init__(self, yaml_file_path):
            self.__yaml_file_path = yaml_file_path
            self.__configuration = None
            self.__logger = None
            self.__driver = None
    ```
    ```Python
        def set_dry_run_parameter_configuration(self):
            """
                This method will set the dry run parameter information inside configuration.
            """
    
            self.__configuration.configuration_info.dry_run = "yes"
    ```
   
3. **Single Responsibility Functions**: Tried to design and use functions in such a way so they have single tasks.

    [home_page.py](source/pages/house_of_nations/home_page.py)
    ```Python
        def get_url(self) -> str:
            """
                This method returns the page url
            """
    
            return self.__configuration.configuration_info.hon_home_url
    ```

4. **Exception Handling**: Used try-except-finally to avoid inconsistent application state.

    [app_executor.py](source/executor/app_executor.py)
    ```Python
        def __run(self, application):
            try:
                self.__display_begin_message()
                self.__handle_pre_steps()
                ...
                application.fill_step1_information_and_move_to_step_2(reservation_page1)
                self.__handle_post_steps()
            except Exception:
                self.__logger.print_log_message(LogLevel.ERROR, traceback.print_exc())
            finally:
                application.shutdown()
    ```
5. **Positive Conditionals**: Used positive conditionals and avoided negative conditionals for better readability.

    [configuration.py](source/model/configuration.py)
    ```Python
            if UrlValidator(hon_home_url).is_valid():
                self.__configuration_info.hon_home_url = hon_home_url
            else:
                raise ValueError("invalid value for hon_home_url...")
    ```

### <a name="build-management"></a>05. Build Management


### <a name="unit-tests"></a>06. Unit-Tests


### <a name="continuous-delivery"></a>07. Continuous Delivery


### <a name="ide"></a>08. IDE


### <a name="dsl"></a>09. DSL


### <a name="functional-programming"></a>10. Functional Programming


