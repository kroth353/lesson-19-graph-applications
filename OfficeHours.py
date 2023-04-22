import networkx as nx
#14

#Edges per node
# 1 -> 5 #2 -> 3 #3 -> 4 #4 -> 4 #5 -> 5 #6 -> 2 #7 -> 4 #8 -> 4 #9 -> 4 #10 -> 4
#11 -> 2 #12 -> 3 #13 -> 2 #14 -> 2 #15 -> 2 #16 -> 2 #17 -> 2 #18 -> 2 #19 -> 2 #20 -> 2 

#movie theater on 17th street, home is on 2nd street
#1st -- 2nd (6) 5th (8) 13th (3) 8th (13)
#2nd -- 9th (1) 6th (17) 15th (8)
#3rd -- 18th (18) 12th (3) 20th (23) 1st (5)
#4th -- 3rd (2) 16th (8) 19th (4) 10th (14)
#5th -- 13th (7) 17th (20) 15th (10) 18th (6)
#6th -- 11th (3) 19th (5) 12th (2) 7th (8)
#7th -- 14th (2) 8th (9) 20th (4) 
#8th -- 12th (8) 17th (2)
#9th -- 14th (4) 6th (11) 16th (10)
#10th -- 20th (15) 11th (3)


Roads = ["1st 2nd {'weight': 6}", "1st 5th {'weight': 8}", "1st 13th {'weight': 3}", "1st 8th {'weight': 13}",
         "2nd 9th {'weight': 1}", "2nd 6th {'weight': 17}", "2nd 15th {'weight': 8}",
         "3rd 18th {'weight': 18}", "3rd 12th {'weight': 3}", "2nd 20th {'weight': 23}",
         "4th 3rd {'weight': 2}", "4th 16th {'weight': 8}", "4th 19th {'weight': 4}", "4th 10th {'weight': 14}",
         "5th 13th {'weight': 17}", "5th 17th {'weight': 20}", "5th 15th {'weight': 10}", "5th 18th {'weight': 6}",
         "6th 11th {'weight': 3}", "6th 19th {'weight': 5}", "6th 12th {'weight': 2}", "6th 7th {'weight': 8}",
         "7th 14th {'weight': 2}", "7th 8th {'weight': 9}", "7th 20th {'weight': 4}",
         "8th 12th {'weight': 8}", "7th 17th {'weight': 2}",
         "9th 14th {'weight': 4}", "9th 6th {'weight': 11}", "9th 16th {'weight': 10}",
         "10th 20th {'weight': 15}", "10th 11th {'weight': 3}"]

G = nx.parse_edgelist(Roads, nodetype=str)
nx.draw_weighted_edgelist(G, "test.weighted.edgelist")
#print(list(G))
print(list(G.edges))
