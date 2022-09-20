# Move Runtime

```sh
move new hello
move sandbox publish # 沙盒环境下发布模块
move sandbox run scripts/my_script.move # 沙盒环境下运行脚本
# 上述命令输出字符串以char code形式展现，我们利用node转换下查看内容
node -e "console.log([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100].map(code => String.fromCharCode(code)).join(''))"
```
