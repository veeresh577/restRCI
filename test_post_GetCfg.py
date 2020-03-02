
from RestRCI import *

log.info("\n------  test_post_GetCgf REST RCI api test ----------\n")

reader = config.get("readercapabilities","GetCgf")
reader =reader.split(character)

@pytest.mark.parametrize('command',reader)
def test_post_GetCgf(api, command):

    response = requests.post(api.url,data=command)
    json_resp = json.loads(response.text)
    log.info("command :) {} \n \t response :) {}\n".format(command,json_resp))
    assert response.status_code == 200 and json_resp["ErrID"] == 0
