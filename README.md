# move-workshop

move language workshop

## Move docs

* <https://github.com/move-cn/letsmove>

## Aptos

* docs: <https://aptos.dev/en>

### Setup CLI

* <https://aptos.dev/en/build/cli/setup-cli>
* Shell COmpletion: `aptos config generate-shell-completions --shell zsh --output-file ~/.oh-my-zsh/completions/_aptos`
* `aptos config set-global-config --config-type global`

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
