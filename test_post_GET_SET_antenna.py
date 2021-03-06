
from RestRCI import *

log.info("\n------  test_post_GET_SET_antenna REST RCI api test ----------\n")

reader = config.get("antenna","GET_SET_antenna")
reader =reader.split(character)

@pytest.mark.parametrize('command',reader)
def test_post_GET_SET_antenna(api, command):

    response = requests.post(api.url,data=command)

    json_resp = json.loads(response.text)
    command =json.loads(command)

    log.info("command :) {} \n \t response :) {}\n".format(command,json_resp))
    # error =api.GetERROR(json_resp)
    assert response.status_code == 200 and json_resp["ErrID"] == 0 and json_resp["Report"] == command["Cmd"]






