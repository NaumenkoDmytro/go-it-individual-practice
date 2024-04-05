topick_chosen = {1,3,8,7,2,5,10,4,6,9,12,11,12,14,15}
all_topics = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18}
topics_done = {1,2,3,5,6,7,8,9,10,11,12,13,14}
sorted_topick_chosen = sorted (topick_chosen)



print(sorted_topick_chosen)

topics_choosen_but_undone = topick_chosen.difference(topics_done)
topics_unchoosen = all_topics.difference(topick_chosen)
print(f"Topics that are chose but not done = {topics_choosen_but_undone}, topics haven't chosen yet = {topics_unchoosen}")
