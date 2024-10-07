mad_libs = "{} laughed at the {} {}." 

print(mad_libs.format("bobby", "green", "alien"))


print(mad_libs.format("sam", "hot", "turtle"))

mad_libs = "{2} laughed at the {1} {0}." 

print(mad_libs.format("bobby", "green", "alien"))


print(mad_libs.format("sam", "hot", "turtle"))

mad_libs = "{name} laughed at the {adj} {noun}." 

print(mad_libs.format(name = "bobby", adj = "green", noun = "alien"))


print(mad_libs.format(name = "sam", adj = "hot", noun = "turtle"))
print(mad_libs.format(adj = "hot", name = "sam", noun = "turtle"))


name = input("enter a name: ")
adj = input("enter an adjective: ")
noun = input("enter a noun: ")

print(mad_libs.format(name = name, adj = adj, noun = noun))
