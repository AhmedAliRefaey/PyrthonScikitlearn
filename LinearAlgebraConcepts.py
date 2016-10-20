import matplotlib

import sklearn


def vector_add(v,w):
     return [v_i+w_i
                for v_i,w_i in zip(v,w)]
    
def vector_subtract(v,w):
    return [v_i-w_i
               for v_i,w_i in zip(v,w) ]

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))
# user Dist Data
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]
# for each user connect with friend ..
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
#add friends property to user in Users collection..

for user in users:
    user["friends"] = []
    
for i, j in friendships:
    # this works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j]) # add i as a friend of j
    users[j]["friends"].append(users[i]) # add j as a friend of i

    def number_of_friends(user):
 
          return len(user["friends"])
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]
sorted(num_friends_by_id,                                # get it sorted
       key=lambda (user_id, num_friends): num_friends,   # by num_friends
       reverse=True)                                     # largest to smallest

def friends_of_friend_ids_bad(user):
    # "foaf" is short for "friend of a friend"
    return [foaf["id"]
            for friend in user["friends"]     # for each of user's friends
            for foaf in friend["friends"]]    # get each of _their_ friends
print [friend["id"] for friend in users[0]["friends"]]  # [1, 2]
print [friend["id"] for friend in users[1]["friends"]]  # [0, 2, 3]
print [friend["id"] for friend in users[2]["friends"]]  # [0, 1, 3]
