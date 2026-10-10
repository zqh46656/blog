# zqh 的博客

使用 [Marmite](https://marmite.blog/) 生成的个人博客。

站点地址：<https://zqh46656.github.io/blog/>

## 本地预览

安装 Marmite 0.4.2 后，在仓库根目录运行：

```sh
marmite . site --serve
```

打开 <http://localhost:8000>。文章位于 `content/posts/`，独立页面位于
`content/pages/`，站点配置位于 `marmite.yaml`。

## GitHub Pages 部署

在仓库 **Settings → Pages → Build and deployment → Source** 中选择
**GitHub Actions**。推送到 `main` 后，`Deploy Marmite to GitHub Pages`
工作流会使用 Marmite 0.4.2 构建并发布 `site/`。

也可以在 **Actions** 中手动运行该工作流。生成的 `site/` 已加入
`.gitignore`，无需提交构建产物。

部署方式参考 [Marmite 官方托管说明](https://marmite.blog/hosting.html)。
