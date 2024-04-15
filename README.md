# Autonomous-Crawlspace-Inspection-Robot
This GitHub contains all relevant files used during development. For a comprehensive guide to the repository set up see the bottom of the document.
## Executive Summary
Crawl spaces grant convenient access to the plumbing, duct work, and electrical wiring of a house, but they often present unique dangers to maintenance professionals and residents alike. Exposure to harsh breathing conditions, hanging obstacles, uncomfortable working positions, and even animals can cause non-ideal conditions. This capstone project will focus on the design and assembly of a robot prototype that can perform these inspections autonomously. The end product will be an autonomous, mobile robot that can be left unattended in a crawlspace by an inspector. It will navigate through the space, create a map and model of the space, compile an image of the entire crawlspace ceiling, and collect sensor data. This sensor data will include humidity, temperature, and wood moisture content.

## Current Robot Capabilities
The first iteration of the project focused on setting up the hardware systems. Sensors, microcontrollers, motors, and power circuits were designed and implemented as part of a larger multi-group project. The following details the current capabilities of the robot.

* Low-level autonomy which allows the robot to navigate through an enclosed area
* Creating a map of the area using the SLAM algorithm
* Take pictures throughout an area and stitch simple areas into a singular, larger image
* Collect humidity, temperature, and moisture content data and overlay information on images
* Supply power for consistent operation across all components
* Robot movement through serial commands and return encoder data to the main microcontroller
* Manual control through text-based commands while also streaming live video to the operator
