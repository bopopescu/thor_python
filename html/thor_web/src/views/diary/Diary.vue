<template>
    <div class="diary">
        <div class="c-content">
            <p>1</p>
            <p>2</p>
            <p>3</p>
            <p>4</p>
            <p>5</p>
            <p>6</p>
            <p>7</p>
            <p>8</p>
            <p>9</p>
            <p>10</p>
        </div>
    </div>
</template>

<script>
	export default {
		name: "Diary",
		components: {

		},
		data: () => ({
			// 左侧导航，仅限二级导航
			nav_bar: [
				{
					path: '/',
					title: '标题',
					subs: false
				},
				{
					path: '',
					title: '內容',
					subs: [
						{
							path: '/home_content',
							title: '內容1',
							index: '2-1'
						},
						{
							path: '/home_content',
							title: '內容2',
							index: '2-2'
						}
					]
				},
				{
					path: '',
					title: '文本编辑器',
					subs: false
				}
			]
		})
	}
</script>
