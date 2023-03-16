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
                        
as of 3/16/23 I have decided to revise the initial client.py and client-gui.py modules. so that will be the next update. eta on that is 3/18/23
