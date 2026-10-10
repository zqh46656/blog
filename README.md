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

带日期的内容会作为文章显示在首页。图片放在 `content/media/`，正文中使用
`![图片说明](media/photo.png)` 引用。

## 添加页面

```sh
marmite . --new "联系我" -p -d pages
```

页面放在 `content/pages/`，不带日期。修改关于页请编辑
`content/pages/about.md`；需要导航入口时，在 `marmite.yaml` 的 `menu` 中添加
`["联系我", "生成的文件名.html"]`。

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
