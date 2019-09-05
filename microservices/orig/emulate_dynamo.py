class emulate_dynamo:
    def __init__(self):
        self.payload = dict()
        self.__sample_data = {"Items":
          [
            {
                "stig_id": {"S": "RHEL-07-010020"},
                "status": {"S": "Not_A_Finding"}
                },
            {
                "stig_id": {"S": "RHEL-07-010010"},
                "status": {"S": "Open"}
                }
          ]
        }

    @property
    def sample_data(self):
        return self.sample_data

    @sample_data.setter
    def sample_data(self,_sample_data):
        self.sample_data = self.__sample_data

    def get_query(self,__payload):
        get = [
            item for item in self.__sample_data["Items"]
            if __payload["ExpressionAttributeValues"][":item1"]["S"]
            in item["stig_id"]["S"]
            ]
        return get

