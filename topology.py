from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=RemoteController )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )
    h3 = net.addHost( 'h3', ip='10.0.0.3' )
    h4 = net.addHost( 'h4', ip='10.0.0.4' )

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )
    s4 = net.addSwitch( 's4' )
    s5 = net.addSwitch( 's5' )
    s6 = net.addSwitch( 's6' )
    s7 = net.addSwitch( 's7' )
    s8 = net.addSwitch( 's8' )
    s9 = net.addSwitch( 's9' )
    s10 = net.addSwitch( 's10' )

    info( '*** Creating links\n' )
    net.addLink( h1, s10 )
    net.addLink( s3, s10 )
    net.addLink( s4, s10 )
    net.addLink( s1, s3 )
    net.addLink( s1, s4 )
    net.addLink( s1, s2 )
    net.addLink( s1, s6 )
    net.addLink( s6, s9 )
    net.addLink( s2, s9 )
    net.addLink( h2, s9 )
    net.addLink( s5, s4 )
    net.addLink( s4, s7 )
    net.addLink( s5, s7 )
    net.addLink( s5, s6 )
    net.addLink( s5, s8 )
    net.addLink( s6, s8 )
    net.addLink( h3, s8 )
    net.addLink( h4, s7 )

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
