import rosbag

# Importing the statistics module
import statistics

from pprint import pprint

bag = rosbag.Bag('/data/example_rosbag_H3.bag')

topics = bag.get_type_and_topic_info()[1].keys()
for topic in topics:
    msg_timestamps = []
    msg_time_deltas = []
    i = 0
    for msg_topic, msg, t in bag.read_messages(topics=[topic]):
        msg_timestamps.append(t)
        if not(i == 0):
            msg_time_deltas.append(msg_timestamps[i].to_sec()-msg_timestamps[i-1].to_sec())
        i = i+1
    print(topic + ":")
    print("\t num_messages: "+str(len(msg_time_deltas)))
    print("\t period:")
    print("\t\t min: "+str(min(msg_time_deltas)))
    print("\t\t max: "+str(max(msg_time_deltas)))
    print("\t\t average: "+str(statistics.mean(msg_time_deltas)))
    print("\t\t median: "+str(statistics.median(msg_time_deltas)))


bag.close()