# move-workshop

move language workshop

## Aptos

* docs: <https://aptos.dev/en>

## Sui

### Explorer

* <https://suivision.xyz/>
* <https://suiscan.xyz/mainnet/home>

### suiup

```sh
suiup install sui
suiup install mvr
suiup install walrus
```

### snapshot

```sh
sui-tool download-db-snapshot --latest --network mainnet --path /home/akagi201/sui/db --no-sign-request --skip-indexes
sui-tool download-formal-snapshot --latest --genesis /home/akagi201/sui/genesis.blob --network mainnet --path /home/akagi201/sui/db --no-sign-request
```
