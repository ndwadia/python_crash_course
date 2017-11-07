# pylint: disable=invalid-name
"""
Working with user input
"""

prompt = "I'll repeat what you say."
prompt += "\nEnter 'Quit' to exit: "
message = ''
msg_aggr = ''
while message.lower() != 'quit':
    message = input(prompt)
    if message.lower() != 'quit':
        print(message)
        msg_aggr = msg_aggr + message
    print(msg_aggr)
