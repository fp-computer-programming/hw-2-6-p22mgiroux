# Author: MOG 9/23/21

free_throws = input("How many free throws were made during the game? ")
two_pts = input("Two pointers? ")
three_pts = input("Three pointers? ")
total_pts = (int(free_throws)) + (int(two_pts) * 2) + (int(three_pts) * 3)

print("Total Pts: " + str(total_pts))