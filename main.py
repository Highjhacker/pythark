from pythark import Block, Account, Delegate, Peer, Loader, MultiSignature, Signature, Transport, Transaction


if __name__ == '__main__':
    #acc = Account()
    #print(acc.get_balance("ANwjGUcVbLXpqbBUWbjUBQWkr4MWVDuJu9"))

    #b = Block()
    #print(b.get_height())
    #print(b.get_block("570934191207974498"))
    #print(b.get_blocks(limit=3, orderBy="timestamp"))

    #a = Account()
    #print(a.get_balance("ANwjGUcVbLXpqbBUWbjUBQWkr4MWVDuJu9"))
    #print(a.get_delegates("AccacXRhyBJSZ3VjQWvRuzsubes58A5gmA", orderBy="timestamp"))
    #print(a.get_top_accounts(limit=5, orderBy="timestamp"))

    #d = Delegate()
    #print(d.get_delegates_count("ANwjGUcVbLXpqbBUWbjUBQWkr4MWVDuJu9"))
    #print(d.search_delegates(query="dr", limit=2, orderBy="username"))
    #print(d.get_delegate("jarunik"))
    #print(d.get_delegates(limit=5, orderBy="username"))

    #p = Peer()
    #print(p.get_peers())
    #print(p.get_peer("78.229.106.139", 4001))
    #l = Loader()
    #print(l.get_status())

    #m = MultiSignature()
    #print(m.get_pending("02c7455bebeadde04728441e0f57f82f972155c088252bf7c1365eb0dc84fbf5de"))

    #s = Signature()
    #print(s.get_signature_fee())

    #t = Transaction()
    #print(t.get_transactions(limit=5, orderBy="timestamp"))

    t = Transport()
    print(t.get_status())