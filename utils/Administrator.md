## Code
    define the class administrator that inherits from the user class which is parent
        function __init__(info)
            call parent constructor(info, user_type="administrator")

    function manage_user_accounts(library, action, user=None)
        if action is "add"
            call library.add_user(user)
        else if action is "remove"
            call library.remove_user(user)
        else
            print "invalid action"
