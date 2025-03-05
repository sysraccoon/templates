This is my **personal** template collection. Any template can be initialized by using
[new-project](https://github.com/sysraccoon/new-project) utility like this:

```sh
new-project templates/rust-cli
```

But I don't use it that way. Instead, my shell config has alias to select a template using fzf:

```sh
alias np='ls -d -1 ~/store/projects/dev/templates/* | fzf | xargs -r new-project'
```
