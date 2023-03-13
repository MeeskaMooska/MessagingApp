json file structures:

    userdata.json:
    users(dictionary)
        \
         user_id(list)
                \
                 username(string)
                 password(string)

    messagedata.json:
    messages(dictionary)
        \
         recipient_uid(list)
                \
                 sender(list)
                    \
                     sender_uid(int)
                     sender_username(string)
                 message(string)
                        