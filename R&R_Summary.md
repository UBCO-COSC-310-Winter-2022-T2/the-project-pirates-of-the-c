1. Highlight what tasks were done during this cycle (by owner).   They will come from your Kanban board or tracking tool. Recall that there is an expectation of on-average, equal contribution to the project.

Kyle Keim (46335485) - Implemented a CI model by introducing a python-app.yml file to the project workflow folder that can check that a given merged pull requests 
fufills a set of pytests that must pass before a PR can be merged into the main branch.

Added and semi-populated a basic Kanban project board to the repo and started working on the database testing/coding of the project that is a work in progress.


Ryan Tschritter (47341862) - Started writing tests for a simulated iot sensor that will be deployed to a docker container. Reasearching more about how the MQTT protocol works and how the python paho-mqtt package works. Getting a better understanding of the mqtt interfacing to python to then discuss with the team. Will update the kanban board with new tasks once I have a understanding of the paho package and whats required.


Mehul Raisingh (46168746) - Currently working on the temperature control system. I have populated the kanban project board with the major tasks that need to be completed in order to fully implement the control system, this includes: writing different testing scenarios for the overall system, writing test for each individual function. I have started to implement the testing/coding components, however I ran into a couple problems and need to redesing a portion of the control system.


Einar Schiele (64296734) -



2. Summary of the progress (relative to the requirements for the project (where are you based on where you thought you were going to be;  what's done and what's left) (this will be supported by your commit logs; remember that each feature needs to be on its own branch, tested, reviewed and merged)

Kyle Keim - "I think that we are on track for creating appropriate tests to follow a TTD model for this project. Creating the Continuous Integration required for the testing of all pulled code, at least for python, was interesting to try and figure out but I managed to find an appropriate workflow through Gthub Actions. Fortunately 
the Projects tab made it really easy to create a Kanban style board so that we can easily see who is doing what task and what needs to be done."

Ryan Tschritter - "We are probably on track for where we need to be. We probably need to have another team meeting to discuss our progress and update eachother on how things have been going to make sure were all aiming for the right goal."

Mehul Raisingh - "There was unexpected problem that I ran into while designing the test for the system. This problem, was mainly to do with how the system would react to additional noise picked up by the sensor. As a result im in the process of redesign the control system to include a filter, i'm currrently figuring out what kinda of filter would be most effective and how to implemented suuitable tests for this (im thinking of creating a sine wave generator that would convulated with a noise function generator that would mimic real world noise). Although there were a few setbacks, Im sure I will be able to get this back on track."



3. Comments on the process;  how is the process you selected as a team working?  Does anything need to change?

We selected a Kanban style work process that allows use to easily see whose working on what, what needs to be done, and what is already completed. It will help
give us a good sense of what needs to be done and where we are at. I think that we could use more issues/tasks on the Kanban board that more specifically target given tasks.


4. Branches/Tasks completed and tested/merged 

PythonWorkflow Branch tested and merged. Including a failed test to check that indeed failing a given pytest will prevent the PR from merging into the main branch.


5. If you have a release candidate (something that is working, even partially, make note of that (this could be on your master branch, or you might choose to branch from master onto a release branch.  

No current release candidate available as of Milestone #4 (27/March/2023).

6. Update your testing report so you know what is working.  What's working; what's passing; what's not? 

The testing report will be updated as more of the project becomes available.
