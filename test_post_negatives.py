from RestRCI import *

log.info("\n------  test_post_negatives REST RCI api test ----------\n")

reader = config.get("negative","negative_commands")
reader =reader.split(character)

@pytest.mark.parametrize('command',reader)
def test_post_negatives(api, command):
    error_codes = {21:21,22:22,1001:1001,31:31}
    response = requests.post(api.url,data=command)
    print(command)
    json_resp = json.loads(response.text)
    print(json_resp)
    log.info("command :) {} \n \t response :) {}\n".format(command,json_resp))
    # error =api.GetERROR(json_resp)
    assert response.status_code == 200 and (json_resp["ErrID"] == error_codes[json_resp["ErrID"]])

