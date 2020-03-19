
from RestRCI import *

reader = config.get("negative","Not_supported_field_values")
reader =reader.split(character)

log.info("\n------  Not_supported_field_values REST RCI api test ----------\n")

@pytest.mark.parametrize('command',reader)
def test_post_Not_suppoerted_fieldvalues(api, command):
    '''Get reader information Api testing'''

    response = requests.post(api.url,data=command)

    json_resp = json.loads(response.text)
    command=json.loads(command)

    log.info("command :) {} \n \t response :) {}\n".format(command,json_resp))

    assert response.status_code == 200 and json_resp["ErrID"] == 22 and json_resp["Report"] == command["Cmd"]
