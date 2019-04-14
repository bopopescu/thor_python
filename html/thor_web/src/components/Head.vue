<template>
    <div class="head">
        <div class="head_inner">
            <a href="/" class="logo">菜鸟日记</a>
            <ul class="_nav">
                <li v-for="(item, index) in nav" :key="index"><a :href="item.path">{{ item.name }}</a></li>
            </ul>
        </div>
    </div>
</template>

<script>
	export default {
		name: "VHead",
        data: () => ({
            nav: [
                { path: '/diary', name: '日记' },
                { path: '/python', name: 'python' },
                { path: '/php', name: 'php' },
                { path: '/javascript', name: 'javascript' },
            ]
        })
	}
</script>

<style scoped>
    .head {
        background: #0593d3;
        box-shadow: 0 1px 11px 2px #66b1ff;
        height: 48px;
        margin-bottom: 25px;
    }
    .head_inner {
        max-width: 1720px;
        margin: 0 auto;
        overflow: auto;
    }
    .logo {
        font-size: 24px;
        color: #fff;
        display: block;
        padding: 0 15px;
        line-height: 48px;
        float: left;
    }
    ._nav {
        float: left;
        margin-left: 30px;
        height: 48px;
    }
    ._nav>li {
        float: left;
        padding: 0 15px;
        height: 48px;
        line-height: 48px;

    }
    ._nav>li:hover {
        background: #0371a1;
    }
    ._nav>li>a {
        font-size: 18px;
        color: #fff;
    }
</style>
