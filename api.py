from pushbullet import Pushbullet

pb = Pushbullet("o.t8XGOI0l8fEuYdqerxxxxxxxxxxxxxxx")
#  Depending on your devices, might be device[1] or similar.
phone = pb.devices[0]
pb.push(phone, "Reciever Number", "Enter message")
