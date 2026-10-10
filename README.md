# zqh 的博客

使用 [Marmite](https://marmite.blog/) 生成的个人博客。

站点地址：<https://zqh46656.github.io/blog/>

## 预览博客

需要 Marmite 0.4.2；尚未安装时可运行 `cargo install marmite --version 0.4.2 --locked`
（需要 Rust），或下载 [预编译版本](https://github.com/rochacbruno/marmite/releases/tag/0.4.2)。
以下命令均在仓库根目录运行：

```sh
marmite . site --watch --serve --bind 127.0.0.1:8000
```

打开 <http://localhost:8000>。修改文件后会自动重新生成，刷新浏览器查看结果；
按 `Ctrl+C` 停止。

## 写文章

```sh
marmite . --new "我的新文章" -d posts -t "笔记,技术"
```

编辑生成在 `content/posts/` 下的 Markdown 文件。也可以手动新建，例如
`content/posts/my-post.md`：

```markdown
---
date: 2026-10-10
tags: 笔记,技术
---
# 我的新文章

这里写正文。
```

带日期的内容会作为文章显示在首页。

## 添加页面

```sh
marmite . --new "联系我" -p -d pages
```

页面放在 `content/pages/`，不带日期。修改关于页请编辑
`content/pages/about.md`；需要导航入口时，在 `marmite.yaml` 的 `menu` 中添加
`["联系我", "生成的文件名.html"]`。

## 添加图片、视频和 PDF

将文件放入 `content/media/`（没有这个目录就新建），也可以按文章分子目录：

```text
content/media/my-post/
├── photo.jpg
├── diagram.svg
├── demo.mp4
└── notes.pdf
```

无论文章在 `content/posts/` 还是页面在 `content/pages/`，正文均用
`media/my-post/文件名` 引用。构建后页面都在站点顶层，因此不用写
`../media/`、`content/media/` 或 `/media/`。路径和文件名大小写需一致；
建议使用不带空格的文件名。下面的示例直接粘贴到 Markdown 正文即可。

### 图片

JPG/JPEG、PNG、GIF、WebP、SVG、AVIF 使用相同的 Markdown 写法：

```markdown
![照片说明](media/my-post/photo.jpg)
![截图说明](media/my-post/screenshot.png)
![动图说明](media/my-post/animation.gif)
![图片说明](media/my-post/photo.webp)
![示意图](media/my-post/diagram.svg)
![图片说明](media/my-post/photo.avif)
```

照片通常用 JPG 或 WebP；截图、透明图片用 PNG 或 WebP；动图用 GIF；
矢量图用 SVG。AVIF 适合较新的浏览器；需要兼容旧浏览器时提供 JPG/WebP 版本。
HEIC、TIFF 等格式建议先导出为 JPG 或 PNG。

需要控制图片宽度时使用 HTML：

```html
<img src="media/my-post/photo.jpg" alt="照片说明"
     width="600" style="max-width: 100%; height: auto;" loading="lazy">
```

### 视频

优先使用 H.264 视频、AAC 音频编码的 MP4，也可以提供 WebM 版本。
使用 `<video>` 显示播放控件：

```html
<video controls preload="metadata" style="width: 100%;">
  <source src="media/my-post/demo.mp4" type="video/mp4">
  <source src="media/my-post/demo.webm" type="video/webm">
  你的浏览器不支持视频播放。
</video>

<p><a href="media/my-post/demo.mp4">打开或下载视频</a></p>
```

只有 MP4 时删掉 WebM 那一行。也可使用 OGV（`type="video/ogg"`），
实际能否播放取决于浏览器和文件内的编码。MOV、MKV、AVI 建议先转换成
H.264/AAC MP4；直接修改文件扩展名无法转换格式。

需要封面时，将封面图片放入同一目录，并在 `<video>` 标签中添加
`poster="media/my-post/cover.jpg"`。较大的视频可以上传到视频平台，
在文章中添加视频链接或使用平台提供的嵌入代码。

### PDF 和其他附件

最简单的方式是添加链接，读者点击后打开或下载文件：

```markdown
[查看 PDF 笔记](media/my-post/notes.pdf)
[下载 ZIP 附件](media/my-post/files.zip)
```

需要在文章内预览 PDF 时使用 HTML，并保留打开链接：

```html
<object data="media/my-post/notes.pdf" type="application/pdf"
        style="width: 100%; height: 700px;">
  <p>无法预览 PDF，请使用下方链接打开。</p>
</object>

<p><a href="media/my-post/notes.pdf">打开或下载 PDF</a></p>
```

PDF 内嵌预览依赖浏览器，部分手机浏览器需要通过链接打开。

添加文件后，用上面的本地预览命令检查图片、播放视频、打开 PDF。
发布时将文章和 `content/media/` 下的文件一起提交；Marmite 会将媒体复制到
生成的站点中。

## 修改外观

- `marmite.yaml`：博客名称 `name`、简介 `tagline`、导航 `menu`、配色 `extra.colorscheme`。
- `content/_hero.md`：首页介绍。
- `custom.css`：自定义样式。

## 发布更新

```sh
git add .
git commit -m "更新博客"
git push origin main
```

Pages 来源设为 **GitHub Actions** 后，推送到 `main` 会自动构建和发布。
只需生成静态文件时运行 `marmite . site`，生成的 `site/` 无需提交。

更多用法见 [Marmite 入门指南](https://marmite.blog/getting-started.html)。
