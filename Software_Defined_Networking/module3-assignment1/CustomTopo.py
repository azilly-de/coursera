#!/usr/bin/python

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel

class CustomTopo(Topo):
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)

        # Add your logic here ...
        self.fanout = fanout
        currentHost = 1
        currentEdge = 1
        currentAgg = 1

        # Core Layer
        coreSW = self.addSwitch('c1', cpu=.5/fanout)

        for a in irange(1, fanout):
            # Aggregation Layer
            aggSW = self.addSwitch('a%s' % currentAgg)
            self.addLink(aggSW, coreSW, bw=linkopts1['bw'], delay=linkopts1['delay'], loss=1, max_queue_size=1000, use_htb=True)
            currentAgg += 1
            for e in irange(1, fanout):
                # Edge Layer
                edgeSW = self.addSwitch('e%s' % currentEdge)
                self.addLink(edgeSW, aggSW, bw=linkopts2['bw'], delay=linkopts2['delay'], loss=1, max_queue_size=1000, use_htb=True)
                currentEdge += 1
                for h in irange(1, fanout):
                    # Host Layer
                    host = self.addHost('h%s' % currentHost, cpu=.5/fanout)
                    self.addLink(host, edgeSW, bw=linkopts3['bw'], delay=linkopts3['delay'], loss=1, max_queue_size=1000, use_htb=True)
                    currentHost += 1

topos = { 'custom': ( lambda: CustomTopo() ) }
