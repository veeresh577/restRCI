
from RestRCI import *

reader = config.get("negative","Not_supported_fields")
reader =reader.split(character)

log.info("\n------  Not_supported_fields REST RCI api test ----------\n")

@pytest.mark.parametrize('command',reader)
def test_post_Not_supported_fields(api, command):
    '''Get reader information Api testing'''

    response = requests.post(api.url,data=command)

    json_resp = json.loads(response.text)
    command=json.loads(command)

    log.info("command :) {} \n \t response :) {}\n".format(command,json_resp))

    assert response.status_code == 200 and json_resp["ErrID"] == 21 and json_resp["Report"] == command["Cmd"]
