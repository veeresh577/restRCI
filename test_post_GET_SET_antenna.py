
from RestRCI import *

reader = config.get("antenna","GET_SET_antenna")
reader =reader.split(character)

@pytest.mark.parametrize('command',reader)
def test_post_GET_SET_antenna(api, command):

    response = requests.post(api.url,data=command)
    json_resp = json.loads(response.text)
    log.info("command :) {} \n response :) {}\n".format(command,json_resp))
    # error =api.GetERROR(json_resp)
    assert response.status_code == 200 and json_resp["ErrID"] == 0






