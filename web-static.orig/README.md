p2pool-node-status
==================


## Installation

### Parallel to the default web-static

To run this UI in parallel to your current p2pool web interface, do in your web-static directory:

``` Bash
git clone https://github.com/farsider350/node-stats-btc.git
```

You can then access the UI per `http://<url-to-your-p2pool>:<port>/static/node-stats/`

### As web-static replacement

To replace your current web-static, do in the top directory of your p2pool installation

``` Bash
mv web-static _web-static-pre
git clone https://github.com/farsider350/node-stats-btc.git web-static
```

and access as usually per `http://<url-to-your-p2pool>:<port>/static`

### On a different host

This UI can be run on a different web server as well.  The web server must than provide at least PHP in order to execute the JSONP handler.

You need to configure the host and port of your p2pool server in the config.json like

``` JavaScript
var config = {
  myself : [],
  host : "http://p2pool.org:9332",
  reload_interval : 30,
  reload_chart_interval : 600,
  use_fontawesome : true
}
```

**Beware**:  The UI queries the p2pool API periodically.  This will put additional network traffic on your p2pool server.  It can, but must not, result in a higher variance!

## Configuration

The `config.json` is found in `js` directory.

### Highlight your own miner address

If you want your miner address highlighted, adjust `myself` variable accordingly. E. g.

``` JavaScript
var config = {
  myself : [
    "12nQSWig35Wue2AGjiGM5F2LUvSwq8uQqS",
    "1MsuC6knLeZKHCyQ39Xcw1qcgScS1ZK5R"
  ],
  host : "",
  reload_interval : 30,
  reload_chart_interval : 600,
  use_fontawesome : true
}
```

### Point the UI to a different p2pool server


You need to configure the host and port of your p2pool server in the `host` variable like

``` JavaScript
var config = {
  myself : [],
  host : "http://p2pool.org:9332",
  reload_interval : 30,
  reload_chart_interval : 600,
  use_fontawesome : true
}
```

### Adjust the reload interval

Per default the UI updates the miner list and server stats every 30 seconds.  You can adjust the `reload_interval` variable like

``` JavaScript
var config = {
  myself : [],
  host : "",
  reload_interval : 20,
  reload_chart_interval : 1200,
  use_fontawesome : true
}
```

to set it to 20 seconds for example.

`reload_chart_interval` sets the amount of seconds until the hashrate graph is reloaded.  In above example, it's configured to 1200 seconds (20 minutes).

**Beware** that each API query puts network and CPU load on your p2pool installation.  Avoid decreasing this value too much.  In my tests, 20 to 30 seconds seem to be fair enough.

### Disable Fontawesome Bitcoin icon

On Bitcoin p2pools, this UI uses the Fontawesome Bitcoin icon per default.  This can be disabled per `use_fontawesome` configuration option.  Set it to false if don't want to use the bitcoin icon.

``` JavaScript
var config = {
  myself : [],
  host : "",
  reload_interval : 30,
  reload_chart_interval : 600,
  use_fontawesome : false
}
```

If this variable is set to `false`, the UI displays the p2pool currency symbol (BTC).

*This does only apply to Bitcoin pools.  On other cryptocurrencies, the UI displays whatever p2pool API replies as currency symbol.*

### Donate

If you like this tool, find it useful or if you just find it useful, that people out there writing free software for everybody to use or contribute, please donate some coins:

Bitcoins 12nQSWig35Wue2AGjiGM5F2LUvSwq8uQqS  


--------------------------

:wq!

