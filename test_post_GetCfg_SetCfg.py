
from RestRCI import *

log.info("\n------  test_post_GetCgf REST RCI api test ----------\n")

# read commands from setting.ini
reader = config.get("readercapabilities","GetCgf")
reader = reader.split(character)

@pytest.mark.parametrize('command',reader)
def test_post_GetCgf_SetCfg(api, command):

    response = requests.post(api.url,data=command)

    json_resp = json.loads(response.text)
    command= json.loads(command)

    log.info("command :) {} \n \t response :) {}\n".format(command,json_resp))
    assert response.status_code == 200 and json_resp["ErrID"] == 0 and json_resp["Report"] == command["Cmd"]
