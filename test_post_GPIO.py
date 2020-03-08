
from RestRCI import * 
log.info("\n------  test_post_Getgpio REST RCI api test ----------\n")

reader = config.get("GPIO","GET_gpi")
reader =reader.split(character)

@pytest.mark.parametrize('command',reader)
def test_post_Getgpio(api, command):
    
    response = requests.post(api.url,data=command)
    print(command)
    json_resp = json.loads(response.text)
    print(json_resp)
    log.info("command :) {} \n \t response :) {}\n".format(command,json_resp))
    # error =api.GetERROR(json_resp)
    assert response.status_code == 200 and json_resp["ErrID"] == 0






