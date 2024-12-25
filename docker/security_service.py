from glob import has_magic

import zoo
import jwt
import sys
import json


def securityIn(main_conf,inputs,outputs):
    has_auth=False
    for i in main_conf["renv"].keys():
        if i.count("HTTP_AUTHORIZATION")>0:
            json_object=jwt.decode(main_conf["renv"][i].split(' ')[1], options={"verify_signature": False})
            has_auth=True
            if "preferred_username" in json_object.keys():
                main_conf["auth_env"]={"user": json_object["preferred_username"]}
            if "email" in json_object.keys():
                main_conf["auth_env"]["email"]=json_object["email"]

    if "auth_env" in main_conf:
        print(main_conf["auth_env"],file=sys.stderr)
    if has_auth or main_conf["lenv"]["secured_url"]=="false":
        return zoo.SERVICE_SUCCEEDED
    else:
        if "headers" in main_conf:
            main_conf["headers"]["status"]="403 Forbidden"
        else:
            main_conf["headers"]={"status":"403 Forbidden"}
        main_conf["lenv"]["code"]="NotAllowed"
        main_conf["lenv"]["message"]="Unable to ensure that you are allowed to access the resource."
        return zoo.SERVICE_FAILED