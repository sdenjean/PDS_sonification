import OSC

c = OSC.OSCClient()
c.connect(('127.0.0.1', 5005))   # connect to SuperCollider
oscmsg = OSC.OSCMessage()
oscmsg.setAddress("/startup")
oscmsg.append('HELLO')
c.send(oscmsg)