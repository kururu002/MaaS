import time
from enum import Enum

def start_focused_work():
    print("Imagine yourself as an expert in the work you are about to do.")
    time.sleep(5) # sleep for 5 second to give time to imagine
    print("Starting brown noise https://www.youtube.com/watch?v=RqzGzwTY-6w.") 


def set_next_goal(goal_type):
    print("Creating a mind map with a word in the center...")
    mind_map_center = input("Enter the word in the center of the mind map: ")
    print(f"Word in the center of the mind map: {mind_map_center}")
    print("Linking at least two layers of more words...")
    layer1_words = input("Enter the words in the first layer: ").split(",")
    print(f"Words in the first layer: {layer1_words}")
    layer2_words = input("Enter the words in the second layer: ").split(",")
    print(f"Words in the second layer: {layer2_words}")
    print("Circle a few words you're interested in...")
    interested_words = input("Enter the words you're interested in: ").split(",")
    print(f"Words you're interested in: {interested_words}")
    if goal_type == "extreme":
        goal_duration = "within 3 months"
    elif goal_type == "long term":
        goal_duration = "achievable to continue"
    print(f"Goal type: {goal_type}, Duration: {goal_duration}")
    ikigai_score = calculate_ikigai()
    print(f"Ikigai score: {ikigai_score}")

def calculate_ikigai():
    print("Calculating Ikigai...")
    passion = input("What are you passionate about? ")
    mission = input("What is your mission in life? ")
    profession = input("What is your profession? ")
    vocation = input("What is your vocation? ")
    ikigai_score = (passion + mission + profession + vocation) / 4
    return ikigai_score
