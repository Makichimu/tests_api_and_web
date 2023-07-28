tests = [
    ("#console > div.endpoints > ul > li:nth-child(1) > a", "test_get_list_users"),
    ("#console > div.endpoints > ul > li:nth-child(2) > a", "test_get_single_user"),
    ("#console > div.endpoints > ul > li:nth-child(3) > a", "test_get_single_user_not_found"),
    ("#console > div.endpoints > ul > li:nth-child(4) > a", "test_get_list_resource"),
    ("#console > div.endpoints > ul > li:nth-child(5) > a", "test_get_single_resource"),
    ("#console > div.endpoints > ul > li:nth-child(6) > a", "test_get_single_resource_not_found"),
    ("#console > div.endpoints > ul > li:nth-child(7) > a", "test_post_create"),
    ("#console > div.endpoints > ul > li:nth-child(8) > a", "test_put_update"),
    ("#console > div.endpoints > ul > li:nth-child(9) > a", "test_patch_update"),
    ("#console > div.endpoints > ul > li:nth-child(10) > a", "test_delete"),
    ("#console > div.endpoints > ul > li:nth-child(11) > a", "test_post_register_successful"),
    ("#console > div.endpoints > ul > li:nth-child(12) > a", "test_post_register_unsuccessful"),
    ("#console > div.endpoints > ul > li:nth-child(13) > a", "test_post_login_successful"),
    ("#console > div.endpoints>ul>li:nth-child(14)>a","test_post_login_unsuccessful"),
    ("#console>div.endpoints>ul>li:nth-child(15)>a","test_get_delayed_response")
]

