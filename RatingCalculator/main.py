def rating_calculator():
    global rating

    rating = (like_number / (like_number + dislike_number)) *100


def rating_show():
    print ("the video's liked rate: %", rating)

    if (rating >70):
        print("the video likes a lot")
    elif (rating >50):
        print("the video likes")
    else:
        print("the video not liked")



def user_input():

    global like
    global dislike
    global like_number
    global dislike_number

    print ("please enter the liked amount:  ")

    try: like_number = int(input())


    except ValueError:
        print ("Please enter the numeric expo!")
        user_input()


    print ("Enter the dislike amount:  ")
    try: dislike_number = int(input())
    except ValueError:
        print("Please enter the numeric expo!")
        user_input()
