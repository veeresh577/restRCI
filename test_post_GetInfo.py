
from RestRCI import *

reader = config.get("readerinfo","getinfo")
reader =reader.split(character)

log.info("\n------  Get reader  information REST RCI api test ----------\n")

@pytest.mark.parametrize('command',reader)
def test_post_getinfo(api, command):
    '''Get reader information Api testing'''

    response = requests.post(api.url,data=command)
    json_resp = json.loads(response.text)
    log.info("command :) {} \n response :) {}\n".format(command,json_resp))
    assert response.status_code == 200 and json_resp["ErrID"] == 0
