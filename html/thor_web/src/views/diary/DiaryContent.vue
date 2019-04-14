<template>
    <div class="diary_content">
        这里是日记内容
    </div>
</template>

<script>
	export default {
		name: "DiaryContent",
        data: () => ({
            articles: [
                {
                	name: `学习Flask第一天，阅读官方文档与git资源`,
                    content: `
                    官网地址：http://flask.pocoo.org
                    git第一个资源地址：https://github.com/pallets/flask
                    第一个dome：
                        from flask import Flask
                        app = Flask(__name__)

                        @app.route('/')
                        def hello():
                            return "Hello Python!"

                        app.run()
                    使用 pip install -U Flask 安装

                    `,
                    translationDocuments: `
                    英语----------------汉语
                    overview            概述
                    docs                文档
                    community           社区
                    extensions          扩展
                    donate              捐赠

                    @ + number 代表相同意思的翻译局
                    @1、Flask is a micro framework for python based on Werkzeug, Jinja2 and good intentions.
                        And before you ask: It's BSD licensed!
                    @1、Flask 是一个基于 Werkzeug、Jinja2 和良好意图的 Python 微框架。
                        在你问之前：这是 BSD 授权的！

                    @2、Flask is Fun
                    @2、Flask 很有趣

                    @3、Latest Version: 1.0.2
                    @3、最新版本 ******

                    @4、And Easy to Setup
                    @4、并且易于设置
                    `
                }
            ]
        })
	}
</script>

<style scoped>

</style>
