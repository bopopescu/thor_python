<template>
    <div class="footers">
        <div class="_footer_inner">
            <span>菜鳥編碼</span>
            <span style="color: #e27575">❤</span>
        </div>
    </div>
</template>

<script>
	export default {
		name: "VFooter"
	}
</script>

<style scoped>
    .footers {
        margin-top: 25px;
        padding: 10px 0;
        background: #000;
    }
    ._footer_inner {
        min-width: 200px;
        margin: 0 auto;
        padding: 10px 0;
        text-align: center;
        font-size: 0.9em;
        color: #f0f2f5;
        letter-spacing: .2em;
    }
</style>
