 
# wm_sound_library

ROS node providing a service that let you play a specific sound available in the library. 

## Prerequisites

* `sudo apt-get install alsa alsa-tools`


## Getting Started

* `cd ros_workdpace/src`
* `git clone https://github.com/WalkingMachine/wm_sound_library`
* `cd ..`
* `catkin_make`
* `roslaunch wm_sound_library wm_soundboard.launch`

## Services

* wm_list_sound [std_msgs/Empty]
  * return the available sounds in the library  

* wm_play_sound [std_msgs/String] 
  * play the specified sound  

## Available sounds
|           |                 |           |               |           |                  |          |                |
|-----------|-----------------|-----------|---------------|-----------|------------------|----------|----------------|
| airhorn   | badumtss        | baseball  | casser        | chewbacca | computer-startup | crickets | denied         |
| ding      | doh             | drama     | drop_the_bass | drumroll  | error            | Engine   | got_item       |
| incorrect | jeopardy        | john_cena | laugh         | murlock   | mac_startup      | R2D2     | shooting_stars |
| trollolol | to_be_continued | turn_down | thug_life     | victory   | wrong            | wazza    | yeah           |


## Running the tests

* rosservice call /wm_list_sound "{}"
  * It should list all the sound file available
 
* rosservice call /wm_play_sound "play:     
            data: 'ding.wav'"
  * It should play the ding sound
  * Use tab to auto-complete this command if you write it in your terminal


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/walkingmachine/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/walkingmachine/wm_sound_library/tags). 

## Authors

* **Jeffrey Cousineau** - *Initial work* - [JeffCousineau](https://github.com/JeffCousineau)

See also the list of [contributors](https://github.com/walkingmachine/wm_sound_library/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Free sounds : https://www.myinstants.com
