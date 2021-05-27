import os
import json
os.environ['pipline'] = 'Staging'
from sentrycommon import CustomersandAccounts

Cust_obj = CustomersandAccounts.CustomersandAccounts()
camera_name = "room"
sentry_id = "YX3HRM8E-P"

cam_info = Cust_obj.get_camera_info_of_an_account("room","YX3HRM8E-P")
#print(cam_info)
empty_list = []
print(cam_info[0]["short_term_static_bbx"])
print(cam_info[0]["static_bounding_box"])

short_term_static_bbx = json.dumps(empty_list)
static_bounding_box = json.dumps(empty_list)

properties_to_update = {"short_term_static_bbx":short_term_static_bbx,"static_bounding_box":static_bounding_box }

Cust_obj.update_camera_info(camera_name, sentry_id, properties_to_update)
cam_info = Cust_obj.get_camera_info_of_an_account("room","YX3HRM8E-P")
print(cam_info[0]["short_term_static_bbx"])
print(cam_info[0]["static_bounding_box"])