import requests as req

base = 'http://172.17.0.2:5001'
# TODO: Need to be actual nodes for consensus!
client1 = 'http://0.0.0.0:3000'
client2 = 'http://0.0.0.1:3000'

# Register new node
resp = req.post(base + '/nodes/register', {'nodes': client1})
print(resp)
resp = req.post(base + '/nodes/register', {'nodes': client2})
print(resp)

# Create new transaction 
#resp = req.post(base + '/transactions/new', {'sender': client1, 'recipient': client2, 'amount': 'some_hash'})
#print(resp)

# Mining (already does the transaction hardcoded)
resp = req.get(base + '/mine')
print(resp)

# Consensus
#resp = req.get(base + '/nodes/resolve')
#print(resp)
