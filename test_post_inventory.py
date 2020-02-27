
import time
from RestRCI import *

log.info("\n------  test_post_inventory REST RCI api test ----------\n")

# reader = config.get("inventory","command_Driven")
# reader =reader.split(character)
reader = {"Cmd":"_GetTags","_StopCondition": 1, "_StopValue":1}

@pytest.mark.parametrize('command',reader)
def test_post_inventory(api, command):
    '''Inventory api testing'''
    time.sleep(2)
    response = requests.post(api.url,data=command)
    json_resp = json.loads(response.text)
    time.sleep(2)
    log.info("command :) {} \n response :) {}\n".format(command,json_resp))
    assert response.status_code == 200 and json_resp["Tags"][0]["ErrID"] == 0

