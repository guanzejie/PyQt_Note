import shotgun_api3

"""
sg = shotgun_api3.Shotgun("https://guanguan.shotgrid.autodesk.com",
                          login="guanzejie@gmail.com",
                          password="13622865573Gzj")
"""
sg = shotgun_api3.Shotgun("https://guanguan.shotgrid.autodesk.com",
                          script_name="guanguan",
                          api_key="xkhhoxk7habzofJdicutzecj-")

name=sg.find("HumanUser",[["name", "is", "guan guan"]],["name", "id"])

project=sg.find_one("Project",[["name","is","PROJECT"]],["name"])


cc=sg.get_session_token()

#task=sg.find_one("Task",[["name","is","PROJECT"]],["id","type"])

#print(task)

print(name)

n=sg.create("Note",{"project" : project,  "sg_note_type":u"通知",  "content":u"你好吗111111111",  "addressings_to":name})
