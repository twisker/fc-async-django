# fc-async-django

## 部署 & 体验

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 构建项目：`s build --use-docker --custom-args="-i https://mirrors.aliyun.com/pypi/simple" `，
      注意，一定要使用 --use-docker 参数，特别是在Windows平台进行构建的时候。
      否则，某些依赖文件会出现与部署环境不相同而造成运行时失败。
    - 项目部署：`s deploy -y`

