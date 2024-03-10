# Uncomment the following lines if you run the optional run_file tests locally
# so the input shows up in the output file. Do not copy these lines into Codio.
#
import sys
def input( prompt=None ):
    if prompt != None:
        print( prompt, end="" )
    aaa_str = sys.stdin.readline()
    aaa_str = aaa_str.rstrip( "\n" )
    print( aaa_str )
    return aaa_str


###############################################################################
#                       '''Programming Project 5'''
#
#     Prompt for a filename consisting of users and their friends
#     Using lists and functions to find out the amount of mutual friends between
#     each duo of users in the file/list
#
#     Prompt user for an integer
#     Using the integer as the user U's ID, find out which user V should be
#     suggested as a friend from how many mutual friends each user has
#
#     Ask user if they would like to input another user/integer or if they
#     would like to exit the program
###############################################################################


def open_file():
    '''
    Checks to see if user entered an existing filename.
    If filename exists: open file and return it to main().
    If filename does not exist: display error message and re-prompt
    user for another filename.
    '''

    # Create while loop to continue prompting user for a filename until they
    # input an existing filename
    while True:
        # Prompt user for a filename
        user_filename = input("\nEnter a filename: ")

        # Try to open the user prompted filename
        try:
            fp = open(user_filename, 'r')

            return fp

        # If user did not enter an existing filename display error message
        # and re-prompt the user for a filename
        except FileNotFoundError:
            print('\nError in filename.')


def read_file(fp):
    '''
    Creates a list called network that holds the friends
    list for each user in the file and returns it to main().
    '''

    # Create list to hold each users friends
    network = []

    # Read the first line to find n (number of users in network)
    n = fp.readline().strip()

    count = 0

    # For test cases that do not include number of users at the top
    if n.isdigit():
        x = int(n)

    else:
        for i in fp:
            count += 1
            x = count

    # Take first line (n) from network to decide how many users there are
    # and friends lists to make
    for i in range(x):
        network.append([])

    # Create friends list for each user in the network
    for line in fp:
        single_line = line.strip().split()

        u = int(single_line[0])
        v = int(single_line[1])

        network[u].append(v)
        network[v].append(u)

    return network


def num_in_common_between_lists(list1, list2):
    '''
    Finds the 'count' number of similar friends between each user.
    Returns that number to calc_similarity_scores(network) to be
    later added to the similarity_matrix list.
    '''

    # Assign count to 0 before for loop
    count = 0

    # Iterates through both user u's and user v's friends lists
    for num1 in list1:
        for num2 in list2:
            if num1 == num2:

                # If user is in both frinds lists increase count by 1
                count += 1

    return count


def calc_similarity_scores(network):
    '''
    Creates a new list called similarity_matrix that holds the number
    of mutual friends each user has with one another.
    Calls num_in_common_between_lists(list1, list2) to get the 'count' of mutual friends
    from user U to user v.
    '''

    # Finds the length of the network (how many users there are)
    n = len(network)

    # Make list to hold the count of mutual friends
    similarity_matrix = []

    # Create the rows for each user to hold their existing count of mutual friends
    # with user v and vice versa ( 2 = [[0,0,0,0] , [0,0,0,0]] )
    for i in range(n):
        row = [0] * n
        similarity_matrix.append(row)

    # Iterates through list to find friends
    for u in range(n):
        for v in range(n):
            num_in_common = num_in_common_between_lists(network[u], network[v])

            similarity_matrix[u][v] = num_in_common

    return similarity_matrix

def recommend(user_id, network, similarity_matrix):
    '''
    Assigns variable for the list that includes the user_id's count.
    Assigns variables for largest count and the user its related to.
    Finds the user with the most amount of similar friends that isn't
    already friends with the user selected and prints out the users ID.
    '''

    # Set a variable that assigns the count of mutual friends between
    # user_id (user u) and the rest of the users in the network ([x,x,x,x])
    similar_users_count = similarity_matrix[user_id]

    # Assign variables to hold the suggested friends user ID and
    # the largest count of mutual friends between the users
    most_similar_user = -1
    max_similarity_count = -1

    # For index, count in amount of iterations(0-similar_users)
    for i, count in enumerate(similar_users_count):

        # Do not count self or existing friends of user_id
        if i != user_id and i not in network[user_id]:

            # Find largest amount of mutual friends
            # (not last instance of mutual friends) tie goes to lower ID number
            if count > max_similarity_count or (count == max_similarity_count
                                                and i < most_similar_user):
                max_similarity_count = count
                most_similar_user = i

    print("\nThe suggested friend for {} is {}".format(user_id, most_similar_user))
    pass


def main():

    # by convention "main" doesn't need a docstring
    print("Facebook friend recommendation.\n")

    # Call Open_file() to get the file pointer
    fp = open_file()

    # Call read_file(fp) to get the list for the netwwork
    network = read_file(fp)

    # Call calc_similarity_scores(network) to get the the similarity_matrix
    similarity_matrix = calc_similarity_scores(network)

    # Make n the integer range of users to choose from
    n = len(network) - 1

    # Create while loop to continuously ask user if they would like
    # to find more suggested friends
    while True:
        user_ID = input("\nEnter an integer in the range 0 to {}: ".format(n))
        check = user_ID.isdigit()

        # If the user inputs a non integer display error and re-prompt
        # (for some reason I cannot combine the last two statements in the while loop)
        while check == False or int(user_ID) > n or 0 > int(user_ID):

            print("\nError: input must be an int between 0 and {}".format(n))
            user_ID = input("\nEnter an integer in the range 0 to {}: ".format(n))
            check = user_ID.isdigit()

            if check == True and 0 <= int(user_ID) <= n:
                continue

        # Make the user_ID and integer for easy iteration capabilities (line 157)
        user_ID = int(user_ID)

        # Call recommend function to get suggested friend
        recommend(user_ID, network, similarity_matrix)

        # Ask user if they would like to continue or not
        selection = input("\nDo you want to continue (yes/no)? ")
        selection = selection.lower()

        if selection == 'no':
            break

    pass


if __name__ == "__main__":
    main()

