# pylint: disable=invalid-name
"""
Working with user input
"""

prompt = "I'll repeat what you say."
prompt += "\nEnter 'Quit' to exit: "
active = True
message = ''
msg_aggr = ''
while active:
    message = input(prompt)
    if message.lower() == 'quit':
        active = False
    else:
        print(message)
        msg_aggr = msg_aggr + ' ' + message
print(msg_aggr)
