
import time
from RestRCI import *

log.info("\n------  test_post_inventory REST RCI api test ----------\n")

reader = config.get("inventory","command_Driven")
reader =reader.split(character)
# reader=[str({"Cmd":"_GetTags","_StopCondition": 3, "_StopValue":6})]
# print(reader)
# print(type(reader))

@pytest.mark.parametrize('command',reader)
def test_post_inventory(api, command):
    response = requests.post(api.url,data=command)
    time.sleep(4)
    print(command)
    json_resp = json.loads(response.text)

    print(json_resp)
    log.info("command :) {} \n \tresponse :) {}\n".format(command,json_resp))
    # error =api.GetERROR(json_resp)
    assert response.status_code == 200 and (json_resp["ErrID"] == 0 and json_resp["Tags"][0]["ErrID"] == 0 )

