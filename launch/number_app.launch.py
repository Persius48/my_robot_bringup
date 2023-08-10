from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    remap_num_channel_topic = ("num_channel","my_number")

    number_publisher_node = Node(
        package = "my_py_pkg",
        executable = "number_publisher",
        name = "my_number_publisher" ,          #changes node name
        remappings = [remap_num_channel_topic], #for remapping topics & Services
        parameters = [                          #for remaping parameter
            {"number_to_publish": 4},
            {"publish_frequency": 5.0}
        ]
    )
    number_counter_node = Node(
        package="my_cpp_pkg",
        executable="number_counter",
        name="my_number_counter",
        remappings = [remap_num_channel_topic,      
                      ("num_count","my_counter")],
        
        

    )

    ld.add_action(number_publisher_node)
    ld.add_action(number_counter_node)

    return ld