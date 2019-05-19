import random
import time

from InstagramAPI import InstagramAPI


def insta_login(username, password):
    """
        This method will receive a username and password of Instagram
        and login at this account.

        Parameters:
            username -> str
            password -> str

        return: None

    """

    insta = InstagramAPI(username, password)
    insta.login()
    return insta


def get_comments_of_one_media(insta, media_id):
    """
        This method will receive a media_id
        and get comments of this media.

        Parameters:
            insta -> InstagramAP
            media_id -> str

        return:
            data_comments -> list

    """

    # The left ID before the underscore means the media id.
    # The right ID after the underscore means the account id.
    # You can get this ids in html page of your media.
    # Probably exist a better way to do this, but that way was faster.
    insta.getMediaComments(media_id)
    data_comments = insta.LastJson["comments"]
    return data_comments


def get_users_comments(data_comments):
    """
        This method will receive a dict with data of comments in one media_id.
        So, will get just the comments text and who made this comment.

        Parameters:
            data_comments -> dict

        return:
        user_comments -> list

    """
    user_comments = []
    for comment in data_comments:
        user_comments.append(
            {"username": comment["user"]["username"],
             "comment": comment["text"]}
        )
    return user_comments


def get_likes_of_one_media(insta, media_id):
    insta.getMediaLikers("2039514162951220054_12737953228")
    return insta.LastJson["users"]


def verify_if_user_liked(username, user_likes):
    """
        Verify if user that win the prize was liked the instagram photo.

        Parameters:
            username -> str
            user_list -> list
        return:
           liked -> bool

    """

    time.sleep(3)
    liked = False
    for user in user_likes:
        if username == user["username"]:
            liked = True
    return liked


def execute_prize():
    """
        main method to execute the instagram prize.
    """

    insta = insta_login("username", "password")
    data_comments = get_comments_of_one_media(insta, "2039514162951220054_12737953228")
    user_comments = get_users_comments(data_comments)

    winner = user_comments[random.randint(0, len(user_comments) - 1)]
    username = winner["username"]

    print("O ganhador foi: @" + username + ".")

    print("Agora vamos verificar se ele curtiu a foto...")
    user_likes = get_likes_of_one_media(insta, "2039514162951220054_12737953228")
    liked = verify_if_user_liked(username, user_likes)

    if liked:
        print("Parabéns @" + username + ", você curtiu a foto."
              " Irei entrar em contato com você.")
    else:
        print("Não curtiu a foto :(. Teremos que escolher outro.")


if __name__ == "__main__":
    execute_prize()
