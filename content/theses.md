---
# An instance of the Blank widget.
# Documentation: https://sourcethemes.com/academic/docs/page-builder/
widget: blank

# Activate this widget? true/false
active: true

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 0

title: Thesis Topics
subtitle:

design:
  columns: "2"
  #background:
    #image: headers/bubbles-wide.jpg
    #image_darken: 0.6
    #image_parallax: true
    #image_position: center
    #image_size: cover
    #text_color_light: true
  spacing:
    padding: ["10px", "0", "10px", "0"]
---
You can find a list of possible thesis topics for MSc and BSc students below.
Feel free to contact me if you have questions or want to discuss additional topics: wohlrab@chalmers.se

* Resolving conflicts in robot mission planning
	* Description: In real-world robotic systems, it often happens that requirements are in conflict with each other. For example, a cleaning robot shall clean a room. At the same time, there might be a requirement mandating that a cleaning robot's battery level should never be below 2%. In some situations, it could be possible for the robot to finish the cleaning task if that battery level requirement is violated. The battery level would fall below 2%, but given that the cleaning task can be accomplished in that case, violating that requirement might be worth it. When is it worth ignoring a requirement to fulfill another one? How should systems know which requirements to prioritize? What strategies can we create so that conflicts can be resolved? The goal of the thesis is to develop a system that selects appropriate strategies to resolve conflicts automatically.
* Replanning missions for robotic systems
	* Description: Robots need to plan their actions. Currently, planning systems tend to assume that you can create a plan once and execute it. In practice, that might not be feasible. A lot of things can happen (e.g., robots can break) and that might require replanning a mission at runtime. Sometimes, replanning can take a long time. Sometimes, humans might need to be involved to fix a broken robot. This thesis focuses on creating mechanisms to replan robotic missions, so that an optimal path can be found even in uncertain contexts.
* Human interaction with robotic systems
	* Description: See the description above. Sometimes, robots might break and humans need to fix mechanical issues. How should that interaction be initiated? When is it a good time to ask a human for help? What is needed to help humans prioritize and schedule their repair tasks?
* Architectural sketches in practice
	* Description: It is very common that architects and developers create whiteboard sketches to draft their ideas for the design of a software system. Those sketches can have different properties and purposes. The idea for this thesis is to investigate how these diagrams are created and used in practice. What do "good" architectural sketches look like? How often and in which phases in the development process do stakeholders use such sketches? Ideally, you have a contact with a company to pursue this topic.
