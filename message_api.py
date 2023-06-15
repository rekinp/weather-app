import http.client, urllib

class MessageAPI:
    def __init__(self, token, user):
        self.conn = http.client.HTTPSConnection("api.pushover.net:443")
        self.token = token
        self.user = user

    def push_message(self, message):
        try:
            self.conn.request("POST", "/1/messages.json",
                          urllib.parse.urlencode({
                              "token": self.token,
                              "user": self.user,
                              "message": message,
                          }), {"Content-type": "application/x-www-form-urlencoded"})
            self.conn.getresponse()
        except http.client.HTTPException as e:
            # Handle HTTP-related exceptions here
            print(f"HTTPException occurred: {e}")

        except Exception as e:
            # Handle other exceptions here
            print(f"Exception occurred: {e}")

        finally:
            self.conn.close()