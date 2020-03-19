
from RestRCI import *

log.info("\n------  test_post_inventory REST RCI api test ----------\n")

reader = config.get("inventory","command_Driven")
reader =reader.split(character)

@pytest.mark.parametrize('command',reader)
def test_post_inventory(api, command):
    time.sleep(3)
    response = requests.post(api.url,data=command)

    log.info("command :) {} \n \tresponse :) {}\n".format(command,response.text))

    condition = True
    json_resp = json.loads(response.text)
    tags=json_resp["Tags"]

    if len(tags):
        for i in range(0,len(tags)):
            if not tags[i]["ErrID"] == 0 :
                condition = False
    else:
        condition = False
        log.info("\t Empty Tags \n")

    command=json.loads(command)

    assert response.status_code == 200 and condition and json_resp["Report"] == command["Cmd"]

