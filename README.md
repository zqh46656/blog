# 真强悍的博客 · 更新指南

站点：[zqh46656.github.io/blog](https://zqh46656.github.io/blog/)。
使用 Marmite 0.4.2 构建，推送到 `main` 后由 GitHub Actions 自动发布。
**以下命令都在本仓库根目录（有 `marmite.yaml` 的目录）执行。**

## 每次更新

1. 同步：运行 `git status`，确认没有未完成的修改，再运行 `git pull --ff-only`。
2. 编辑：文章放 `content/posts/`，附件放 `content/media/`，路径规则见下方。
3. 预览：检查排版、图片、附件和文章链接。
4. 检查：重新构建发布版本，运行链接检查。
5. 发布：确认改动后提交、推送，在 GitHub Actions 查看发布结果。

## 文件放哪里

| 要更新的内容 | 编辑或放置的位置 |
| --- | --- |
| 新文章、已有文章 | `content/posts/文章名.md` |
| 图片、视频、PDF、其他附件 | `content/media/文章名/文件名` |
| 关于本站 | `content/pages/about.md` |
| 其他独立页面（不带日期） | `content/pages/页面名.md` |
| 首页欢迎语、最新文章列表 | `content/index.md` |
| 博客名称、导航、分类、配色 | `marmite.yaml` |
| 自定义样式 | `custom.css` |
| 写作模板 | `examples/post.md`，复制后再编辑 |

`site/` 是自动生成的结果，不在里面写文章或修改样式，也不用提交。
文件名建议使用小写英文、数字和连字符，如 `my-post.md`；文件名和引用的大小写必须一致。

## 写文章

复制模板，或在 `content/posts/` 手动创建 `my-post.md`：

```markdown
---
date: 2026-10-12 12:00:00
tags: 游戏,解谜
stream: games
---
# 我的文章标题

这里写正文。
```

- `date`：改成文章的实际发布日期；带日期才会作为文章进入首页、归档和 RSS。
- `tags`：多个标签用**英文逗号**分隔，尽量复用已有标签。
- `stream`：从下表选一个分类；不填写时进入默认分类。
- `# 标题`：正文开头写文章标题。

| `stream` 值 | 分类 |
| --- | --- |
| `games` | 游戏评测 |
| `movies` | 影评与拉片 |
| `discussions` | 其它讨论 |
| `tools` | 工具和资源 |

也可以用命令生成文章，再补上 `stream` 和正文：

```sh
marmite . --new "我的新文章" -d posts -t "游戏,解谜"
```

“游戏评测”导航始终保留。暂无文章时访问会返回 404，链接检查允许这种空分类；
发布首篇 `stream: games` 的文章后，会自动生成分类页，无需额外操作。

## 放资源、写链接

建议按文章分文件夹。以 `my-post.md` 为例：

```text
content/
├── posts/my-post.md
└── media/my-post/
    ├── photo.jpg
    ├── demo.mp4
    └── notes.pdf
```

文章和页面中都这样引用：

```markdown
![照片说明](media/my-post/photo.jpg)
[打开或下载 PDF](media/my-post/notes.pdf)
[打开或下载视频](media/my-post/demo.mp4)
```

正文资源路径从 **`media/`** 开始，不写 `content/media/`、`../media/` 或 `/media/`。
已有的 `content/media/文件名` 也可继续使用，对应引用 `media/文件名`。
图片一般用 JPG、PNG 或 WebP。需要直接播放视频时，可写：

```html
<video controls preload="metadata" style="width: 100%;">
  <source src="media/my-post/demo.mp4" type="video/mp4">
</video>
```

视频建议使用 H.264/AAC 的 MP4；较大的视频可放视频平台，再添加完整链接。
附件链接最方便，PDF 内嵌预览在部分手机上不可用，仍需保留下载链接。

**链接到另一篇文章时，使用生成的 HTML 文件名。** 例如 `stream: tools` 的
`my-post.md` 默认生成 `tools-my-post.html`：

```markdown
[阅读另一篇文章](tools-my-post.html)
```

不确定文件名时，构建后查 `site/urls.json`。修改已发布文章的文件名或 `stream`
可能改变 URL；如需保留旧链接，可在文章头部添加 `aliases: 旧文件名不含.html`。

## 本地预览和发布检查

首次使用：安装 [Marmite 0.4.2](https://github.com/rochacbruno/marmite/releases/tag/0.4.2)
和 Python 3.9 或更高版本。已有 Rust 的电脑可运行：

```sh
cargo install marmite --version 0.4.2 --locked
```

启动预览，然后打开 <http://127.0.0.1:8000>：

```sh
marmite . site --url http://127.0.0.1:8000 --watch --serve --bind 127.0.0.1:8000
```

修改后自动重新生成，刷新浏览器查看；`Ctrl+C` 停止。
`--url` 只覆盖本次预览地址，不用修改 `marmite.yaml` 中的正式站点地址。

**发布前停止预览，重新构建正式版本并检查：**

```sh
marmite . site --verbose
python3 scripts/build_feed.py site
python3 scripts/check_links.py site
```

检查通过后仍应在浏览器确认图片、PDF、视频和外部链接可用。
`build_feed.py` 将各分类的新文章合并到 `index.rss`，保留最新 15 篇并去重；
全站只公开这一个订阅入口。预览的自动重建会重置 RSS，检查订阅时需重新执行此脚本。
脚本检查内部页面、导航、静态资源、附件和目录锚点；外部网站需手动确认。

## 提交和发布

```sh
git status
git diff
git add .
git diff --cached --stat
git commit -m "更新博客：说明本次修改"
git push origin main
```

提交前确认文章和附件都已包含。推送后在仓库的 **Actions** 中查看
`Deploy Marmite to GitHub Pages`；任务成功后刷新正式站点。

## 常见问题

| 现象 | 先检查 |
| --- | --- |
| 文章没有出现在首页 | 是否放在 `content/posts/`，是否填写 `date` |
| 多个标签变成一个 | `tags` 是否用了中文逗号，改为英文逗号 |
| 图片或附件打不开 | 文件是否存在、大小写是否一致、引用是否以 `media/` 开始 |
| 文章链接 404 | 构建后查 `site/urls.json`，注意分类前缀 |
| 本地预览没有样式、导航打不开 | 是否使用上面的 `--url` 预览命令 |
| 发布失败 | 查看 Actions 失败步骤，按提示修正缺失文件或链接 |
| Git 拉取提示有冲突或本地修改 | 先处理、提交或保存当前修改，再拉取；不要直接覆盖 |

新建独立页面可运行 `marmite . --new "联系我" -p -d pages`，需要导航时在
`marmite.yaml` 的 `menu` 添加 `["联系我", "页面文件名.html"]`。
历史版本用 Git 查看，`*.bak*` 备份不要提交。
更多用法见 [Marmite 入门指南](https://marmite.blog/getting-started.html)。
