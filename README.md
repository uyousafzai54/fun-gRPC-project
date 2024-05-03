# fun-gRPC-project
location ping that needs quorum (I need to use my Tokyo server)

All you need is a gRCP server constantly listening on one port. It accepts a number and a list of some IP addrs.

Once it recieves these, it can then spawn threads and assign an IP to each. 

These sub-servers then finish the connection with the clients.
