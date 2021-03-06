
from RestRCI import *

reader = config.get("readerinfo","getinfo")
reader =reader.split(character)

log.info("\n------  Get reader  information REST RCI api test ----------\n")

@pytest.mark.parametrize('command',reader)
def test_post_getinfo(api, command):
    '''Get reader information Api testing'''

    response = requests.post(api.url,data=command)

    json_resp = json.loads(response.text)
    command=json.loads(command)

    log.info("command :) {} \n \t response :) {}\n".format(command,json_resp))

    assert response.status_code == 200 and json_resp["ErrID"] == 0 and json_resp["Report"] == command["Cmd"]
