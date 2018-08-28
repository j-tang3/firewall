# firewall

# Design:
To determine whether or not a packet will be accepted by the firewall or not, my instinctual response was to iterate through all the rules, and for every rule, compare each individual element (direction, protocol, port, ip address). However, with a large set of rules, this would not be efficient. If I had additional time, I would have tested different designs in searching through all the rules. When initializing the class, I would read the csv file and separate the data into filterable sections (eg. all the rules that have direction = "inbound"), to avoid iterating through all the rules every time a new packet is encountered.

# Test: 
Given the hour allotted for this challenge, I was not able to fully test my code, but if I had additional time, I would have created a csv file with a collection of valid inputs ranging from a simple IP address to inputs including ranges. I would then initialize the firewall and test it with entries of different direction, protocol, and ranges within and outside of the initialize port and IP address, to make sure I covered all possible inputs and scenarios. 
