import random
def computer_start(common_set, computer_dic, left_over):
    common_set_random = random.choice(common_set)
    left_over.append(common_set_random)
    common_set.remove(common_set_random)
    return common_set, computer_dic, left_over

