# Bitcoin Hash
Calculates the hash of a bitcoin block.

### Run
```bash
$ python bitcoinHash.py -u https://blockchain.info/rawblock/000000000000000000046308409bb6a9fe11d98529efd3c50ba0445e06bc8746
```
```bash
$ python bitcoinHash.py -f 000000000000000000046308409bb6a9fe11d98529efd3c50ba0445e06bc8746.json
```

### Usage
```
options:
  -h, --help            show this help message and exit
  -v, --verbose         display intermediate hash
  -f FILE, --file FILE  read the block from a json file
  -u URL, --url URL     read the block from a URL
```

### Algorithm description
https://en.bitcoin.it/wiki/Block_hashing_algorithm
