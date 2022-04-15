# my-kitty-config

## usage

```shell
# backup your config first
# mv ~/.config/kitty  ~/.config/kitty.bak

git clone https://github.com/ttys3/my-kitty-config.git ~/.config/kitty
```

## Shortcuts

key name see <https://github.com/xkbcommon/libxkbcommon/blob/master/include/xkbcommon/xkbcommon-keysyms.h>

or using `kitty --debug-input` to detect keysyms

### config

| key                                       | description   |
|-------------------------------------------|---------------|
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>r</kbd> | reload config |
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>e</kbd> | reload config |
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>d</kbd> | debug config  |

### session

| key                                       | description                         |
|-------------------------------------------|-------------------------------------|
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>s</kbd> | save current layout to session file |

### tab

| key                                           | description        |
|-----------------------------------------------|--------------------|
| <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>⭠</kbd> | previus tab        |
| <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>⭢</kbd> | next tab           |
| <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>,</kbd> | move tab backward  |
| <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>.</kbd> | move tab forward   |
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>,</kbd>     | change tab title   |
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>c</kbd>     | create new tab     |
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>x</kbd>     | close window / tab |

### os window

| key                          | description       |
|------------------------------|-------------------|
| <kbd>ctrl</kbd>+<kbd>q</kbd> | quit kitty        |
| <kbd>f11</kbd>               | toggle fullscreen |

### window

| key                                           | description                  |
|-----------------------------------------------|------------------------------|
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>-</kbd>     | horizontal split             |
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>\\</kbd>     | vertial split                |
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>x</kbd>     | close window                 |
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>z</kbd>     | zoom (maxmize) window        |
| <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>r</kbd> | resize window                |
| <kbd>ctrl</kbd>+<kbd>⭠</kbd>                  | to left window               |
| <kbd>ctrl</kbd>+<kbd>⭢</kbd>                  | to right window              |
| <kbd>ctrl</kbd>+<kbd>⭡</kbd>                  | to up window                 |
| <kbd>ctrl</kbd>+<kbd>⭣</kbd>                  | to down window               |
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>h</kbd>     | to left window               |
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>l</kbd>     | to right window              |
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>k</kbd>     | to up window                 |
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>j</kbd>     | to down window               |
| <kbd>shift</kbd>+<kbd>⭠</kbd>                 | move current window to left  |
| <kbd>shift</kbd>+<kbd>⭢</kbd>                 | move current window to right |
| <kbd>shift</kbd>+<kbd>⭡</kbd>                 | move current window to up    |
| <kbd>shift</kbd>+<kbd>⭣</kbd>                 | move current window to down  |
| <kbd>alt</kbd>+<kbd>⭠</kbd>                   | resize window narrower       |
| <kbd>alt</kbd>+<kbd>⭢</kbd>                   | resize window wider          |
| <kbd>alt</kbd>+<kbd>⭡</kbd>                   | resize window taller         |
| <kbd>alt</kbd>+<kbd>⭣</kbd>                   | resize window shorter        |
| <kbd>ctrl</kbd>+<kbd>home</kbd>               | resize window reset          |

### font

| key                          | description     |
|------------------------------|-----------------|
| <kbd>ctrl</kbd>+<kbd>=</kbd> | font size +     |
| <kbd>ctrl</kbd>+<kbd>-</kbd> | font size -     |
| <kbd>ctrl</kbd>+<kbd>0</kbd> | font size reset |

### misc

| key                                                       | description                                                                          |
|-----------------------------------------------------------|--------------------------------------------------------------------------------------|
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>t</kbd>                 | kitten themes                                                                        |
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>space</kbd>             | copy pasting with hints like [tmux-thumbs](https://github.com/fcsonline/tmux-thumbs) |
| <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>ctrl</kbd>+<kbd>a</kbd> | send real <kbd>ctrl</kbd>+<kbd>a</kbd> (emacs shortcut <kbd>Home</kbd>)              |

## session restore

> if you have used <kbd>ctrl</kbd>+<kbd>a</kbd>><kbd>s</kbd> generate the session, you do not need this.

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

Keyboard shortcuts <https://sw.kovidgoyal.net/kitty/conf/#keyboard-shortcuts>

The launch command syntax reference <https://sw.kovidgoyal.net/kitty/launch/#syntax-reference>
