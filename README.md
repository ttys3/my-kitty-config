# my-kitty-config


## usage

```shell
# backup your config first
# mv ~/.config/kitty  ~/.config/kitty.bak

git clone https://github.com/ttys3/my-kitty-config.git ~/.config/kitty
```

## Shortcuts

key name see https://github.com/xkbcommon/libxkbcommon/blob/master/include/xkbcommon/xkbcommon-keysyms.h

or using `kitty --debug-input` to detect keysyms

### config

| key  | description  |
|---|---|
| ctrl+shift+r  | reload config  |
| ctrl+a>r  | reload config  |

### tab

| key  | description  |
|---|---|
| ctrl+shift+left  | previus tab  |
| ctrl+shift+right  | next tab  |
| ctrl+shift+,  | move tab backward  |
| ctrl+shift+.  | move tab forward |
| ctrl+a>,  | change tab title |
| ctrl+a>c  | create new tab |
| ctrl+a>x  | close window / tab |

### window

| key  | description  |
|---|---|
| ctrl+a>-  | horizontal split |
| ctrl+a>\  | vertial split |
| ctrl+shift+r  | resize window |
| ctrl+left  | to left window|
| ctrl+right  | to right window|
| ctrl+up  | to up window|
| ctrl+down| to down window|
| ctrl+a>h  | to left window|
| ctrl+a>l  | to right window|
| ctrl+a>k  | to up window|
| ctrl+a>j| to down window|
| shift+left  | move current window to left|
| shift+right  | move current window to right|
| shift+up  | move current window to up|
| shift+down  | move current window to down|
| alt+left  | resize window narrower |
| alt+right  | resize window wider |
| alt+up  | resize window taller |
| alt+down  | resize window shorter |
| ctrl+home  | resize window reset |


### font

| key  | description  |
|---|---|
| ctrl+=  | font size + |
| ctrl+-  | font size - |
| ctrl+0  | font size reset |

## session restore

you can create your session file under `~/.config/kitty`, let's say the filename is `session.conf`

change `startup_session none` to `startup_session session.conf`

create `session.conf` like this:

```ini
new_tab home
layout splits
cd ~
launch zsh
focus

new_tab work
cd ~/work
launch zsh

new_tab nvim
cd ~/.config/nvim
launch zsh

new_tab go
cd ~/repo/go
launch zsh

new_tab rust
cd ~/repo/rust
launch zsh
```

## kitty docs

Keyboard shortcuts https://sw.kovidgoyal.net/kitty/conf/#keyboard-shortcuts

The launch command syntax reference https://sw.kovidgoyal.net/kitty/launch/#syntax-reference
